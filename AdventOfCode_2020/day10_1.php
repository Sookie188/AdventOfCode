<?php
include_once "functions.php";

//$input = file("test.txt");

$input = file("day10.txt");

$input = trimInput($input);
sort($input);

$diff1 = 0;
$diff3 = 1;

$prev = 0;
foreach ($input as $adapter) {
    $cookie = $adapter - $prev;
    if ($cookie == 1) {
        $diff1++;
    } elseif ($cookie == 3) {
        $diff3++;
    }
    $prev = $adapter;
}

echo 'Stapel mit 1: ' . $diff1 . "\r\n";
echo 'Stapel mit 3: ' . $diff3 . "\r\n";
echo 'Result: ' . $diff1 * $diff3;