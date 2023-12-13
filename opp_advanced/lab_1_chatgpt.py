class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not all(isinstance(value, int) for value in (hours, minutes, seconds)):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Unsupported operand type for +: TimeInterval and {}".format(type(other).__name__))
        return TimeInterval.from_seconds(self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Unsupported operand type for -: TimeInterval and {}".format(type(other).__name__))
        return TimeInterval.from_seconds(max(0, self.total_seconds - other.total_seconds))

    def __mul__(self, factor):
        if not isinstance(factor, int):
            raise TypeError("Unsupported operand type for *: TimeInterval and {}".format(type(factor).__name__))
        return TimeInterval.from_seconds(max(0, self.total_seconds * factor))

    def __str__(self):
        hours, remainder = divmod(self.total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    @classmethod
    def from_seconds(cls, total_seconds):
        return cls(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

# Example Usage
time1 = TimeInterval(hours=21, minutes=58, seconds=50)
time2 = TimeInterval(hours=1, minutes=45, seconds=22)

# Addition
result_addition = time1 + time2
assert str(result_addition) == "23:44:12"
print("Addition:", result_addition)

# Subtraction
result_subtraction = time1 - time2
assert str(result_subtraction) == "20:13:28"
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = time1 * 2
assert str(result_multiplication) == "43:57:40"
print("Multiplication:", result_multiplication)
