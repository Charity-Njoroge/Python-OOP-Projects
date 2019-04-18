class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        print("%.2d : %.2d : %.2d" % (self.hour, self.minute, self.second))

    # method to change time to integer (represent time in seconds)
    def time_to_int(self):
        minutes = (self.hour * 60) + self.minute
        seconds = (minutes * 60) + self.second
        return seconds

    # method to add an object to another object or a number to an object
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    # method to add a number to a Time object
    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


# function  to change seconds to time format
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


# driver program
start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)


