<?php

function trimInput($input): array
{
    $trimmed = array();
    for ($i = 0; $i < count($input); $i++) {
        $trimmed[$i] = trim($input[$i]);
    }
    return $trimmed;
}

function splitInputByPattern($input, $pattern): array
{
    $split = array();
    for ($i = 0; $i < count($input); $i++) {
        $split[$i] = explode($pattern, $input[$i]);
    }
    return $split;
}

function splitEverything($input)
{
    $splitEv = array();
    foreach ($input as $row) {
        $splitEv[] = str_split($row);
    }
    return $splitEv;
}