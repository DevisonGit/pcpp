class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not all(isinstance(value, int) for value in (hours, minutes, seconds)):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return TimeInterval.from_seconds(self.total_seconds + other.total_seconds)
        elif isinstance(other, int):
            return TimeInterval.from_seconds(self.total_seconds + other)
        else:
            raise TypeError("Unsupported operand type for +: TimeInterval and {}".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return TimeInterval.from_seconds(max(0, self.total_seconds - other.total_seconds))
        elif isinstance(other, int):
            return TimeInterval.from_seconds(max(0, self.total_seconds - other))
        else:
            raise TypeError("Unsupported operand type for -: TimeInterval and {}".format(type(other).__name__))

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

# Addition of integer (seconds)
result_addition_int = time1 + 62
assert str(result_addition_int) == "21:59:52"
print("Addition (Integer):", result_addition_int)

# Subtraction of integer (seconds)
result_subtraction_int = time1 - 62
assert str(result_subtraction_int) == "21:57:48"
print("Subtraction (Integer):", result_subtraction_int)
