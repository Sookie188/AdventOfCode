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

$result = 0;
for ($i = $preamble; $i < count($input); $i++) {
    if (!lookAtNumbers($input, $preamble, $input[$i], $i)) {
        $result = $input[$i];
    }
}

echo "Result: " . $result;
echo "\r\n";

function findSet($needle, $numbers): array
{
    for ($i = 0; $i < count($numbers); $i++) {
        for ($j = $i + 1; $j < count($numbers); $j++) {
            $sum = sum($numbers, $i, $j);
            if ($sum == $needle) {
                return array_slice($numbers, $i, $j - $i);
            }
            if ($sum > $needle) {
                continue 2;
            }
        }
    }
    return array();
}

function sum($numbers, $start, $end): int
{
    $result = 0;
    for ($i = $start; $i < $end; $i++) {
        $result += $numbers[$i];
    }
    return $result;
}

$moreShit = findSet($result, $input);

$fuck = max($moreShit) + min($moreShit);

echo "Result Part 2: " . $fuck;