# TimeTrack Package

## Overview

The `bennet.timetrack` package provides a simple implementation of a stopwatch for measuring elapsed time, recording laps, and splits. 

## Installation

To use the `timetrack` package, ensure the directory structure matches the following:

```
timetrack/
├── bennet/
│   └── timetrack/
│       ├── __init__.py
│       └── timetrack.py
```

Then, you can import the package in your Python code.

## Usage

### StopWatch

The `StopWatch` class allows you to start, pause, resume, stop, and reset a stopwatch, as well as record lap and split times.

#### Example

```python
from bennet.timetrack.timetrack import StopWatch

# Create a stopwatch instance
stopwatch = StopWatch()

# Start the stopwatch
stopwatch.start()

# Record a lap after some time
time.sleep(2)
stopwatch.lap()

# Pause the stopwatch
time.sleep(1)
stopwatch.pause()

# Resume the stopwatch
time.sleep(1)
stopwatch.resume()

# Record another lap
time.sleep(2)
stopwatch.lap()

# Stop the stopwatch
time.sleep(1)
elapsed_lap_time = stopwatch.get_elapsed_lap_time(formatted=True)
stopwatch.stop()

# Retrieve lap and split times
lap_times = stopwatch.lap_times
split_times = stopwatch.split_times
elapsed_time = stopwatch.get_elapsed_time(formatted=True)

print(f"Lap times: {lap_times}")
print(f"Split times: {split_times}")
print(f"Elapsed time: {elapsed_time}")
print(f"Elapsed lap time: {elapsed_lap_time}")

# Reset the stopwatch
stopwatch.reset()
```

## Modules

### `timetrack.py`

#### Classes

- **StopWatch**
  - `__init__(self)`: Initialize the `StopWatch` with default attributes.
  - `start(self)`: Start the stopwatch.
  - `lap(self)`: Record a lap time and a split time.
  - `pause(self)`: Pause the stopwatch.
  - `resume(self)`: Resume the stopwatch after a pause.
  - `stop(self)`: Stop the stopwatch.
  - `reset(self)`: Reset all the attributes of the stopwatch.
  - `start_time(self)`: Retrieve the start time.
  - `end_time(self)`: Retrieve the end time.
  - `lap_times(self)`: Retrieve the list of lap times.
  - `split_times(self)`: Retrieve the list of split times.
  - `running(self)`: Check if the stopwatch is running.
  - `paused(self)`: Check if the stopwatch is paused.
  - `get_lap_time(self, index, formatted=False)`: Retrieve the lap time at the specified index.
  - `get_split_time(self, index, formatted=False)`: Retrieve the split time at the specified index.
  - `get_elapsed_time(self, formatted=False)`: Retrieve the elapsed time since the stopwatch started.
  - `get_elapsed_lap_time(self, formatted=False)`: Retrieve the elapsed time since the last lap.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License.
```

This `README.md` file provides a comprehensive overview of the package, installation instructions, usage examples, and descriptions of the class and its methods. Adjust the content as needed to better fit your project's specific requirements.
```