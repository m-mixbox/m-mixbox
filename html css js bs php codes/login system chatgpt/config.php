<?php
session_start();

// Change these to your database credentials
$db_host = 'localhost';
$db_username = 'your_username';
$db_password = 'your_password';
$db_name = 'your_database';

// Connect to the database
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Function to hash passwords
function hash_password($password) {
    return password_hash($password, PASSWORD_DEFAULT);
}

// Function to verify password
function verify_password($password, $hashed_password) {
    return password_verify($password, $hashed_password);
}

// Function to validate login credentials
function validate_login($username, $password, $conn) {
    $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows == 1) {
        $stmt->bind_result($id, $db_username, $db_password);
        $stmt->fetch();

        if (verify_password($password, $db_password)) {
            $_SESSION['user_id'] = $id;
            $_SESSION['username'] = $db_username;
            return true;
        } else {
            return false; // Incorrect password
        }
    } else {
        return false; // User not found
    }

    $stmt->close();
}

// Function to check if user is logged in
function is_logged_in() {
    return isset($_SESSION['user_id']);
}

// Function to log out user
function logout() {
    session_destroy();
    header("Location: login.php");
    exit();
}

?>
