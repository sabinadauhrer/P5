<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = array(
        "username" => $_POST["username"],
        "password" => $_POST["password"]
    );

    $json_data = json_encode($data);

    $ch = curl_init('http://127.0.0.1:5000/login');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $json_data);

    $response = curl_exec($ch);
    curl_close($ch);

    $response_data = json_decode($response, true);

    if (isset($response_data['message'])) {
        echo $response_data['message'];
        if (isset($response_data['user_id'])) {
            echo " Benutzer-ID: " . $response_data['user_id'];
        }
    } else {
        echo "Fehler beim Login.";
    }
}
?>