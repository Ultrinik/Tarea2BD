<?php session_start();?>
<?php include '../include/navbar.html'; ?>
    <div class='container-fluid'>
        <div class="row p-3">
            <h1>Mi Perfil</h1>
        </div>
        <div class="row p-3">
            <div class="col">
                <!-- Mostrar aquí los datos del usuario de la sesión -->
                <div class="container shadow-lg rounded m-auto p-5">
                    <p>Nombre Completo: <?= $_SESSION["usuario"] ?></p>
                    <p>Correo: <?= $_SESSION["email"] ?></p>
                    <p>País: <?= $_SESSION["pais"] ?></p>
                    <p>Fecha de Ingreso: <?= $_SESSION["fecha_ingreso"] ?></p>
                </div>
            </div>
        </div>
    </div>
</body>

</html>