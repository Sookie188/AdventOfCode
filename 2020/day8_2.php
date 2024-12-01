<?php
include("functions.php");
$input = file("day8.txt");

//$input = file("test.txt");
$input = trimInput($input);
$input = splitInputByPattern($input, ' ');

//var_dump($input);

function computer($input): array
{
    $row = 0;
    $accumulator = 0;
    $rowsVisited = array();
    while ($row < count($input)) {
        if (in_array($row, $rowsVisited)) {
            return array($accumulator, false);
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
    return array($accumulator, true);
}

for ($i = 0; $i < count($input); $i++) {
    if ($input[$i][0] != 'jmp') {
        continue;
    }
    $copy = $input;
    $copy[$i][0] = 'nop';
    $result = computer($copy);
    if ($result[1]) {
        print_r('Result: ' . $result[0]);
        break;
    }
}