# log-check

A small Python script that reads a log file and counts lines
with `ERROR` and `WARNING` levels.

## Usage

```bash
python3 log_check.py <logfile>
```

Example:

```bash
python3 log_check.py sample.log
```

Output:

```
ERROR lines: 2
WARNING lines: 1
```

## Exit codes

- `0` - the file was read successfully
- `1` - wrong arguments or the file was not found

## Files

- `log_check.py` - the script
- `sample.log` - example log file for testing

## Requirements

Python 3, no external libraries.
