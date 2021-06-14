<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id']) & $_SESSION['administrador'] == 't'){
    $sesionActiva = 1;

    
    $view_id = filter_var($_GET["id"], FILTER_SANITIZE_STRING);
    $sql = 'SELECT * FROM usuario WHERE id = $1';
    $result = pg_query_params($dbconn, $sql, array($view_id));
    $row = pg_fetch_row($result);
    $fecha_registro = filter_var($row[6], FILTER_SANITIZE_STRING);
    $nombre = filter_var($row[1], FILTER_SANITIZE_STRING);
    $apellido = filter_var($row[2], FILTER_SANITIZE_STRING);
    $correo = filter_var($row[3], FILTER_SANITIZE_STRING);
    
    $paisId = filter_var($row[5], FILTER_SANITIZE_STRING);
    $sql = 'SELECT nombre FROM pais WHERE cod_pais = $1';
    $result = pg_query_params($dbconn, $sql, array($paisId));
    $row = pg_fetch_row($result);
    $pais = $row[0];
    $_SESSION['view_id'] = $view_id;
    
    
    pg_close($dbconn);

}
else{
    $sesionActiva = 0;
}

?>