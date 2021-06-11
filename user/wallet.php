<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php';

if(isset($_SESSION['id'])){
    $sesionActiva = 1;

    $sql = '
    SELECT
        moneda.sigla as codigo, moneda.nombre as nombre, usuario_tiene_moneda.balance as balance,
        precio_moneda.valor as valor, usuario_tiene_moneda.balance*precio_moneda.valor as total
    FROM
        moneda, usuario_tiene_moneda, precio_moneda
    WHERE
        usuario_tiene_moneda.id_usuario = $1 AND
        usuario_tiene_moneda.id_moneda = moneda.id AND
        precio_moneda.fecha = (
            SELECT
                MAX(precio_moneda.fecha)
            FROM
                precio_moneda
            WHERE
                moneda.id = precio_moneda.id_moneda
        )
    ';
    $result = pg_query_params($dbconn, $sql, array($_SESSION['id']));
    $num_billeteras = pg_num_rows($result);

    pg_close($dbconn);
}
else{
    $sesionActiva = 0;
 }
?>