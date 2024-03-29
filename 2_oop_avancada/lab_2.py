class TimeInterval:
    def __init__(self, hour, minute, second):
        if not all(isinstance(val, int) for val in (hour, minute, second)):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        self.hour = hour * 3600
        self.minute = minute * 60
        self.second = second
        self.total_seconds = self.hour + self.minute + self.second

    def __add__(self, other):
        if isinstance(other, int):
            self.total = self.total_seconds + other
        else:
            self.total = self.total_seconds + other.total_seconds
        return self.__str__()

    def __sub__(self, other):
        if isinstance(other, int):
            self.total = self.total_seconds - other
        else:
            self.total = self.total_seconds - other.total_seconds
        return self.__str__()

    def __mul__(self, other):
        self.total = self.total_seconds * other
        return self.__str__()

    def __str__(self):
        return f"{(self.total // 3600):02d}:{(self.total % 3600 // 60):02d}:{(self.total % 60):02d}"


fti = TimeInterval(21, 58, 50)


print(fti + 62)
print(fti - 62)


assert fti + 62 == "21:59:52"
assert fti - 62 == "21:57:48"
