<?php
header('Content-Type: text/plain');

$name = trim($_REQUEST['name']);
if ($name == '') $name = "default";
$name = basename($name);

$lat = trim($_REQUEST['lat']);
$lon = trim($_REQUEST['lon']);
$time = trim($_REQUEST['time']);
$alt = trim($_REQUEST['alt']);
$speed = trim($_REQUEST['speed']);

$json = <<<EOT
{
    "lat": $lat,
    "lon": $lon,
    "time": "$time",
    "alt": $alt,
    "speed": $speed
}
EOT;

$out = fopen("recording/$name", "w");
fwrite($out, $json);
fclose($out);

?>
