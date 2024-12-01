<?php
include_once "functions.php";

$input = file("test.txt");

//$input = file("day11.txt");

$input = trimInput($input);
$input = splitEverything($input);

print_r($input);