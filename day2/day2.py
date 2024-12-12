# Read and parse the input, skipping any empty lines
data = [[int(y) for y in line.strip().split()] 
        for line in open('input.txt') if line.strip()]

def is_safe(level, dampener_allowed=True):
    def check_sequence(seq):
        # Check if the sequence is entirely increasing or decreasing with diffs between 1 and 3
        diffs = [b - a for a, b in zip(seq, seq[1:])]
        is_increasing = all(1 <= diff <= 3 for diff in diffs)
        is_decreasing = all(-3 <= diff <= -1 for diff in diffs)
        return is_increasing or is_decreasing

    if check_sequence(level):
        return True

    if not dampener_allowed:
        return False

    # Try removing each element once to see if it makes the sequence safe
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]
        if check_sequence(modified_level):
            return True

    return False

# Part One: Without using the Problem Dampener
safe_count_part1 = sum(is_safe(report, dampener_allowed=False) for report in data)
print(f"Part One - Safe Reports: {safe_count_part1}")

# Part Two: With the Problem Dampener (allowing one removal)
safe_count_part2 = sum(is_safe(report, dampener_allowed=True) for report in data)
print(f"Part Two - Safe Reports with Dampener: {safe_count_part2}")