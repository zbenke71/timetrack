import time
import logging

logger = logging.getLogger(__name__)


class StopWatch:
    """
    A simple stopwatch implementation for measuring elapsed time, recording laps, and splits.

    https://bennet.hu
    """

    def __init__(self):
        self._start_time = None
        self._rel_start_time = None
        self._end_time = None
        self._running = False
        self._paused = False
        self._lap_times = []
        self._split_times = []

    def start(self):
        """
        Start the stopwatch. The method can only be applied when the stopwatch is stopped or reset.
        """
        if not self._running:
            self._start_time = time.time()
            self._rel_start_time = self._start_time
            self._running = True
            self._end_time = None
            self._lap_times = []
            self._split_times = []
            logger.info("Stopwatch started")
        else:
            logger.warning("Cannot start: stopwatch is running")

    def lap(self):
        """
        Record a lap time and a split time. It cannot be applied if the stopwatch is paused or not running.
        """
        if self._running and not self._paused:
            self._split_times.append(time.time() - self._rel_start_time)
            num = len(self._split_times)
            if num > 1:
                self._lap_times.append(self._split_times[-1] - self._split_times[-2])
            else:
                self._lap_times.append(self._split_times[-1])
            logger.info("Lap recorded")
        else:
            logger.warning("Cannot record lap: stopwatch is paused or not running")

    def pause(self):
        """
        Pause the stopwatch. It cannot be applied if the stopwatch is already paused or not running.
        """
        if self._running and not self._paused:
            self._end_time = time.time()
            self._paused = True
            logger.info("Stopwatch paused")
        else:
            logger.warning("Cannot pause: stopwatch is already paused or not running")

    def resume(self):
        """
        Resume the stopwatch after a pause.
        """
        if self._running and self._paused:
            self._rel_start_time += time.time() - self._end_time
            self._end_time = None
            self._paused = False
            logger.info("Stopwatch resumed")
        else:
            logger.warning("Cannot resume: stopwatch is not paused")

    def stop(self):
        """
        Stop the stopwatch. If there are laps recorded, the lap time and split time of the last lap will be recorded.
        It cannot be applied if the stopwatch is not running.
        """
        if self._running:
            self._end_time = time.time()
            self._running = False
            if self._split_times:
                self._split_times.append(self._end_time - self._rel_start_time)
                num = len(self._split_times)
                if num > 1:
                    self._lap_times.append(self._split_times[-1] - self._split_times[-2])
                else:
                    self._lap_times.append(self._split_times[-1])
            logger.info("Stopwatch stopped")
        else:
            logger.warning("Cannot stop: stopwatch is not running")

    def reset(self):
        """
        Reset all the attributes.
        """
        self._start_time = None
        self._rel_start_time = None
        self._end_time = None
        self._running = False
        self._paused = False
        self._lap_times = []
        self._split_times = []
        logger.info("Stopwatch reset")

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def lap_times(self):
        return self._lap_times

    @property
    def split_times(self):
        return self._split_times

    @property
    def running(self):
        """
        :return: True if the stopwatch is running. False if it is not running. It is running even when the stopwatch is paused.
        """
        return self._running

    @property
    def paused(self):
        """
        :return: True if the stopwatch is running but paused. False if it is not running or running but not paused.
        """
        return self._paused

    def get_lap_time(self, index, formatted=False) -> float | str:
        """
        Retrieve the lap time at the specified index.

        :param index: The index of the lap time to retrieve.
        :param formatted: Whether to return the lap time in formatted (str) or float representation.
        :return: The lap time at the specified index.
        """
        if self._lap_times:
            num = len(self._lap_times)
            if 0 <= index < num or 0 > index >= -num:
                lap_time = self._lap_times[index]
                if formatted:
                    return self._str_time(lap_time)
                else:
                    return lap_time
            else:
                raise IndexError("Index out of range")
        else:
            raise IndexError("No lap recorded")

    def get_split_time(self, index, formatted=False) -> float | str:
        """
        Retrieve the split time at the specified index.

        :param index: The index of the split time to retrieve.
        :param formatted: Whether to return the split time in formatted (str) or float representation.
        :return: The split time at the specified index.
        """
        if self._split_times:
            num = len(self._split_times)
            if 0 <= index < num or 0 > index >= -num:
                split_time = self._split_times[index]
                if formatted:
                    return self._str_time(split_time)
                else:
                    return split_time
            else:
                raise IndexError("Index out of range")
        else:
            raise IndexError("No split recorded")

    def get_elapsed_time(self, formatted=False) -> float | str:
        """
        Retrieve the elapsed time since the stopwatch started.

        :param formatted: Whether to return the elapsed time in formatted (str) or float representation.
        :return: The elapsed time since the stopwatch started.
        """
        elapsed_time = self._calculate_elapsed_time()
        if formatted:
            return self._str_time(elapsed_time)
        else:
            return elapsed_time

    def get_elapsed_lap_time(self, formatted=False) -> float | str:
        """
        Retrieve the elapsed time since the last lap.

        :param formatted: Whether to return the elapsed time in formatted (str) or float representation.
        :return: The elapsed time since the last lap.
        """
        elapsed_lap_time = self._calculate_elapsed_lap_time()
        if formatted:
            return self._str_time(elapsed_lap_time)
        else:
            return elapsed_lap_time

    def _calculate_elapsed_time(self):
        if self._start_time is None:
            return 0
        elif self._end_time is None:
            return time.time() - self._rel_start_time
        else:
            return self._end_time - self._rel_start_time

    def _calculate_elapsed_lap_time(self):
        if self._split_times:
            return self._calculate_elapsed_time() - self._split_times[-1]
        else:
            return self._calculate_elapsed_time()

    @staticmethod
    def _str_time(float_time: float) -> str:
        if float_time < 3600:
            return time.strftime("%M:%S", time.gmtime(float_time))
        elif float_time < 86400:
            return time.strftime("%H:%M:%S", time.gmtime(float_time))
        else:
            return str(int(float_time // 86400)) + " day(s) and " + time.strftime("%H:%M:%S", time.gmtime(float_time % 86400))
