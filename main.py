# спросить у пользователя на сколько часов поставить таймер
# базвый таймер подразумивается как таймер на два часа с одним 15 минутным перерывом
# выводить время как 20:05(20 минут 5 секунд)когда время доходит до часа переходим во вкладку 15 минут таймера отдыха
# так же лучше сделать чтобы он шёл от 59:59 до 00:00 так будет проще и нагляднее
# после снова вызвать рабочий час
# после полного окончания таймера стоит вывести что-то одобрительное типа 'Great!You did it!'
import time
from exceptions import InvalidHours


def get_valid_hours() -> int:
    while True:
        try:
            hours = get_hours_input()
            validate_hours(hours)
            break
        except InvalidHours:
            print("Please enter a valid number")
    return hours


def get_hours_input() -> int:
    raw_hours = input("How many hours should the timer be set for? ")
    try:
        int_hours = int(raw_hours)
        return int_hours
    except ValueError:
        raise InvalidHours



def validate_hours(hours: int) -> None:
    if hours <= 0:
        raise InvalidHours


def main():
    hours = get_valid_hours()


main()


def timer(hours, minutes=59, seconds=60):
    for hour in range(hours):
        while minutes > 0:
            while seconds > 0:
                seconds -= 1
                time.sleep(1)
                print(f"{minutes:02d}:{seconds:02d}")
                if seconds == 0:
                    minutes -= 1
                    seconds = 60
                continue
