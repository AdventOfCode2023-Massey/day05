# Advent of Code 2023 Day 5 Part 2
# Code by Github Copilot Chat
# Editing by Bart Massey

def parse_input(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    lines_iter = iter(lines)

    # Parse the seeds
    seeds_line = next(lines_iter).split(':')[1].split()
    seeds = []
    for i in range(0, len(seeds_line), 2):
        start_seed = int(seeds_line[i])
        length = int(seeds_line[i+1])
        seeds.append((start_seed, length))

    # Parse the mappings
    mappings = []
    mapping = []
    for line in lines_iter:
        if ':' in line:
            if mapping:
                mappings.append(mapping)
                mapping = []
        else:
            start_value, start_key, length = map(int, line.split())
            mapping.append((start_value, start_key, length))
    mappings.append(mapping)  # Append the last mapping

    return seeds, mappings

def walk_through_mappings(seeds, mappings):
    all_location_ranges = []
    for start_seed, length in seeds:
        location_ranges = [(start_seed, start_seed + length)]
        for mapping in mappings:
            new_location_ranges = []
            for start_location, end_location in location_ranges:
                for start_key, start_value, map_length in mapping:
                    if start_key <= start_location < start_key + map_length:
                        new_start_location = start_value + (start_location - start_key)
                        new_end_location = min(start_value + map_length, end_location)
                        new_location_ranges.append((new_start_location, new_end_location))
                        if new_end_location < end_location:
                            start_location = new_end_location
                        else:
                            break
                    elif start_location < start_key:
                        break
                else:
                    new_location_ranges.append((start_location, end_location))
            location_ranges = new_location_ranges
        all_location_ranges.extend(location_ranges)
    return min(start for start, end in all_location_ranges)

def main(input_file):
    seeds, mappings = parse_input(input_file)
    locations = walk_through_mappings(seeds, mappings)
    print(min(locations))

import sys

if __name__ == "__main__":
    main(sys.argv[1])
