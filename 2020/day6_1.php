<?php
$test = file_get_contents("test.txt");
$input = file_get_contents("day6.txt");

$answers = explode(PHP_EOL . PHP_EOL, $input);

$data[] = array();
$valid = 0;
$result = 0;

for ($i = 0; $i < count($answers); $i++) {
    $rows[$i] = preg_split('/[\s]+/', $answers[$i]);

    $lost[$i] = implode($rows[$i]);
    $help[$i] = str_split($lost[$i]);
    $moreHelp[$i] = array_unique($help[$i]);
    $result += count($moreHelp[$i]);
}


echo 'Das Ergebnis ist vielleicht: ' . $result;