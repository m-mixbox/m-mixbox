<?php
function getAddress($latitude, $longitude) {
    // URL to the OpenStreetMap Nominatim API
    $url = "https://nominatim.openstreetmap.org/reverse?format=json&lat={$latitude}&lon={$longitude}&addressdetails=1";

    // Initialize cURL session
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

    // Execute cURL session and fetch data
    $response = curl_exec($ch);

    // Close cURL session
    curl_close($ch);

    // Decode JSON response
    $data = json_decode($response, true);

    // Check if the response contains an address
    if (isset($data['address'])) {
        // Construct the address from the address details
        $address = "";
        if (isset($data['address']['road'])) $address .= $data['address']['road'] . ", ";
        if (isset($data['address']['city'])) $address .= $data['address']['city'] . ", ";
        if (isset($data['address']['state'])) $address .= $data['address']['state'] . ", ";
        if (isset($data['address']['country'])) $address .= $data['address']['country'];
        return $address;
    } else {
        return "No address found.";
    }
}

// Example usage
$latitude = 23.3472;
$longitude = 85.3245952;

$address = getAddress($latitude, $longitude);
echo "The address is: " . $address;
?>
