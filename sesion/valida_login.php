<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
    $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
    $sql = 'SELECT * FROM usuario WHERE correo = $1';
    $result = pg_query_params($dbconn, $sql, array($correo));
    $row = pg_fetch_assoc($result);
	
    if(pg_num_rows($result) != 0){
        if(password_verify($contrasena, $row['contraseña'])){

            session_start();
            $_SESSION["usuario"] = $row['nombre'] . ' ' . $row['apellido'];
            $_SESSION["id"] = $row['id'];
            $_SESSION["correo"]= $row['correo'];
            $_SESSION["pais"]= $row['pais'];
            $_SESSION["fecha_registro"]= $row['fecha_registro'];
            $_SESSION["administrador"] = $row['administrador'];
            pg_close($dbconn);
        
        
            header('Location: '.'/user/profile.html');
            exit();

        } else {
            echo '<script language="javascript">';
            echo 'alert ("\nCorreo o ontraseña incorrecto/s.")';
            echo '</script>';
            header('Location: '.'/sesion/log-in.html');
            pg_close($dbconn);
        }
        
    } else {
        echo '<script language="javascript">';
        echo 'alert ("\nCorreo o ontraseña incorrecto/s.")';
        echo '</script>';
        header('Location: '.'/sesion/log-in.html');
        pg_close($dbconn);
    }
    
}
?>
