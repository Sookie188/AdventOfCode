<?php

$input = file("day1.txt");
$fuel = 0;

for ($i = 0; $i < count($input); $i++) {
    $fuel += floor($input[$i] / 3) - 2;
}

echo $fuel;