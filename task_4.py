new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
# Добавляем задачу из new_tasks в completed_tasks и удаляем её из new_tasks
completed_tasks.append(new_tasks.pop(4))
# Удаляем задачу "task_007" из new_tasks
new_tasks.remove("task_007")
# Выводим последний элемент списка new_tasks
print(new_tasks[-1:])