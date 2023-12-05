def parse_input(input_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    lines_iter = iter(lines)

    # Parse the seeds
    seeds = set(map(int, next(lines_iter).split(':')[1].split()))

    # Parse the mappings
    mappings = []
    mapping = {}
    for line in lines_iter:
        if ':' in line:
            if mapping:
                mappings.append(mapping)
                mapping = {}
        else:
            start_value, start_key, length = map(int, line.split())
            keys = range(start_key, start_key + length)
            values = range(start_value, start_value + length)
            mapping.update(zip(keys, values))
    mappings.append(mapping)  # Append the last mapping

    return seeds, mappings

def walk_through_mappings(seeds, mappings):
    locations = set()
    for seed in seeds:
        location = seed
        for mapping in mappings:
            location = mapping.get(location, location)
        locations.add(location)
    return locations

def main(input_file):
    seeds, mappings = parse_input(input_file)
    locations = walk_through_mappings(seeds, mappings)
    print(min(locations))

import sys

if __name__ == "__main__":
    main(sys.argv[1])