<?php 

if ($_SERVER['REQUEST_METHOD'] === 'POST') { 

    if($_POST['_method'] === 'PUT'){
        $id_usuario = $_POST['id_usuario'];
        $id_moneda = $_POST['id_moneda'];
        $id_usuario_url = $_POST['id_usuario_url'];
        $id_moneda_url = $_POST['id_moneda_url'];
        $balance = $_POST['balance'];
        $url = 'http://127.0.0.1:5000/api/usuario_tiene_moneda/'.$id_moneda_url.'/'.$id_usuario_url;
        $ch = curl_init($url);

        $data = array('id_usuario'=>$id_usuario, 'id_moneda'=>$id_moneda, 'balance'=>$balance);
        $data_json = json_encode($data);

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_json)));
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        //Execute the request.
        $response = curl_exec($ch);
        curl_close($ch);
    }  elseif ($_POST['_method'] === 'POST'){

        $id_usuario = filter_var($_POST["id_usuario"], FILTER_SANITIZE_STRING);
        $id_moneda = filter_var($_POST["id_moneda"], FILTER_SANITIZE_STRING);
        $balance = filter_var($_POST["balance"], FILTER_SANITIZE_STRING);
        

        $url = 'http://127.0.0.1:5000/api/usuario_tiene_moneda/';
        $ch = curl_init($url);

        $data = array('id_usuario'=>$id_usuario, 'id_moneda'=>$id_moneda, 'balance'=>$balance);
        $data_json = json_encode($data);

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_json)));
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
        curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($ch);
        curl_close($ch);


    }

} else{
    $ch = curl_init();
    $id = $_GET['id'];
    $id_moneda = $_GET['id_moneda'];

    $url = 'http://127.0.0.1:5000/api/usuario_tiene_moneda/'.$id.'/'.$id_moneda;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

}

header('Location: '.'/extras/CRUD/all_usuario_tiene_moneda.html');
?>