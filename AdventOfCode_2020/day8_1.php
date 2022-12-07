<?php
include("functions.php");
$input = file("day8.txt");

//$input = file("test.txt");
$input = trimInput($input);
$input = splitInputByPattern($input, ' ');

//var_dump($input);

$accumulator = 0;
$row = 0;

$rowsVisited = array();
while ($row < count($input)) {
    if (in_array($row, $rowsVisited)) {
        break;
    }
    $rowsVisited[] = $row;
    $current = $input[$row];
    switch ($current[0]) {
        case 'nop':
            $row++;
            break;
        case 'acc':
            $accumulator += $current[1];
            $row++;
            break;
        case 'jmp':
            $row += $current[1];
            break;
        default:
            print_r('ERROR');
    }
}
echo 'Schleife ist vorbei: ' . $accumulator;