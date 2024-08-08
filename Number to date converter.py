#Number to date converter
#6.2
def format_time(seconds):
    days, seconds = divmod(seconds, 24 * 3600)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    days_word = "день" if days == 1 else "дні" if 1 < days < 5 else "днів"
    return f"{int(days)} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
seconds = int(input("Введіть секунди (від 0 до 8640000): "))
if 0 <= seconds < 8640000:
    print(format_time(seconds))
else:
    print("Некоректне значення. Введіть число від 0 до 8640000.")