<?php
$numbers = file("day1.txt");

for ($i = 0; $i < count($numbers); $i++) {
    for ($j = $i + 1; $j < count($numbers); $j++) {
        for ($k = $j + 1; $k < count($numbers); $k++) {
            $check = $numbers[$i] + $numbers[$j] + $numbers[$k];
            if ($check == 2020) {
                echo $numbers[$i] * $numbers[$j] * $numbers[$k];
            }
        }
    }
}