<?php
include_once "functions.php";

$input = file("test.txt");

$input = trimInput($input);

print_r($input);

$x = 0;
$y = 0;


foreach ($input as $instruction) {
    $direction = $instruction[0];
    $number = substr($instruction, 1);
    $face = array("north", "east", "west", "south");
    switch ($direction) {
        case "F":
            if ($face == "east") {
                $y += $number;
            } else {
                $x += $number;
            }
            break;
        case "N":
            if ($face == "east") {
                $x += $number;
            } else {
                $y += $number;
            }
            break;
        case "R":
            if ($number == "90") {
                $face = 'south';
            } elseif ($number == "180") {

            }
            break;
        case "L":
            break;
    }
}

echo "X: " . $x . "\r\n";
echo "Y: " . $y;
