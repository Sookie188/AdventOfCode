<?php

$input = file("day1.txt");

function countFuel($mass)
{
    if ($mass <= 5) {
        return 0;
    }
    $fuel = floor($mass / 3) - 2;
    return $fuel + countFuel($fuel);
}

$fuel = 0;
for ($i = 0; $i < count($input); $i++) {

    $fuel += countFuel($input[$i]);
}

echo $fuel;
