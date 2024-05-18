<?php 
//take response and add it to json
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get existing JSON data
    $existing_data = file_get_contents('existing_data.json');
    
    // Convert existing JSON data to an associative array
    $users = json_decode($existing_data, true);
    
    // Create an empty array to store new user data
    $new_user = array();
    
    // Loop through each form field and add it to the new user array
    foreach ($_POST as $key => $value) {
        $new_user[$key] = $value;
    }
    
    // Add new user data to the users array
    $users[] = $new_user;
    
    // Convert users array to JSON
    $json_data = json_encode($users, JSON_PRETTY_PRINT);
    
    // Write JSON data back to the file
    file_put_contents('existing_data.json', $json_data);
    
    // Display success message
    echo "Form data has been added to existing_data.json";
} else {
    // Display error message if form is not submitted
    echo "Form not submitted!";
}
?>