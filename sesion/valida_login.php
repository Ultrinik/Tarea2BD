<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $correo = filter_var($_POST["correo"], FILTER_SANITIZE_STRING);
    $contrasena = filter_var($_POST["contraseña"], FILTER_SANITIZE_STRING);
    $sql = 'SELECT * FROM usuario WHERE correo = $1';
    $result = pg_query_params($dbconn, $sql, array($correo));
    $row = pg_fetch_assoc($result);
	
    #if(password_verify($contrasena, $row['contraseña'])){
    if($contrasena == $row['contraseña']){

        session_start();
        $_SESSION["usuario"] = $row['nombre'] . ' ' . $row['apellido'];
        $_SESSION["id"] = $row['id'];
        $_SESSION["correo"]= $row['correo'];
        $_SESSION["pais"]= $row['pais'];
        $_SESSION["fecha_registro"]= $row['fecha_registro'];
        $_SESSION["administrador"] = $row['administrador'];
        pg_close($dbconn);
	
	if($row['administrador'] == 't'){
		
		header('Location: '.'/admin/users/all.html');
               exit();
        }
        else{
		header('Location: '.'/user/profile.html');
		exit();
        }
        
        
    } else {
        echo "<br> Contraseña incorrecta";
        pg_close($dbconn);
    }
    
}
?>
