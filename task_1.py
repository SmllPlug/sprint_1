time_value = '1h 45m,360s,25m,30m 120s,2h 60s'
# Переменная для счета общего количества минут
count_minutes = 0
# Разделяем строку на отдельные части по запятой
time_parts = time_value.split(',')
for part in time_parts:
    # Разделяем каждую часть по пробелу
    parts = part.split()
    # Переменная для счета минут в часах, минутах и секундах
    minutes = 0
    for i in parts:
        # Проверяем есть ли в части "h" для часов и если есть считаем и переводим в минуты
        if "h" in i:
            hours=int(i.replace("h",""))
            minutes += hours * 60
        # Проверяем если в части "m" для минут и если есть считаем минуты    
        elif "m" in i:
            mins=int(i.replace("m",""))
            minutes += mins
        # Проверяем если в части "s" для секунд и если есть считаем и переводим в минуты
        elif "s" in i:
            secs=int(i.replace("s",""))
            minutes += secs // 60
    # Считаем общее количество минут
    count_minutes += minutes
print(f"Общее количество минут: {count_minutes}")