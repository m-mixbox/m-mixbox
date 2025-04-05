<?php
// Start session if not already started
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Check if user is logged in and is an admin
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true || !isset($_SESSION["role"]) || $_SESSION["role"] !== "admin"){
    header("location: ../auth/login.php");
    exit;
}

require_once "../config/db.php";
require_once "../utils/admin_functions.php";

// Fetch statistics
$stats = [];

// Total users (excluding admins)
$sql = "SELECT COUNT(*) as total_users FROM users WHERE role = 'user'";
$stmt = $pdo->query($sql);
$stats['total_users'] = $stmt->fetch()['total_users'];

// Conversion statistics
$sql = "SELECT 
    COUNT(*) as total_conversions,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as successful_conversions,
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed_conversions
FROM file_conversions";
$stmt = $pdo->query($sql);
$stats['conversions'] = $stmt->fetch();

// Recent user activities with usernames
$sql = "SELECT fc.*, u.username 
        FROM file_conversions fc 
        JOIN users u ON fc.user_id = u.id 
        ORDER BY fc.created_at DESC 
        LIMIT 10";
$stmt = $pdo->query($sql);
$recent_activities = $stmt->fetchAll();

// Admin logs with usernames
$sql = "SELECT al.*, u.username 
        FROM admin_logs al 
        JOIN users u ON al.admin_id = u.id 
        ORDER BY al.created_at DESC 
        LIMIT 10";
$stmt = $pdo->query($sql);
$admin_logs = $stmt->fetchAll();

// Log this dashboard view
logAdminAction($pdo, $_SESSION['id'], 'view_logs', 'Accessed admin dashboard');
?>

<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
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
            margin-bottom: 20px;
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
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-shield-alt me-2"></i>
                Admin Dashboard
            </a>
            <div class="navbar-nav ms-auto">
                <a class="nav-item nav-link" href="../index.php">
                    <i class="fas fa-exchange-alt me-2"></i>
                    Converter Dashboard
                </a>
                <span class="nav-item nav-link">
                    <i class="fas fa-user-shield me-2"></i>
                    <?php echo htmlspecialchars($_SESSION["username"]); ?>
                </span>
                <a class="nav-item nav-link" href="../auth/logout.php">
                    <i class="fas fa-sign-out-alt me-2"></i>
                    Logout
                </a>
            </div>
        </div>
    </nav>

    <div class="container animate-fadeIn">
        <!-- Statistics -->
        <div class="row g-4 mb-4">
            <div class="col-md-3">
                <div class="card stats-card">
                    <div class="number"><?php echo $stats['total_users']; ?></div>
                    <div class="label">Total Users</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stats-card">
                    <div class="number"><?php echo $stats['conversions']['total_conversions']; ?></div>
                    <div class="label">Total Conversions</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stats-card">
                    <div class="number text-success"><?php echo $stats['conversions']['successful_conversions']; ?></div>
                    <div class="label">Successful</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card stats-card">
                    <div class="number text-danger"><?php echo $stats['conversions']['failed_conversions']; ?></div>
                    <div class="label">Failed</div>
                </div>
            </div>
        </div>

        <!-- Recent Activities -->
        <div class="card mb-4">
            <div class="card-header bg-transparent">
                <h5 class="mb-0">
                    <i class="fas fa-history me-2"></i>
                    Recent User Activities
                </h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Username</th>
                                <th>Original File</th>
                                <th>Converted File</th>
                                <th>Type</th>
                                <th>Status</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach($recent_activities as $activity): ?>
                            <tr>
                                <td>
                                    <i class="fas fa-user me-2"></i>
                                    <?php echo htmlspecialchars($activity['username']); ?>
                                </td>
                                <td>
                                    <i class="fas fa-file me-2"></i>
                                    <?php echo htmlspecialchars($activity['original_filename']); ?>
                                </td>
                                <td>
                                    <i class="fas fa-file-alt me-2"></i>
                                    <?php echo htmlspecialchars($activity['converted_filename']); ?>
                                </td>
                                <td>
                                    <span class="badge bg-primary">
                                        <?php echo htmlspecialchars($activity['conversion_type']); ?>
                                    </span>
                                </td>
                                <td>
                                    <?php if($activity['status'] == 'completed'): ?>
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
                                    <?php echo date('M d, Y H:i', strtotime($activity['created_at'])); ?>
                                </td>
                            </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Admin Logs -->
        <div class="card">
            <div class="card-header bg-transparent">
                <h5 class="mb-0">
                    <i class="fas fa-shield-alt me-2"></i>
                    Admin Activity Logs
                </h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Admin</th>
                                <th>Action</th>
                                <th>Description</th>
                                <th>IP Address</th>
                                <th>Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach($admin_logs as $log): ?>
                            <tr>
                                <td>
                                    <i class="fas fa-user-shield me-2"></i>
                                    <?php echo htmlspecialchars($log['username']); ?>
                                </td>
                                <td>
                                    <span class="badge bg-info">
                                        <?php echo htmlspecialchars($log['action_type']); ?>
                                    </span>
                                </td>
                                <td><?php echo htmlspecialchars($log['description']); ?></td>
                                <td>
                                    <i class="fas fa-network-wired me-2"></i>
                                    <?php echo htmlspecialchars($log['ip_address']); ?>
                                </td>
                                <td>
                                    <i class="fas fa-calendar me-2"></i>
                                    <?php echo date('M d, Y H:i', strtotime($log['created_at'])); ?>
                                </td>
                            </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>