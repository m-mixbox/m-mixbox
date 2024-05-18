<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $temp_data = array();
    $data = array();

    // Loop through all form fields
    foreach ($_POST as $key => $value) {
        // Skip submit button
        if ($key != "submit") {
            // Store field and its value in data array
            $temp_data[$key] = $value;
        }
    }
    $data[] = $temp_data;

    // Convert data to JSON
    $json_data = json_encode($data, JSON_PRETTY_PRINT);

    // Save JSON data to a file
    $file = 'data.json';
    if (file_exists($file)) {
        $existing_data = file_get_contents($file);
        $existing_data = json_decode($existing_data, true); // Decode JSON to associative array
    } else {
        $existing_data = array(); // If file doesn't exist, initialize with empty array
    }

    // Merge new data with existing data
    $merged_data = array_merge($existing_data, $data);

    // Convert merged data to JSON
    $json_data = json_encode($merged_data, JSON_PRETTY_PRINT);

    // Save merged JSON data to the file
    file_put_contents($file, $json_data);
    echo "Data saved successfully!";
} else {
    echo "Form submission error!";
}
?>