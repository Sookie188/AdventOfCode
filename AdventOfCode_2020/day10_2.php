<?php
include_once "functions.php";

$input = file("test.txt");

//$input = file("day10.txt");

$input = trimInput($input);
sort($input);

$jolts = max($input) + 3;

$diff1 = 0;
$diff3 = 1;

$prev = 0;

function doJoltMath($input)
{
    $joltDiff = 3;
    foreach ($input as $adapter) {
        $cookie = $adapter - $prev;
        if ($cookie == 1) {
            $diff1++;
            $joltDiff++;
        } elseif ($cookie == 3) {
            $diff3++;
            $joltDiff += 3;
        } elseif ($cookie == 2) {
            $joltDiff += 2;
        }
        $prev = $adapter;
    }
    return $joltDiff;
}

function getDistanceBetweenNodes($curNode, $nextNode)
{
    return $nextNode - $curNode;
}

echo getDistanceBetweenNodes(5, 8);

function findPaths($curNode, $dist, $input)
{
    $curPath = array();
    $dest = max($input);
    $maxlen = 18;
    $pathlen = 0;

    if ($curNode != $dest) {
        if (!in_array($curNode, $curPath)) {
            if (getDistanceBetweenNodes($curNode, $curNode + 1) <= 3) {
                $pathlen += getDistanceBetweenNodes($curNode, $curNode + 1);
                if ($pathlen > $maxlen) {
                    return $curPath;
                }
                $curPath[] = $curNode;
            }
        }
    }
//    foreach ()
//        for nextNode, edgeDist adjacent to curNode:
//    findPaths(nextNode, dist + edgeDist)
//    remove last element of curpath
}

//echo 'Jolts: ' . $jolts . "\r\n";
echo 'Joltdiff: ' . doJoltMath($input) . "\r\n";

