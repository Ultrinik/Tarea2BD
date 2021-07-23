<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id'])){
    $sesionActiva = 1;
    $admin = $_SESSION['administrador'];

    if(isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on')   
         $url = "https://";   
    else  
         $url = "http://";
    $url.= $_SERVER['HTTP_HOST'];   
    $url.= $_SERVER['REQUEST_URI'];    
}
else{
    $sesionActiva = 0;
    $admin = 0;
 }
?>