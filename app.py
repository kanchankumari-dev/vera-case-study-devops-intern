# Tiny Task Tracker - add/list tasks saved to a local JSON file
import json, os
from config import API_KEY, DB_PATH

def load_tasks():
    if not os.path.exists(DB_PATH):
        return []
    return json.load(open(DB_PATH))

def save_tasks(tasks):
    json.dump(tasks, open(DB_PATH, "w"), indent=2)

def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        print(f"[{'x' if t['done'] else ' '}] {i}. {t['text']}")

def main():
    print(f"Task Tracker (using API key: {API_KEY[:8]}...)")
    while True:
        cmd = input("\n(a)dd, (l)ist, (q)uit > ").strip().lower()
        if cmd == "a": add_task(input("Task: "))
        elif cmd == "l": list_tasks()
        elif cmd == "q": break

if __name__ == "__main__":
    main()
