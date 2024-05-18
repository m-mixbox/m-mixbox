<?php
require_once 'config.php';

if (!is_logged_in()) {
    header("Location: login.php");
    exit();
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h2>Welcome, <?php echo $_SESSION['username']; ?></h2>
    <p>This is your dashboard. You are logged in!</p>
    <a href="logout.php">Logout</a>
</body>
</html>
?>
