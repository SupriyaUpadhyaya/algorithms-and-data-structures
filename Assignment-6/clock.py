class Clock:
    hours: int = 0
    minutes: int = 0

    def __init__(self, hours: int, minute: int) -> None:

        if (hours < 0) or (minute < 0):
            print("Invalid time input!")
            return
        else:
            self.hours = hours
            self.minutes = minute
            self.__normalize__()

    def __str__(self) -> str:
        if (self.hours < 10):
            hours = "0" + str(self.hours)
        else:
            hours = str(self.hours)

        if (self.minutes < 10):
            minute = "0" + str(self.minutes)
        else:
            minute = str(self.minutes)
        
        return (hours + ":" + minute)

    def __eq__(self, other: object) -> bool:
        # if self and other are of different, incompatible types, they are not equal
        if not isinstance(other, Clock):
            return False
        elif self.hours == other.hours and self.minutes == other.minutes:
            return True
        else:
            return False

    def __add__(self, other: "Clock") -> "Clock":
        newhours = other.hours + self.hours
        newminutes = other.minutes + self.minutes

        newClock = Clock(newhours, newminutes)

        return newClock

    def __normalize__(self) -> None:
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

        if self.hours >= 24:
            self.hours = self.hours % 24
        else:
            self.hours = self.hours
        
        return None

    def add_minutes(self, minutes: int) -> "Clock":
        self.minutes += minutes
        self.__normalize__()

        return self


if __name__ == "__main__":
    clock1 = Clock(100, 59)
    clock2 = Clock(100, 59)
    print(clock1)
    print(clock2)
    print(clock1 == clock2)
    print(clock1.__add__(clock1))
    clock1.add_minutes(15)
    print(clock1)
