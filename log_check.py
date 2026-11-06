import sys


def count_levels(path):
    count = 0
    countW = 0
    with open(path) as f:
        for line in f:
            if "ERROR" in line:
                count += 1
            elif "WARNING" in line:
                countW += 1
    return count, countW


if len(sys.argv) != 2:
    print("Usage: python3 log_check.py <logfile>")
    sys.exit(1)

try:
    errors, warnings = count_levels(sys.argv[1])
except FileNotFoundError:
    print("File not found:", sys.argv[1])
    sys.exit(1)

print("ERROR lines:", errors)
print("WARNING lines:", warnings)
