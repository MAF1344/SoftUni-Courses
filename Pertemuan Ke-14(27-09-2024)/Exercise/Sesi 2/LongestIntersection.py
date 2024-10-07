N = int(input())
all_intersections = []

for _ in range(N):
    range_str = input()

    first_range, second_range = range_str.split('-')
    first_start, first_end = map(int, first_range.split(','))
    second_start, second_end = map(int, second_range.split(','))

    intersection = list(range(max(first_start, second_start), min(first_end, second_end) + 1))
    all_intersections.append(intersection)

longest_intersection = max(all_intersections, key=len)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")