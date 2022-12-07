<?php
$test = file_get_contents("test.txt");
$input = file_get_contents("day4.txt");
$required = file("day4_required.txt");

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
    $eyecolors = array('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth');
    for ($k = 0; $k < count($required); $k++) {
        $key_found = false;
        for ($b = 0; $b < count($passport); $b++) {
            $key = array_search(trim($required[$k]), $passport[$b]);
            if ($key !== false) {
                $key_found = true;
                $value = $passport[$b][1];
                switch (str_replace("\r\n", "", $required[$k])) {
                    case "byr":
                        if (!($value >= 1920 && $value <= 2002)) {
                            return false;
                        }
                        break;
                    case "iyr":
                        if (!($value >= 2010 && $value <= 2020)) {
                            return false;
                        }
                        break;
                    case "eyr":
                        if (!($value >= 2020 && $value <= 2030)) {
                            return false;
                        }
                        break;
                    case "hgt":
                        $height = substr($value, 0, -2);
                        $unit = substr($value, -2);
                        if ($unit == 'cm') {
                            if (!($height >= 150 && $height <= 193)) {
                                return false;
                            }
                        }
                        if ($unit == 'in') {
                            if (!($height >= 59 && $height <= 76)) {
                                return false;
                            }
                        }
                        break;
                    case "hcl":
                        if (preg_match("/#[a-f0-9]{6}/", $value) === 0) {
                            return false;
                        }
                        break;
                    case "ecl":
                        if (array_search($value, $eyecolors) === false) {
                            return false;
                        }
                        break;
                    case "pid":
                        if (preg_match("/^\d{9}+$/", $value) === 0) {
                            return false;
                        }
                        break;
                    default:
                        return false;
                }
            }
        }
        if (!$key_found) {
            return false;
        }
    }
    return true;
}

$valid_passports = array();

for ($t = 0; $t < count($data); $t++) {
    if (checkPassport($data[$t], $required)) {
        $valid++;
        $valid_passports[] = $data[$t];
    }
}

echo "Habe " . $valid . " Passports gefunden";