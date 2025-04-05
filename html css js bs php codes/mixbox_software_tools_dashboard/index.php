<?php
// Previous PHP code remains the same until the HTML part
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: auth/login.php");
    exit;
}

require_once "config/db.php";

// API endpoint configuration
define('API_BASE_URL', 'http://localhost:8000');

// Previous PHP functions remain the same
function uploadFile($file, $conversionType) {
    $target_dir = "uploads/";
    if (!file_exists($target_dir)) {
        mkdir($target_dir, 0777, true);
    }
    
    $target_file = $target_dir . basename($file["name"]);
    
    if (move_uploaded_file($file["tmp_name"], $target_file)) {
        $curl = curl_init();
        
        $endpoint = API_BASE_URL . "/upload/" . $conversionType . "/";
        
        $cfile = new CURLFile($target_file, $file['type'], $file['name']);
        
        curl_setopt_array($curl, [
            CURLOPT_URL => $endpoint,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => ['file' => $cfile]
        ]);
        
        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        
        curl_close($curl);
        
        global $pdo;
        $sql = "INSERT INTO file_conversions (user_id, original_filename, converted_filename, conversion_type, status) 
                VALUES (:user_id, :original_filename, :converted_filename, :conversion_type, :status)";
        
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            ':user_id' => $_SESSION['id'],
            ':original_filename' => $file['name'],
            ':converted_filename' => 'converted_' . $file['name'],
            ':conversion_type' => $conversionType,
            ':status' => ($httpCode == 200) ? 'completed' : 'failed'
        ]);
        
        unlink($target_file);
        
        if ($httpCode == 200) {
            header('Content-Type: application/octet-stream');
            echo $response;
            exit;
        }
        
        return $httpCode == 200;
    }
    return false;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_FILES["file"])) {
        $conversionType = $_POST["conversion_type"];
        $success = uploadFile($_FILES["file"], $conversionType);
        
        if ($success) {
            $success_message = "File converted successfully!";
        } else {
            $error_message = "Error converting file.";
        }
    }
}

// Fetch statistics
$sql = "SELECT 
            COUNT(*) as total_conversions,
            SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as successful_conversions,
            SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed_conversions
        FROM file_conversions 
        WHERE user_id = :user_id";
$stmt = $pdo->prepare($sql);
$stmt->execute([':user_id' => $_SESSION['id']]);
$stats = $stmt->fetch();

// Fetch conversion history
$sql = "SELECT * FROM file_conversions WHERE user_id = :user_id ORDER BY created_at DESC LIMIT 10";
$stmt = $pdo->prepare($sql);
$stmt->execute([':user_id' => $_SESSION['id']]);
$conversions = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Conversion Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-gradient-start: #1a1c2e;
            --bg-gradient-end: #2d324d;
            --card-bg: rgba(255, 255, 255, 0.05);
            --card-border: rgba(255, 255, 255, 0.1);
        }

        body {
            background: linear-gradient(135deg, var(--bg-gradient-start), var(--bg-gradient-end));
            min-height: 100vh;
            padding-bottom: 20px;
        }

        .navbar {
            background: var(--card-bg) !important;
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--card-border);
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 15px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(4px);
        }

        .stats-card {
            text-align: center;
            padding: 20px;
        }

        .stats-card .number {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .upload-zone {
            border: 2px dashed var(--card-border);
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 20px;
            display: none;
        }

        .upload-zone.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }

        .upload-zone:hover {
            border-color: #4facfe;
            background: rgba(79, 172, 254, 0.1);
        }

        .conversion-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .nav-tabs {
            border-bottom: none;
            margin-bottom: 20px;
        }

        .nav-tabs .nav-link {
            border: none;
            color: rgba(255, 255, 255, 0.7);
            padding: 15px 25px;
            border-radius: 10px;
            margin-right: 10px;
            transition: all 0.3s ease;
        }

        .nav-tabs .nav-link:hover {
            color: #fff;
            background: rgba(79, 172, 254, 0.1);
        }

        .nav-tabs .nav-link.active {
            color: #fff;
            background: linear-gradient(45deg, #4facfe, #00f2fe);
            border: none;
        }

        .conversion-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin: 15px 0;
            color: #fff;
        }

        .conversion-desc {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            margin-bottom: 20px;
        }

        .theme-toggle {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 50%;
            width: 45px;
            height: 45px;
            cursor: pointer;
            transition: all 0.3s ease;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .theme-toggle:hover {
            transform: scale(1.1);
        }

        .table {
            margin: 0;
        }

        .table th {
            border-top: none;
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
        }

        .table td {
            color: rgba(255, 255, 255, 0.9);
            vertical-align: middle;
        }

        .badge {
            padding: 8px 12px;
            border-radius: 8px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .animate-fadeIn {
            animation: fadeIn 0.5s ease forwards;
        }

        .conversion-container {
            padding: 20px;
            border-radius: 15px;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-exchange-alt me-2"></i>
                File Converter
            </a>
            <div class="navbar-nav ms-auto">
                <?php if(isset($_SESSION["role"]) && $_SESSION["role"] === "admin"): ?>
                    <a class="nav-item nav-link" href="admin/dashboard.php">
                        <i class="fas fa-shield-alt me-2"></i>
                        Admin Dashboard
                    </a>
                <?php endif; ?>
                <span class="nav-item nav-link">
                    <i class="fas fa-user<?php echo ($_SESSION["role"] === "admin" ? "-shield" : ""); ?> me-2"></i>
                    <?php echo htmlspecialchars($_SESSION["username"]); ?>
                    <?php if(isset($_SESSION["role"]) && $_SESSION["role"] === "admin"): ?>
                        <span class="badge bg-primary ms-1">Admin</span>
                    <?php endif; ?>
                </span>
                <a class="nav-item nav-link" href="auth/logout.php">
                    <i class="fas fa-sign-out-alt me-2"></i>
                    Logout
                </a>
            </div>
        </div>
    </nav>

    <div class="container animate-fadeIn">
        <?php if(isset($success_message)): ?>
            <div class="alert alert-success fade show">
                <i class="fas fa-check-circle me-2"></i>
                <?php echo $success_message; ?>
            </div>
        <?php endif; ?>
        
        <?php if(isset($error_message)): ?>
            <div class="alert alert-danger fade show">
                <i class="fas fa-exclamation-circle me-2"></i>
                <?php echo $error_message; ?>
            </div>
        <?php endif; ?>

        <!-- Statistics -->
        <div class="row g-4 mb-4">
            <div class="col-md-4">
                <div class="card stats-card">
                    <div class="number" data-target="<?php echo $stats['total_conversions']; ?>">0</div>
                    <div class="label">Total Conversions</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card stats-card">
                    <div class="number text-success" data-target="<?php echo $stats['successful_conversions']; ?>">0</div>
                    <div class="label">Successful</div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card stats-card">
                    <div class="number text-danger" data-target="<?php echo $stats['failed_conversions']; ?>">0</div>
                    <div class="label">Failed</div>
                </div>
            </div>
        </div>

        <!-- Conversion Tabs -->
        <div class="card mb-4">
            <div class="card-body">
                <ul class="nav nav-tabs" id="conversionTabs" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#imageTab" type="button">
                            <i class="fas fa-image me-2"></i>Image to DOCX
                        </button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#jsonTab" type="button">
                            <i class="fas fa-file-code me-2"></i>GSTR 1 JSON to Excel
                        </button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#pdfTab" type="button">
                            <i class="fas fa-file-pdf me-2"></i>GSTR 3B to Excel
                        </button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#excelTab" type="button">
                            <i class="fas fa-file-excel me-2"></i>Excel to Tally XML
                        </button>
                    </li>
                </ul>

                <div class="tab-content" id="conversionTabContent">
                    <div class="tab-pane fade show active" id="imageTab">
                        <div class="conversion-container">
                            <h3 class="conversion-title">Convert Image to DOCX</h3>
                            <p class="conversion-desc">Convert your images into editable Word documents. Supports JPG and PNG formats.</p>
                            <div class="upload-zone active" data-type="image">
                                <i class="fas fa-image conversion-icon"></i>
                                <h5>Drop your image here</h5>
                                <p class="text-muted">or click to browse</p>
                                <form method="post" enctype="multipart/form-data" class="d-none">
                                    <input type="hidden" name="conversion_type" value="image">
                                    <input type="file" name="file" accept="image/*" required>
                                </form>
                            </div>
                        </div>
                    </div>

                    <div class="tab-pane fade" id="jsonTab">
                        <div class="conversion-container">
                            <h3 class="conversion-title">Convert GSTR 1 JSON to Excel</h3>
                            <p class="conversion-desc">Transform your GSTR 1 JSON return data into organized Excel spreadsheets for analysis.</p>
                            <div class="upload-zone" data-type="json">
                                <i class="fas fa-file-code conversion-icon"></i>
                                <h5>Drop your JSON file here</h5>
                                <p class="text-muted">or click to browse</p>
                                <form method="post" enctype="multipart/form-data" class="d-none">
                                    <input type="hidden" name="conversion_type" value="json">
                                    <input type="file" name="file" accept=".json" required>
                                </form>
                            </div>
                        </div>
                    </div>

                    <div class="tab-pane fade" id="pdfTab">
                        <div class="conversion-container">
                            <h3 class="conversion-title">Convert GSTR 3B to Excel</h3>
                            <p class="conversion-desc">Convert your GSTR 3B PDF returns into Excel format for better analysis and record keeping.</p>
                            <div class="upload-zone" data-type="pdf">
                                <i class="fas fa-file-pdf conversion-icon"></i>
                                <h5>Drop your PDF file here</h5>
                                <p class="text-muted">or click to browse</p>
                                <form method="post" enctype="multipart/form-data" class="d-none">
                                    <input type="hidden" name="conversion_type" value="pdf">
                                    <input type="file" name="file" accept=".pdf" required>
                                </form>
                            </div>
                        </div>
                    </div>

                    <div class="tab-pane fade" id="excelTab">
                        <div class="conversion-container">
                            <h3 class="conversion-title">Convert Excel to Tally XML</h3>
                            <p class="conversion-desc">Convert your Excel spreadsheets into Tally-compatible XML format for direct import into Tally software.</p>
                            <div class="upload-zone" data-type="excel">
                                <i class="fas fa-file-excel conversion-icon"></i>
                                <h5>Drop your Excel file here</h5>
                                <p class="text-muted">or click to browse</p>
                                <form method="post" enctype="multipart/form-data" class="d-none">
                                    <input type="hidden" name="conversion_type" value="excel">
                                    <input type="file" name="file" accept=".xlsx,.xls" required>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Conversion History -->
        <div class="card">
            <div class="card-header bg-transparent">
                <h5 class="mb-0">
                    <i class="fas fa-history me-2"></i>
                    Recent Conversions
                </h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Original File</th>
                                <th>Converted File</th>
                                <th>Type</th>
                                <th>Status</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach($conversions as $conversion): ?>
                            <tr>
                                <td>
                                    <i class="fas fa-file me-2"></i>
                                    <?php echo htmlspecialchars($conversion['original_filename']); ?>
                                </td>
                                <td>
                                    <i class="fas fa-file-alt me-2"></i>
                                    <?php echo htmlspecialchars($conversion['converted_filename']); ?>
                                </td>
                                <td>
                                    <span class="badge bg-primary">
                                        <?php echo htmlspecialchars($conversion['conversion_type']); ?>
                                    </span>
                                </td>
                                <td>
                                    <?php if($conversion['status'] == 'completed'): ?>
                                        <span class="badge bg-success">
                                            <i class="fas fa-check me-1"></i>
                                            Completed
                                        </span>
                                    <?php else: ?>
                                        <span class="badge bg-danger">
                                            <i class="fas fa-times me-1"></i>
                                            Failed
                                        </span>
                                    <?php endif; ?>
                                </td>
                                <td>
                                    <i class="fas fa-calendar me-2"></i>
                                    <?php echo date('M d, Y H:i', strtotime($conversion['created_at'])); ?>
                                </td>
                            </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <button class="theme-toggle" id="themeToggle">
        <i class="fas fa-sun"></i>
    </button>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Theme Toggle
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        const icon = themeToggle.querySelector('i');

        function toggleTheme() {
            if (html.getAttribute('data-bs-theme') === 'dark') {
                html.setAttribute('data-bs-theme', 'light');
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
                document.documentElement.style.setProperty('--bg-gradient-start', '#f8f9fa');
                document.documentElement.style.setProperty('--bg-gradient-end', '#e9ecef');
            } else {
                html.setAttribute('data-bs-theme', 'dark');
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
                document.documentElement.style.setProperty('--bg-gradient-start', '#1a1c2e');
                document.documentElement.style.setProperty('--bg-gradient-end', '#2d324d');
            }
        }

        themeToggle.addEventListener('click', toggleTheme);

        // Animated Statistics
        const numbers = document.querySelectorAll('.number');
        numbers.forEach(number => {
            const target = parseInt(number.getAttribute('data-target'));
            const increment = target / 30;
            let current = 0;

            const updateNumber = () => {
                if(current < target) {
                    current += increment;
                    number.textContent = Math.round(current);
                    setTimeout(updateNumber, 50);
                } else {
                    number.textContent = target;
                }
            };

            updateNumber();
        });

        // Tab Change Handler
        document.querySelectorAll('.nav-link').forEach(tab => {
            tab.addEventListener('click', () => {
                // Hide all upload zones
                document.querySelectorAll('.upload-zone').forEach(zone => {
                    zone.classList.remove('active');
                });
                
                // Show the upload zone for the active tab
                const tabId = tab.getAttribute('data-bs-target');
                const uploadZone = document.querySelector(`${tabId} .upload-zone`);
                uploadZone.classList.add('active');
            });
        });

        // Drag and Drop File Upload
        document.querySelectorAll('.upload-zone').forEach(zone => {
            const form = zone.querySelector('form');
            const input = form.querySelector('input[type="file"]');

            zone.addEventListener('click', () => input.click());

            zone.addEventListener('dragover', (e) => {
                e.preventDefault();
                zone.style.borderColor = '#4facfe';
                zone.style.background = 'rgba(79, 172, 254, 0.1)';
            });

            zone.addEventListener('dragleave', () => {
                zone.style.borderColor = '';
                zone.style.background = '';
            });

            zone.addEventListener('drop', (e) => {
                e.preventDefault();
                zone.style.borderColor = '';
                zone.style.background = '';
                
                const file = e.dataTransfer.files[0];
                if (file) {
                    const dataTransfer = new DataTransfer();
                    dataTransfer.items.add(file);
                    input.files = dataTransfer.files;
                    form.submit();
                }
            });

            input.addEventListener('change', () => {
                if (input.files.length > 0) {
                    form.submit();
                }
            });
        });
    </script>
</body>
</html>