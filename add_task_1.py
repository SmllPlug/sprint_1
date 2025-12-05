# Типы багов
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
# тикеты
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
# Словарь для хранения связанных тикетов по типам багов
tickets_by_type = {}
# Функция для удаления дубликатов тикетов
def del_duplicates(dic_tickets):
    # Проходим по ключам словаря тикетов
    for key in dic_tickets:
        unic_tickets=[]
        # Проходим по значениям для каждого ключа
        for value in dic_tickets[key]:
            if value not in unic_tickets:
                unic_tickets.append(value)
        dic_tickets[key] = unic_tickets
    return dic_tickets
            
# Функция для свяывания уровня типа бага с тикетами
def link_types_and_tickets(bug_types, dic_tickets):
    # Список для хранения уже использованных тикетов
    used = []
    # Итоговый словарь с типами багов и их тикетами
    result = {}
    # Проходим по уровням багов от 1 до 5
    for level in range(1, 6):
        clean_list = []
        # Проходим по тикетам для текущего уровня багов
        for ticket in dic_tickets[level]:
            if ticket not in used:
                clean_list.append(ticket)
                used.append(ticket)
        result[bug_types[level]] = clean_list
    return result
           

tickets=del_duplicates(tickets)
tickets_by_type=link_types_and_tickets(types, tickets)
print(tickets_by_type)