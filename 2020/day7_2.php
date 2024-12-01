<?php
$input = file("day7.txt");

//$input = file("test.txt");

$split = array();

$colours = array();

for ($i = 0; $i < count($input); $i++) {
    $input[$i] = str_replace("bags", "bag", $input[$i]);
    $split[$i] = explode(' contain ', str_replace(".", "", trim($input[$i])));

    if (strpos($split[$i][1], 'no other bag') !== false) {
        $split[$i][1] = array();
    } else {
        $split[$i][1] = explode(', ', $split[$i][1]);
        for ($j = 0; $j < count($split[$i][1]); $j++) {
            $split[$i][1][$j] = (explode(' ', $split[$i][1][$j], 2));
        }
    }
}


$helpMe = blackMagicShit($split, 'shiny gold bag', 1);
print_r($helpMe - 1);

function blackMagicShit($bunchOfBags, $bag, $number)
{
    $counter = 1;
    $bag_arr = findBagByName($bunchOfBags, $bag);
    foreach ($bag_arr[1] as $content) {
        $counter += blackMagicShit($bunchOfBags, $content[1], $content[0]);
    }
    return $counter * $number;
}

function findBagByName($bunchOfBags, $bag)
{
    foreach ($bunchOfBags as $candidate) {
        if ($candidate[0] === $bag) {
            return $candidate;
        }
    }
    return null;
}