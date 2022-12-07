<?php
$test = file_get_contents("test.txt");
$input = file_get_contents("day6.txt");

$answers = explode(PHP_EOL . PHP_EOL, $input);

$data[] = array();
$valid = 0;

for ($i = 0; $i < count($answers); $i++) {
    $rows[$i] = preg_split('/[\s]+/', $answers[$i]);

    $isteigentlichegal = [];
    for ($j = 0; $j < count($rows[$i]); $j++) {
        $isteigentlichegal[$j] = str_split($rows[$i][$j]);

    }
    $data[$i] = $isteigentlichegal;
}

$finalResult = 0;
$result = 0;

for ($x = 0; $x < count($data); $x++) {

    if (count($data[$x]) < 2) {
        $finalResult += count($data[$x][0]);
    } else {
        $result = call_user_func_array('array_intersect', $data[$x]);

        $finalResult += count($result);
    }
}

echo 'Das Ergebnis ist vielleicht: ' . $finalResult;
