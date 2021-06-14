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

    $sql = 'SELECT nombre, apellido, SUM(valor*balance) AS Valor_Total
    FROM(SELECT ultimo_valor.id_moneda, valor
             FROM (
            SELECT id_moneda, max(fecha)
            FROM precio_moneda
            GROUP BY id_moneda) AS ultimo_valor 
            LEFT JOIN precio_moneda ON ultimo_valor.max = precio_moneda.fecha 
            AND ultimo_valor.id_moneda = precio_moneda.id_moneda)
            AS valor_monedas
        RIGHT JOIN 
        (SELECT *
             FROM usuario_tiene_moneda LEFT JOIN usuario 
             ON usuario_tiene_moneda.id_usuario = usuario.id
             WHERE usuario.id = $1) AS moneda_usuario
        ON moneda_usuario.id_moneda = valor_monedas.id_moneda
    GROUP BY
        nombre, apellido';
    
    $result1 = pg_query_params($dbconn, $sql, array($_SESSION['id']));
    $row1 = pg_fetch_row($result1);
    pg_close($dbconn);
}
else{
    $sesionActiva = 0;
 }
?>