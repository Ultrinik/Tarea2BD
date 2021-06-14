<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	#query
    $sql = 'SELECT MAX(id) FROM usuario';
	$result = pg_query($dbconn, $sql);
    $row = pg_fetch_row($result);
    $id = $row[0] + 1;
	
    $nombre = filter_var($_POST["nombre"], FILTER_SANITIZE_STRING);
    $apellido = filter_var($_POST["apellido"], FILTER_SANITIZE_STRING);
    $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
    $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
    $pais = filter_var($_POST["pais"], FILTER_SANITIZE_STRING);
    $fecha_registro = date("Y-m-d H:i:s");
    $administrador = 0;
    #query
    $sql = 'SELECT * FROM usuario WHERE correo = $1'; 
    $result = pg_query_params($dbconn, $sql, array($correo));

    if( pg_num_rows($result) > 0 ){
        #usuario ya existe
        echo '<script language="javascript">';
        echo 'alert ("\nUsuario ya registrado.")';
        echo '</script>';
        #header('Location: '.'/sesion/sign-up.html');
    } else {
        #crear usuario
        $opciones = array('cost'=>12);
        $contrasena_hasheada = password_hash($contrasena, PASSWORD_BCRYPT, $opciones);
        $sql = 'INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, administrador) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';
        if(pg_query_params($dbconn, $sql, array($id, $nombre, $apellido, $correo, $contrasena_hasheada, $pais, $fecha_registro, $administrador)) !== FALSE){
            header('Location: '.'/extras/sing-up-succes.html');
        } else {
            echo '<script language="javascript">';
            echo 'alert ("\nHa ocurrido un error.")';
            echo '</script>';
            header('Location: '.'/sesion/sign-up.html');
        }
    }
    pg_close($dbconn);
}
?>