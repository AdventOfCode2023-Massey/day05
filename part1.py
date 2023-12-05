# Advent of Code 2023 Day 5 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

def map_number(num, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= num < src_start + length:
            return dest_start + (num - src_start)
    return num

def solve(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    locations = []
    for seed in seeds:
        soil = map_number(seed, seed_to_soil)
        fertilizer = map_number(soil, soil_to_fertilizer)
        water = map_number(fertilizer, fertilizer_to_water)
        light = map_number(water, water_to_light)
        temperature = map_number(light, light_to_temperature)
        humidity = map_number(temperature, temperature_to_humidity)
        location = map_number(humidity, humidity_to_location)
        locations.append(location)
    return min(locations)

def main(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    lines_iter = iter(lines)

    # Discard the seeds label line and parse the seeds
    next(lines_iter)
    seeds = list(map(int, next(lines_iter).split(':')[1].split()))
    mappings = []
    mapping = []
    while True:
        try:
            # Discard the label line
            next(lines_iter)
            # If there's a previous mapping, append it to mappings
            if mapping:
                mappings.append(mapping)
                mapping = []
            # Collect lines for the current mapping until an empty line or end of file
            while (line := next(lines_iter)) and ':' not in line:
                mapping.append(tuple(map(int, line.split())))
        except StopIteration:
            # Append the last mapping
            mappings.append(mapping)
            break

    print(solve(seeds, *mappings))


import sys

if __name__ == "__main__":
    main(sys.argv[1])