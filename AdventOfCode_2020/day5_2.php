<?php
$input = file("day5.txt");

$test = file("test.txt");

$row_arr_bin = array();
$column_arr_bin = array();

$bestIDEver = 0;
$id = 0;

foreach ($input as $value) {
    $trimed = (str_replace("\n", "", $value));
    $row = substr($trimed, 0, 7);
    $column = substr($trimed, 7, 3);
    //print_r('Value: ' . $value . ' Row: ' . $row . ' Column: ' . $column . "\r\n");

    $row_arr = str_split($row);
    $column_arr = str_split($column);

    for ($i = 0; $i <= count($row_arr); $i++) {
        if ($row_arr[$i] == 'B') {
            $row_arr_bin[$i] = 1;
        }
        if ($row_arr[$i] == 'F') {
            $row_arr_bin[$i] = 0;
        }
    }

    $backTogether_row = implode("", $row_arr_bin);
    $row_final = bindec($backTogether_row);

    for ($j = 0; $j <= count($column_arr); $j++) {
        if ($column_arr[$j] == 'R') {
            $column_arr_bin[$j] = 1;
        }
        if ($column_arr[$j] == 'L') {
            $column_arr_bin[$j] = 0;
        }
    }

    $backTogether_column = implode("", $column_arr_bin);
    $column_final = bindec($backTogether_column);

    $SeatID = $row_final * 8 + $column_final;

    if ($SeatID > $bestIDEver) {
        $bestIDEver = $SeatID;
    }

    $seat_array[$id] = $SeatID;
    $id++;
}

sort($seat_array);

$s = 0;
for ($x = 11; $x < 10000; $x++) {
    if ($x !== $seat_array[$s]) {
        echo $x . "\r\n";
        break;
    }
    $s++;
}

print_r("\r\n" . 'final high number to put into field to gain a star: ' . $bestIDEver);