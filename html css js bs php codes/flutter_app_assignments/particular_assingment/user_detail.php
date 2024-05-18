<?php

// Read the JSON data from the file
$json_data = file_get_contents('data.json');

// Decode the JSON data into an associative array
$data = json_decode($json_data, true);

// Function to search for user data based on ref_no
function getUserDataByRefNo($data, $ref_no) {
    // Initialize result
    $result = array();

    // Search for the user with the matching ref_no
    foreach ($data['ageas_federal'] as $user) {
        if ($user['ref_no'] == $ref_no) {
            // Found the user, store their data
            $result = $user;
            break;
        }
    }

    return $result;
}

// Get the reference number from the query string
$ref_no = isset($_GET['ref_no']) ? $_GET['ref_no'] : "";

// If a reference number is provided
if (!empty($ref_no)) {
    // Search for the user data
    $user_data = getUserDataByRefNo($data, $ref_no);

    // If user data is found
    if (!empty($user_data)) {
        // Encode the user data into JSON
        $json_response = json_encode($user_data, JSON_PRETTY_PRINT);

        // Set the content type to JSON
        header('Content-Type: application/json');

        // Send the JSON response to the client
        echo $json_response;
    } else {
        // User not found
        echo "User with reference number '$ref_no' not found.";
    }
} else {
    // No reference number provided
    echo "Please provide a reference number.";
}

?>
