<?php session_start();
include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

$nombre = $_SESSION["usuario"];
$correo = $_SESSION["correo"];

$paisId = $_SESSION["pais"];
$sql = 'SELECT nombre FROM pais WHERE cod_pais = $1';
$result = pg_query_params($dbconn, $sql, array($paisId));
$row = pg_fetch_row($result);
$pais = $row[0];

$fecha_registro = $_SESSION["fecha_registro"];
?>