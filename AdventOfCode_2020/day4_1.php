<?php
$test = file_get_contents("test.txt");
$input = file_get_contents("day4.txt");

$passports = explode(PHP_EOL . PHP_EOL, $input);

$data[] = array();
$valid = 0;

for ($i = 0; $i < count($passports); $i++) {
    $rows[$i] = preg_split('/[\s]+/', $passports[$i]);

    $isteigentlichegal = [];
    for ($j = 0; $j < count($rows[$i]); $j++) {
        $isteigentlichegal[$j] = explode(":", $rows[$i][$j]);
    }
    $data[$i] = $isteigentlichegal;
}

function checkPassport($passport, $required): bool
{
    for ($k = 0; $k < count($required); $k++) {
        $key_found = false;
        for ($b = 0; $b < count($passport); $b++) {
            $key = array_search(trim($required[$k]), $passport[$b]);
            if ($key !== false) {
                $key_found = true;
            }
        }
        if (!$key_found) {
            return false;
        }
    }
    return true;
}

$required = file("day4_required.txt");
for ($t = 0; $t < count($passports); $t++) {
    if (checkPassport($data[$t], $required)) {
        $valid++;
    }
}

echo $valid;