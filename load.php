<?php
header('Content-Type: application/json');

$name = trim($_REQUEST['name']);
if ($name == '') $name = "default";

readfile("recording/$name");
?>
