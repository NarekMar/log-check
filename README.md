# Log-check

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
- `Dockerfile` - builds a container image with the script

## Requirements

Python 3, no external libraries.



## Docker

Build the image:

```bash
docker build -t log-check .
```

Run with the bundled `sample.log`:

```bash
docker run --rm log-check
```

Run with your own log file from the current folder:

```bash
docker run --rm -v $(pwd):/data log-check /data/yourfile.log
```

The `-v` flag mounts the current folder into the container as `/data`,
so the script reads the real file instead of the copy baked into the image.
