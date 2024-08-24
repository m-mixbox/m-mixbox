<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the 'audio' file field is set and there's no upload error
    if (isset($_FILES['audio']) && $_FILES['audio']['error'] === UPLOAD_ERR_OK) {
        // Define the upload directory
        $uploadDir = 'uploads/';
        $uploadFile = $uploadDir . basename($_FILES['audio']['name']);

        // Create the upload directory if it doesn't exist
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0777, true);
        }

        // Move the uploaded file to the target directory
        if (move_uploaded_file($_FILES['audio']['tmp_name'], $uploadFile)) {
            echo json_encode(['message' => 'File successfully uploaded.', 'filename' => $uploadFile]);
        } else {
            http_response_code(500);
            echo json_encode(['message' => 'File upload failed.']);
        }
    } else {
        http_response_code(400);
        echo json_encode(['message' => 'No file uploaded or file upload error.']);
    }
} else {
    http_response_code(405);
    echo json_encode(['message' => 'Invalid request method.']);
}
?>
