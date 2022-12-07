<?php
$input = file("day3.txt");

$test = file("test.txt");
$map[] = array();
$trees = 0;

function checkEquals($haystack, $needle): bool
{
    return (strcmp($haystack, $needle) == 0);
}

for ($i = 0; $i < count($input); $i++) {
    $map[$i] = str_split(trim($input[$i]));
}

$i = 1;
$k = 3;
$columns = count($map[0]);
while ($i < count($input)) {
    if (checkEquals($map[$i][($k % $columns)], '#')) {
        $trees++;
    }

    $k += 3;
    $i++;
}

print('Result: ' . $trees);