from datetime import datetime
# Adicionar, atualizar e excluir tasks
tasks =  []

def add(id, description):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task =  {
    "id": id,
    "description": description,
    "status": 'pending',
    "createdAt": now,
    "updateAt": now
    }

    tasks.append(new_task)
    print(f'Task added sucessfully (ID:{id})')

def update(id, description):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = tasks[id]

    update_task = {
    "id": task,
    "description": description,
    "status": task['status'],
    "createdAt": task['createdAt'],
    "updateAt": now
    }
    task = update_task

def delete(id):
    print(id)
    del tasks[id-1]

# Marque uma task como em andamento ou concluída.
def mark_progress(id):
    tasks[id-1]['status'] = 'progress'
def mark_done(id):
    tasks[id-1]['status'] = 'done'

# Liste todas as tasks
def listAll():
    for task in tasks :
       print(f"task {task['id']}: {task['description']} - Status: {task['status']}")

# Liste todas as tasks que foram realizadas.
def listDone():
    for task in tasks :
       if(task['status'] == 'done'):
           print(f"task {task['id']}: {task['description']} - Status: {task['status']}")

# Liste todas as tasks que não foram concluídas.
def listPending():
    for task in tasks :
        if(task['status'] == 'pending'):
            print(f"task {task['id']}: {task['description']} - Status: {task['status']}")

# Liste todas as tasks que estão em andamento.
def listProgress():
    for task in tasks :
        if(task['status'] == 'progress'):
            print(f"task {task['id']}: {task['description']} - Status: {task['status']}")

def main():
    add(1, 'Buy groceries')
    add(2, 'Buy Journal')

    mark_progress(1)
    mark_done(2)

    listAll()

# Define o ponto de entrada do programa
if __name__ == "__main__":
    main()
