<?php 

if ($_SERVER['REQUEST_METHOD'] === 'POST') { 

    if($_POST['_method'] === 'PUT'){

        $fecha_url = $_POST['fecha_url'];

        $fecha = $_POST['fecha'];
        $hora = $_POST['hora'];
        $datetime = $fecha . ' ' . $hora;

        $valor = $_POST['valor'];
        $id = $_POST['id'];
        
        $url = 'http://127.0.0.1:5000/api/precio_moneda/'.$id.'/'.$fecha_url;

        $ch = curl_init($url);

        $data = array('id_moneda'=>$id, 'valor'=>$valor, 'fecha'=>$datetime);
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

        $id_moneda = filter_var($_POST["id_moneda"], FILTER_SANITIZE_STRING);
        $valor = filter_var($_POST["valor"], FILTER_SANITIZE_STRING);
        $fecha = filter_var($_POST["fecha"], FILTER_SANITIZE_STRING);
        $hora = filter_var($_POST["hora"], FILTER_SANITIZE_STRING);
        $date = $fecha . ' ' . $hora;
        

        $url = 'http://127.0.0.1:5000/api/precio_moneda/';
        $ch = curl_init($url);

        $data = array('id_moneda'=>$id_moneda, 'valor'=>$valor, 'fecha'=>$date);
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
    $fecha = str_replace(' ', '_', $_GET['fecha']);

    $url = 'http://127.0.0.1:5000/api/precio_moneda/'.$id.'/'.$fecha;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

}

header('Location: '.'/extras/CRUD/all_precio_moneda.html');
?>