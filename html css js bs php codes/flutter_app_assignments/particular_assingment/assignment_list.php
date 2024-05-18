<?php

// Read the JSON data from the file
$json_data = file_get_contents('existing_data.json');

// Decode the JSON data into an associative array
$data = json_decode($json_data, true);

// Initialize an array to store extracted data
$users_info = array();

// Iterate through each user's data
foreach ($data['ageas_federal'] as $user) {
    // Extract name and address
    $name = isset($user['l_name']) ? $user['l_name'] : "";
    $address = isset($user['house_type']) ? $user['house_type'] : "";

    // Create an array with name and address
    $user_info = array(
        "name" => $name,
        "address" => $address
    );

    // Add user's info to the array
    $users_info[] = $user_info;
}

// Encode the extracted data to JSON
$json_response = json_encode($users_info, JSON_PRETTY_PRINT);

// Set the content type to JSON
header('Content-Type: application/json');

// Send the JSON response to the client
echo $json_response;

?>
