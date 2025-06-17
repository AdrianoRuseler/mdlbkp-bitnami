<?php
$mysqli = new mysqli("mariadb", "myuser", "mypassword", "mydb");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
echo "Connected successfully to MariaDB!";
?>
