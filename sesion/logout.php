<?php
/* Este archivo debe manejar la lógica de cerrar una sesión */
session_destroy();

header('Location: '.'/index.html');
?>