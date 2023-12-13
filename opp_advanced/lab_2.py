class TimeInterval:
    def __init__(self, hours, minutes, seconds) -> None:
        if not all(isinstance(value, int) for value in (hours, minutes, seconds)):
            raise TypeError()
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total = (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def __str__(self) -> str:
        hours = self.total // 3600
        minutes = (self.total % 3600) // 60
        seconds = self.total % 60
        return f"{hours}:{minutes}:{seconds}"
    
    def __add__(self, other):
        self.total = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        if isinstance(other, int):
            self.total += other
        else:
            self.total += other.total
        return self.__str__()
    
    def __sub__(self, other):
        self.total = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        if isinstance(other, int):
            self.total -= other
        else:
            self.total -= other.total
        return self.__str__()
    
    def __mul__(self, other):
        self.total = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        self.total *= other
        return self.__str__()



fti = TimeInterval(21,58,50)
sti = TimeInterval(1,45,22)
print(fti)
print(sti)
print(fti + sti)
print(fti - sti)
print(fti * 2)

print(fti + 62)
print(fti - 62)
