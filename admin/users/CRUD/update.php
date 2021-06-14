<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST" & $_SESSION['administrador'] == 't') {
    $sesionActiva = 1;

    $nombre = filter_var($_POST["nombre"], FILTER_SANITIZE_STRING);
    $apellido = filter_var($_POST["apellido"], FILTER_SANITIZE_STRING);
    $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
    $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
    $pais = filter_var($_POST["pais"], FILTER_SANITIZE_STRING);
    
    $opciones = array('cost'=>12);
    $contrasena_hasheada = password_hash($contrasena, PASSWORD_BCRYPT, $opciones);

    $sql = "UPDATE usuario SET nombre = $1, apellido = $2, correo = $3, contraseña = $4, pais = $5 WHERE id = $6";
	
    if(pg_query_params($dbconn, $sql, array($nombre, $apellido, $correo, $contrasena, $pais, $_SESSION['view_id'])) !== FALSE){
        echo '<script language="javascript">';
        echo 'alert ("\nUsuario modificado con éxito.")';
        echo '</script>';
        header('Location: '.'/admin/users/all.html');
    } else {
        echo '<script language="javascript">';
        echo 'alert ("\nHa ocurrido un error.")';
        echo '</script>';
        header('Location: '.'/admin/users/all.html');
    }
    
}
?>