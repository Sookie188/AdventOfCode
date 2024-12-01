<?php
$input = file("day7.txt");

//$input = file("test.txt");

$splitted = array();

$colours = array();

for ($i = 0; $i < count($input); $i++) {
    $input[$i] = str_replace("bags", "bag", $input[$i]);
    $splitted[$i] = explode('contain', $input[$i]);

    if (containsBag(trim($splitted[$i][1]), 'shiny gold')) {
        $colours[] = trim($splitted[$i][0]);
    }
}

$diff_colours_b4 = count(array_unique($colours));
$diff_colours_af = -1;

while ($diff_colours_b4 != $diff_colours_af) {
    for ($i = 0; $i < count($splitted); $i++) {
        for ($j = 0; $j < count($colours); $j++) {
            if (containsBag(trim($splitted[$i][1]), $colours[$j])) {
                $addThis = trim($splitted[$i][0]);
                array_push($colours, $addThis);
            }
        }
    }
    $diff_colours_b4 = $diff_colours_af;
    $diff_colours_af = count(array_unique($colours));
}

function containsBag($bags, $bagColour): bool
{
    if (strpos($bags, $bagColour) !== false) {
        return true;
    }
    return false;
}

echo 'Ergebnis: ' . count(array_unique($colours));