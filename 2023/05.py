with open("AdventOfCode_2023/input/05.txt") as fp:
    input_lines = fp.readlines()


def parse_maps(input_lines):
    maps = {}
    current_map = None
    seeds = []

    for line in input_lines:
        line = line.strip()
        if 'seeds:' in line:
            numbers = ''.join(char if char.isdigit() or char.isspace() else ' ' for char in line)
            seeds = [int(number) for number in numbers.split() if number]
        if line.endswith("map:"):
            current_map = line[:-1]
            maps[current_map] = []
        elif current_map is not None and line:
            maps[current_map].append(list(map(int, line.split())))
    
    return seeds, maps

def convert_seed_to_location(seed, maps):
    
    seed_to_soil_map = maps["seed-to-soil map"]
    soil_to_fertilizer_map = maps["soil-to-fertilizer map"]
    fertilizer_to_water_map = maps["fertilizer-to-water map"]
    water_to_light_map = maps["water-to-light map"]
    light_to_temp_map = maps["light-to-temperature map"]
    temp_to_humidity_map = maps["temperature-to-humidity map"]
    humidity_to_location_map = maps["humidity-to-location map"]

    soil = seed
    for dest_start, source_start, length in seed_to_soil_map:
        if source_start <= soil < source_start + length:
            soil = dest_start + (soil - source_start)
            break

    fertilizer = soil
    for dest_start, source_start, length in soil_to_fertilizer_map:
        if source_start <= fertilizer < source_start + length:
            fertilizer = dest_start + (fertilizer - source_start)
            break

    water = fertilizer
    for dest_start, source_start, length in fertilizer_to_water_map:
        if source_start <= water < source_start + length:
            water = dest_start + (water - source_start)
            break

    light = water
    for dest_start, source_start, length in water_to_light_map:
        if source_start <= light < source_start + length:
            light = dest_start + (light - source_start)
            break

    temperature = light
    for dest_start, source_start, length in light_to_temp_map:
        if source_start <= temperature < source_start + length:
            temperature = dest_start + (temperature - source_start)
            break

    humidity = temperature
    for dest_start, source_start, length in temp_to_humidity_map:
        if source_start <= humidity < source_start + length:
            humidity = dest_start + (humidity - source_start)
            break

    location = humidity
    for dest_start, source_start, length in humidity_to_location_map:
        if source_start <= location < source_start + length:
            location = dest_start + (location - source_start)
            break

    return location

def part1(input_lines):
    seeds, maps = parse_maps(input_lines)
    lowest_location = min(convert_seed_to_location(seed, maps) for seed in seeds)
    
    print(lowest_location)    
    

def part2(input_lines):
    seeds, maps = parse_maps(input_lines)
    seeds_full = []
    for i in range(0, len(seeds)-1, 2): 
        seeds_full.extend(list(range(seeds[i], seeds[i] + seeds[i+1])))

    lowest_location = min(convert_seed_to_location(seed, maps) for seed in seeds_full)
    
    print(lowest_location)   

print("Ergebnis Part1: ")
part1(input_lines)

print("Ergebnis Part2: ")
part2(input_lines)
