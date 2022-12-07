<?php
include("functions.php");
$input = file("day9.txt");

//$input = file("test.txt");
$input = trimInput($input);

//var_dump($input);

$preamble = 25;

function lookAtNumbers($numbers, $preamble, $current, $index)
{
    for ($i = $index - $preamble; $i < $index; $i++) {
        for ($j = $i + 1; $j < $index; $j++) {
            $result = $numbers[$i] + $numbers[$j];
            if ($result == $current) {
                return true;
            }
        }
    }
    return false;
}

for ($i = $preamble; $i < count($input); $i++) {
    if (!lookAtNumbers($input, $preamble, $input[$i], $i)) {
        echo "Result: " . $input[$i];
    }
}
