<?php

    // advent of code day 1

    // read input
    $data = file('../inputs/day1.txt');

    // set inital values
    $elf_calories = 0; # calory count for current elf
    $calories_list = array(); # the calories_list to be returned

    foreach($data as $calories){
        if(ctype_space($calories)){
            $calories_list[] = $elf_calories;
            $elf_calories = 0;
        }
        $elf_calories += intval($calories);
    }

    // solution part one
    $solution_part_one = max($calories_list); # 70374

    // solution part two
    arsort($calories_list);
    $top3 = array_slice($calories_list, 0, 3, true);
    $solution_part_two = array_sum($top3); # 204610

?>
