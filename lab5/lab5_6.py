class Time:
    hours: int
    minutes: int

    def __init__(self, hours, minutes) -> None:
        self.hours = hours
        self.minutes = minutes

    def add_time(self, hours, minutes) -> None:
        self.hours += hours
        self.minutes += minutes

    def display(self):
        return self.hours, self.minutes

    def display_minutes(self) -> int:
        return self.minutes + self.hours * 60


zegar1: Time = Time(6, 30)
print(f"Aktualna godzina:{zegar1.display()}")
