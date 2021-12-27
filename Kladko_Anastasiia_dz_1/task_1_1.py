def convert_time(duration: int) -> str:
    if duration < 60 :
        time = (f'{duration} сек')
    elif duration >= 60 and duration < 3600:
        time = (f'{duration//60} мин {duration%60} сек')
    elif duration >= 3600 and duration < 86400 :
        time = (f'{duration//3600} час {duration%3600//60} мин {duration%3600%60} сек')
    elif duration >= 86400 :
        time = (f'{duration//86400} дн {duration%86400//3600} час {duration%86400%3600//60} минут {duration%86400%3600%60} сек')
    return time


duration = 400153
result = convert_time(duration)
print(result)