<?php session_start();
include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if (isset($_SESSION['id'])) {
   $sesionActiva = 1;
   
   $sql = 'SELECT * FROM usuario_tiene_moneda WHERE id_usuario = $1';
   $billeteras = pg_query_params($dbconn, $sql, array($_SESSION['id']));
   $num_billeteras = pg_num_rows($billeteras);

   $admin = $_SESSION['administrador'];
}
else{
   $sesionActiva = 0;
   $num_billeteras = 0;
   $admin = 0;
}

?>