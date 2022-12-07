<?php
$numbers = file("day1.txt");

for ($i = 0; $i < count($numbers); $i++) {
    for ($j = $i + 1; $j < count($numbers); $j++) {
        $check = $numbers[$i] + $numbers[$j];
        if ($check == 2020) {
            echo $numbers[$i] * $numbers[$j];
        }
    }
}