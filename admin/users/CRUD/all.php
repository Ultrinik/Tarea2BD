<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id'])){
    $sesionActiva = 1;
    $admin = $_SESSION['administrador'];

    $sql = 'SELECT * FROM usuario';
    $result = pg_query($dbconn, $sql);

    pg_close($dbconn);
}
else{
    $sesionActiva = 0;
    $admin = 0;
 }
?>