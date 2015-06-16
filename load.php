<?php
header('Content-Type: application/json');
header('Cache-Control: private, no-store, no-cache, must-revalidate');
header('Pragma: no-cache');

$name = trim($_REQUEST['name']);
if ($name == '') $name = "default";
$name = basename($name);

readfile("recording/$name");
?>
