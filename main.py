# спросить у пользователя на сколько часов поставить таймер
# базвый таймер подразумивается как таймер на два часа с одним 15 минутным перерывом
# выводить время как 20:05(20 минут 5 секунд)когда время доходит до часа переходим во вкладку 15 минут таймера отдыха
# так же лучше сделать чтобы он шёл от 59:59 до 00:00 так будет проще и нагляднее
# после снова вызвать рабочий час
# после полного окончания таймера стоит вывести что-то одобрительное типа 'Great!You did it!'
import time

minutes = 59
seconds = 60
total_seconds = 0
number_of_timer_hours = int(input("How many hours should the timer be set for? "))


#def timer_with_break()
for hour in range(number_of_timer_hours):
    while minutes > 0:
        while seconds > 0:
            seconds -= 1
            time.sleep(1)
            print(f"{minutes:02d}:{seconds:02d}")
            if seconds ==0:
                minutes -= 1
                seconds=60
            continue
     #if minutes == 0:
        # print("")