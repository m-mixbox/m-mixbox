<?php 

    // Enable us to use Headers
    ob_start();

    // Set sessions
    if(!isset($_SESSION)) {
        session_start();
    }

    $hostname = "localhost";
    $username = "test1";
    $password = "4Mu99BhzK8dr4vF1";
    $dbname = "login_database";
    
    $connection = mysqli_connect($hostname, $username, $password, $dbname) or die("Database connection not established.")

?>