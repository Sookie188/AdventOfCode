<?php
$input = file("day2.txt");

$test = file("test.txt");

$i = 0;

foreach ($input as $value) {
    $pattern = "[\s]";

    $check = preg_split($pattern, $value, -1, PREG_SPLIT_NO_EMPTY);

    $contains = explode('-', $check[0], 2);
    $first = intval($contains[0] - 1);
    $second = intval($contains[1] - 1);

    $letterDots = explode(':', $check[1], 1);
    $letter = str_replace(':', '', $letterDots);

    $pw = str_split($check[2]);

    if ((strcmp($pw[$first], $letter[0]) == 0 && strcmp($pw[$second], $letter[0]) !== 0) ||
        (strcmp($pw[$first], $letter[0]) !== 0 && strcmp($pw[$second], $letter[0]) == 0)) {
        $i++;
    }
}

print($i);