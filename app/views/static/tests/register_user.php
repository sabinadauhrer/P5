<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = array(
        "username" => $_POST["username"],
        "password" => $_POST["password"],
        "name" => $_POST["name"],
        "firstname" => $_POST["firstname"],
        "email" => $_POST["email"],
        "phone" => $_POST["phone"],
        "iban" => $_POST["iban"],
        "country" => $_POST["country"],
        "zip" => $_POST["zip"],
        "city" => $_POST["city"],
        "street" => $_POST["street"],
        "snumber" => $_POST["snumber"],
        "is_admin" => isset($_POST["is_admin"]) ? true : false
    );

    $json_data = json_encode($data);

    $ch = curl_init('http://127.0.0.1:5000/add_user');
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
        echo "Fehler bei der Registrierung.";
    }
}
?>