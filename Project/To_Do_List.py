tasks = {}

def add_task(task_id, task_name):
    tasks[task_id] = {"task": task_name, "done": False}
    print(f"Task '{task_name}' added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, info in tasks.items():
            status = "Done" if info["done"] else "Not Done"
            print(f"ID: {task_id} | Task: {info['task']} | Status: {status}")

def mark_done(task_id):
    if task_id in tasks:
        tasks[task_id]["done"] = True
        print(f"Task '{tasks[task_id]['task']}' marked as done!")
    else:
        print("Task not found.")

def delete_task(task_id):
    if task_id in tasks:
        removed = tasks.pop(task_id)
        print(f"Task '{removed['task']}' deleted!")
    else:
        print("Task not found.")


add_task(1, "Study Python")
add_task(2, "Web development")
view_tasks()
mark_done(1)
view_tasks()
delete_task(2)
view_tasks()
