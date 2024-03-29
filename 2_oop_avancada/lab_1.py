class TimeInterval:
    def __init__(self, hour, minute, second):
        if not all(isinstance(val, int) for val in (hour, minute, second)):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        self.hour = hour * 3600
        self.minute = minute * 60
        self.second = second
        self.total_seconds = self.hour + self.minute + self.second

    def __add__(self, other):
        self.total = self.total_seconds + other.total_seconds
        return self.__str__()

    def __sub__(self, other):
        self.total = self.total_seconds - other.total_seconds
        return self.__str__()

    def __mul__(self, other):
        self.total = self.total_seconds * other
        return self.__str__()

    def __str__(self):
        return f"{self.total // 3600}:{self.total % 3600 // 60}:{self.total % 60}"


fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)

print(fti + sti)
print(fti - sti)
print(fti * 2)

assert fti + sti == "23:44:12"
assert fti - sti == "20:13:28"
assert fti * 2 == "43:57:40"
