<?php 

if ($_SERVER['REQUEST_METHOD'] === 'POST') { 

    if($_POST['_method'] === 'PUT'){
        $sigla = $_POST['sigla'];
        $nombre = $_POST['nombre'];
        $id = $_POST['id'];
        $url = 'http://127.0.0.1:5000/api/moneda/'.$id;
        $ch = curl_init($url);

        $data = array('id'=>$id, 'sigla'=>$sigla, 'nombre'=>$nombre);
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

        $nombre = filter_var($_POST["nombre"], FILTER_SANITIZE_STRING);
        $sigla = filter_var($_POST["sigla"], FILTER_SANITIZE_STRING);
        

        $url = 'http://127.0.0.1:5000/api/moneda/';
        $ch = curl_init($url);

        $data = array('nombre'=>$nombre, 'sigla'=>$sigla);
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
    $url = 'http://127.0.0.1:5000/api/moneda/'.$id;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

}

header('Location: '.'/extras/CRUD/all_moneda.html');
?>