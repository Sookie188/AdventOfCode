<?php
$input = file("day2.txt");
$test = file("test.txt");

$i = 0;

foreach ($input as $value) {
    $pattern = "[\s]";

    $check = preg_split($pattern, $value, -1, PREG_SPLIT_NO_EMPTY);

    $contains = explode('-', $check[0], 2);
    $min = $contains[0];
    $max = $contains[1];

    $letterDots = explode(':', $check[1], 1);
    $letter = str_replace(':', '', $letterDots);

    $pw = explode(' ', $check[2]);

    $result = substr_count($pw[0], $letter[0]);

    if (($min <= $result) && ($result <= $max)) {
        $i++;
    }
}

print($i);