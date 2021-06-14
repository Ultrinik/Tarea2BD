<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';
session_start();
if(isset($_SESSION['id']) & $_SESSION['administrador'] == 't'){
    $sesionActiva = 1;

    $view_id = filter_var($_GET["id"], FILTER_SANITIZE_STRING);
    $sql = 'DELETE FROM cuenta_bancaria WHERE id_usuario = $1';
    pg_query_params($dbconn, $sql, array($view_id));
    $sql = 'DELETE FROM usuario_tiene_moneda WHERE id_usuario = $1';
    pg_query_params($dbconn, $sql, array($view_id));
    
    $sql = 'DELETE FROM usuario WHERE id = $1';
    pg_query_params($dbconn, $sql, array($view_id));
    
    
    
    header('Location: '.'/admin/users/all.html');
    
    pg_close($dbconn);

}
else{
    $sesionActiva = 0;
}

?>