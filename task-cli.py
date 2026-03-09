import json # ler e converter dados em json
import os # interagir com o sistema operacional 
import sys # interagir com o cmd

from datetime import datetime

# Adicionar, atualizar e excluir tasks

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,'r') as f:  #reader
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f: #write
        json.dump(tasks, f, indent=4)

def get_next_id(tasks): # pegar o proximo id
    return max([t['id'] for t in tasks], default=0) + 1

def find_task_by_id(tasks, task_id): 
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def current_time(): # data e hora atual
    return  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_task(tasks, description):
    
    new_task =  {
    "id": get_next_id(tasks),
    "description": description,
    "status": 'pending',
    "createdAt": current_time(),
    "updateAt": current_time()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(id)
    print(f'Task added sucessfully (ID: {new_task['id']})')

def update(tasks, task_id, description):
    task = find_task_by_id(tasks, task_id)
    if task:
        task['description'] = description
        task['updateAt'] = current_time()
        save_tasks(tasks)
        print(f'Tarefa {task_id} atualizada com sucesso.')
    else:
        print(f'Tarefa {task_id} não encontrada')

def delete(task, task_id):
    original_len = len(tasks)
    task = [t for t in task if t['id']!= task_id]
    if len(tasks) < original_len:
        save_tasks(tasks)
        print(f'Tarefa{task_id} deletado com sucesso!')
    else:
        print(f'Tarefa {task_id} não encontrada')

# Marque uma task como em andamento ou concluída.
def mark_task(tasks, task_id, status):
    task = find_task_by_id(tasks, task_id)
    if task:
        task['status'] = status
        task['updateAt'] = current_time()
        save_tasks(tasks)
        print(f"Tarefa {task_id} marcada como '{status}'")
    else:
        print(f"Tarefa {task_id} não encontrada")

def list_tasks(tasks, status=None):
    filtered = tasks if status is None else [t for t in tasks if t['status'] == status]
    if not filtered:
        print("Nenhuma tarefa encontrada")
        return
    for t in filtered:
        print(f"{t['id']}: {t['description']} - Status: {t['status']}")

def main():
   # executar via comando de cli
    tasks = load_tasks()
    if len(sys.argv) < 2:
        print("Uso: python task_tracker.py <comando> [argumentos]")
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        add_task(tasks, " ".join(sys.argv[2:]))
    elif command == "update" and len(sys.argv) >= 4:
        update_task(tasks, int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete" and len(sys.argv) == 3:
        tasks = delete_task(tasks, int(sys.argv[2]))
    elif command == "progress" and len(sys.argv) == 3:
        mark_task(tasks, int(sys.argv[2]), "progress")
    elif command == "done" and len(sys.argv) == 3:
        mark_task(tasks, int(sys.argv[2]), "done")
    elif command == "list":
        list_tasks(tasks)
    elif command == "list_done":
        list_tasks(tasks, "done")
    elif command == "list_pending":
        list_tasks(tasks, "pending")
    elif command == "list_progress":
        list_tasks(tasks, "progress")
    else:
        print("Comando desconhecido ou argumentos insuficientes")
# Define o ponto de entrada do programa
if __name__ == "__main__":
    main()
