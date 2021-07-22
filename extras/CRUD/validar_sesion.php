<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id'])){
    $sesionActiva = 1;
    $admin = $_SESSION['administrador'];
    $url.= $_SERVER['HTTP_HOST'];   
    
    // Append the requested resource location to the URL   
    $url.= $_SERVER['REQUEST_URI'];    
}
else{
    $sesionActiva = 0;
    $admin = 0;
 }
?>