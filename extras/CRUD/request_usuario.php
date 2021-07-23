<?php 

if ($_SERVER['REQUEST_METHOD'] === 'POST') { 

    if($_POST['_method'] === 'PUT'){

        $id = $_POST['id'];
        $nombre = filter_var($_POST["nombre"], FILTER_SANITIZE_STRING);
        $apellido = filter_var($_POST["apellido"], FILTER_SANITIZE_STRING);
        $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
        $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
        $pais = filter_var($_POST["pais"], FILTER_SANITIZE_STRING);
        
        //$opciones = array('cost'=>12);
        //$contrasena_hasheada = password_hash($contrasena, PASSWORD_BCRYPT, $opciones);

        $url = 'http://127.0.0.1:5000/api/usuario/'.$id;
        $ch = curl_init($url);

        $data = array('id'=>$id, 'nombre'=>$nombre, 'apellido'=>$apellido, 'correo'=>$correo, 'contraseña'=>$contrasena, 'pais'=>$pais);
        $data_json = json_encode($data);

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_json)));
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        //Execute the request.
        $response = curl_exec($ch);
        curl_close($ch);
    } elseif ($_POST['_method'] === 'POST'){

        $nombre = filter_var($_POST["nombre"], FILTER_SANITIZE_STRING);
        $apellido = filter_var($_POST["apellido"], FILTER_SANITIZE_STRING);
        $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
        $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
        $pais = filter_var($_POST["pais"], FILTER_SANITIZE_STRING);
        
        //$opciones = array('cost'=>12);
        //$contrasena_hasheada = password_hash($contrasena, PASSWORD_BCRYPT, $opciones);

        $url = 'http://127.0.0.1:5000/api/usuario/';
        $ch = curl_init($url);

        $data = array('id'=>$id, 'nombre'=>$nombre, 'apellido'=>$apellido, 'correo'=>$correo, 'contraseña'=>$contrasena, 'pais'=>$pais);
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

    $url = 'http://127.0.0.1:5000/api/usuario/'.$id;
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

}

header('Location: '.'/extras/CRUD/all_usuario.html');
?>