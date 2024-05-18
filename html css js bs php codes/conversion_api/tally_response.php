
<?php

// API endpoint to upload the file
$apiEndpoint = 'http://127.0.0.1:8000/upload/excel';

// Check if a file was uploaded
if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
    
    // File details
    $fileName = $_FILES['file']['name'];
    $fileTmpName = $_FILES['file']['tmp_name'];
    
    // Check file size (max 5MB)
    if ($_FILES['file']['size'] > 5 * 1024 * 1024) {
        echo "Error: File size exceeds the limit (5MB).";
        exit;
    }
    
    // Check file type (assuming Excel files are of MIME type 'application/vnd.ms-excel' or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    $allowedTypes = ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'];
    if (!in_array($_FILES['file']['type'], $allowedTypes)) {
        echo "Error: Unsupported file type.";
        exit;
    }
    
    $uploadDirectory = 'uploads/';
    
    // Ensure the upload directory exists
    if (!file_exists($uploadDirectory)) {
        mkdir($uploadDirectory, 0777, true);
    }
    
    // Move the uploaded file to the upload directory
    $destinationPath = $uploadDirectory . $fileName;
    if (!move_uploaded_file($fileTmpName, $destinationPath)) {
        echo "Error: Failed to move uploaded file.";
        exit;
    }
    $fileUrl = __DIR__.$fileName;
    // Initialize cURL
    $curl = curl_init();
    
    // Set cURL options
    curl_setopt_array($curl, [
        CURLOPT_URL => $apiEndpoint,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => http_build_query(['file_url' => $fileUrl]),
        CURLOPT_FOLLOWLOCATION => true, // Follow redirects
        CURLOPT_MAXREDIRS => 5 // Maximum number of redirects to follow (adjust as needed)
    ]);
    
    // Execute the cURL request
    $response = curl_exec($curl);
    
    // Check for errors
    if ($response === false) {
        echo "Error: " . curl_error($curl);
    } else {
        // Handle the API response
        // Here, assuming the API response is an XML file, you can process it as needed
        // For example, you can save it locally, parse it, or display it
        
        // Save the XML response as a file locally
        $responseFileName = 'response_' . time() . '.xml'; // You can adjust the filename as needed
        $responseFile = fopen($responseFileName, 'w');
        fwrite($responseFile, $response);
        fclose($responseFile);
        
        echo "API Response saved as: " . $responseFileName;
        
        // If you want to parse the XML response, you can use PHP's built-in SimpleXML extension
        // For example:
        // $xml = simplexml_load_string($response);
        // var_dump($xml); // Display the parsed XML structure
    }
    
    // Close cURL session
    curl_close($curl);
    
} else {
    // Handle file upload error
    if (!isset($_FILES['file'])) {
        echo "Error: No file uploaded.";
    } else {
        echo "Error: " . $_FILES['file']['error'];
    }
}
?>
