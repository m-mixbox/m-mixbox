<?php
// Define variables and initialize with empty values
$name = $email = $message = "";
$name_err = $email_err = $message_err = "";

// Define an array to hold errors for additional fields
$field_err = [];

// Processing form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty($_POST["name"])) {
        $name_err = "Please enter your name.";
    } else {
        $name = test_input($_POST["name"]);
        // Check if name only contains letters and whitespace
        if (!preg_match("/^[a-zA-Z-' ]*$/", $name)) {
            $name_err = "Only letters and white space allowed";
        }
    }

    // Validate email
    if (empty($_POST["email"])) {
        $email_err = "Please enter your email address.";
    } else {
        $email = test_input($_POST["email"]);
        // Check if email address is well-formed
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $email_err = "Invalid email format";
        }
    }

    // Validate message
    if (empty($_POST["message"])) {
        $message_err = "Please enter your message.";
    } else {
        $message = test_input($_POST["message"]);
    }

    // Validate additional fields
    for ($i = 1; $i <= 27; $i++) {
        $fieldName = "field_" . $i;
        if (empty($_POST[$fieldName])) {
            $field_err[$i] = "Please enter a value for Field " . $i . ".";
        } else {
            // Additional validation can be added here if necessary
        }
    }
}

// Function to sanitize and validate input data
function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Long Form Validation with PHP</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .error {color: red;}
        .submitted-data { display: none; }
    </style>
</head>
<body>

<div class="container">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <h2 class="mt-5">Long Form Validation with PHP</h2>
            <form id="myForm" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                <!-- Name -->
                <div class="form-group">
                    <label>Name:</label>
                    <input type="text" name="name" class="form-control" value="<?php echo isset($name) ? $name : ''; ?>" required>
                    <span class="error"><?php echo isset($name_err) ? $name_err : ''; ?></span>
                </div>
                <!-- Email -->
                <div class="form-group">
                    <label>Email:</label>
                    <input type="text" name="email" class="form-control" value="<?php echo isset($email) ? $email : ''; ?>" required>
                    <span class="error"><?php echo isset($email_err) ? $email_err : ''; ?></span>
                </div>
                <!-- Message -->
                <div class="form-group">
                    <label>Message:</label>
                    <textarea name="message" class="form-control" rows="5" required><?php echo isset($message) ? $message : ''; ?></textarea>
                    <span class="error"><?php echo isset($message_err) ? $message_err : ''; ?></span>
                </div>
                <?php
                // Adding 27 additional input fields with validation errors
                for ($i = 1; $i <= 27; $i++) {
                    $fieldName = "field_" . $i;
                    echo '<div class="form-group">';
                    echo '<label>Field ' . $i . ':</label>';
                    echo '<input type="text" name="' . $fieldName . '" class="form-control">';
                    echo '<span class="error">';
                    if (isset($field_err[$i])) {
                        echo $field_err[$i];
                    }
                    echo '</span>';
                    echo '</div>';
                }
                ?>
                <!-- Submit Button -->
                <div class="form-group">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>

            <!-- Submitted Data -->
            <div class="submitted-data">
                <h2>Submitted Data:</h2>
                <p><strong>Name:</strong> <?php echo $name; ?></p>
                <p><strong>Email:</strong> <?php echo $email; ?></p>
                <p><strong>Message:</strong> <?php echo $message; ?></p>
                <!-- Additional Fields -->
                <?php
                for ($i = 1; $i <= 27; $i++) {
                    $fieldName = "field_" . $i;
                    echo '<p><strong>Field ' . $i . ':</strong> ';
                    echo isset($_POST[$fieldName]) ? $_POST[$fieldName] : '';
                    echo '</p>';
                }
                ?>
            </div>
        </div>
    </div>
</div>
<script>
document.getElementById("myForm").addEventListener("submit", function(event) {
    var formData = new FormData(this);
    var allFieldsFilled = true;

    // Check if all fields are filled
    formData.forEach(function(value) {
        if (value === "") {
            allFieldsFilled = false;
        }
    });

    // If all fields are filled, show the submitted data
    if (allFieldsFilled) {
        var submittedDataDiv = document.querySelector(".submitted-data");
        submittedDataDiv.style.display = "block";
    } else {
        // Prevent form submission if not all fields are filled
        event.preventDefault();
        alert("Please fill in all fields.");
    }
});
</script>
</body>
</html>
