<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

$nombre = filter_var($_SESSION["usuario"], FILTER_SANITIZE_STRING);
$correo = filter_var($_SESSION["correo"], FILTER_SANITIZE_STRING);

$paisId = filter_var($_SESSION["pais"], FILTER_SANITIZE_STRING);
$sql = 'SELECT nombre FROM pais WHERE cod_pais = $1';
$result = pg_query_params($dbconn, $sql, array($paisId));
$row = pg_fetch_row($result);
$pais = $row[0];

$fecha_registro = filter_var($_SESSION["fecha_registro"], FILTER_SANITIZE_STRING);

pg_close($dbconn);
?>