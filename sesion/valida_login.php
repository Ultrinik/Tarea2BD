<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $correo = $_POST["correo"];
    $contrasena = $_POST["contraseña"];
    $sql = 'SELECT * FROM usuario WHERE correo = $1';
    $result = pg_query_params($dbconn, $sql, array($correo));
	
    while($row = pg_fetch_assoc($result)) {
        if(password_verify($contrasena, $row['contraseña'])){
        #if($contrasena == $row['contraseña']){

            session_start();
            $_SESSION["usuario"] = $row['nombre'] . ' ' . $row['apellido'];
            $_SESSION["correo"]= $row['correo'];
            $_SESSION["pais"]= $row['pais'];
            $_SESSION["fecha_registro"]= $row['fecha_registro'];
            pg_close($dbconn);
    

            header('Location: '.'/user/profile.html');
            exit();
            
            
        } else {
            echo "<br> Contraseña incorrecta";
            pg_close($dbconn);
        }

    }
    
}
?>