<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $correo = $_POST["correo"];
    $contrasena = $_POST["contraseña"];
    $sql = 'SELECT * FROM usuario WHERE correo = $1';
    $result = pg_query_params($dbconn, $sql, array($correo));
	
    if( pg_num_rows($result) == 1 ) {
        while($row = pg_fetch_assoc($result)) {
			echo $contrasena;
			echo $row['contraseña'];
            if(password_verify($contrasena, $row['contraseña'])){
			#if($contrasena == $row['contraseña']){

                session_start();
                $_SESSION["usuario"] = $row['nombre'] . ' ' . $row['apellido'];
                $_SESSION["correo"]= $row['correo'];
                $_SESSION["pais"]= $row['pais'];
                $_SESSION["fecha_ingreso"]= $row['fecha_ingreso'];
                pg_close($dbconn);
        
                if($row['administrador']){
                    header('Location: '.'/admin/users/all.html');
                    exit();
                } else {
                    header('Location: '.'/user/profile.php');
                    exit();
                }
                
                
            } else {
                echo "<br> Contraseña incorrecta";
                pg_close($dbconn);
            }

        }
    } else {
        echo "<br> Multiples instancias del correo en la DB";
    }
    
}
?>