def add_task(task_list, task):
    task_obj = {"id": len(task_list) + 1, "task": task}
    task_list.append(task_obj)
    return task_obj

def list_tasks(task_list):
    return task_list
