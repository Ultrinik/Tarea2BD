<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id'])){
    $sesionActiva = 1;
    $admin = $_SESSION['administrador'];
}
else{
    $sesionActiva = 0;
    $admin = 0;
 }
?>