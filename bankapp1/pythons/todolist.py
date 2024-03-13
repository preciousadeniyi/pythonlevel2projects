import mysql.connector 



class ToDoList:
    def __init__(self):
       
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Proma.com2003",
            database="todolist"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            task VARCHAR(255),
                            status BOOLEan
                            )""")
        self.conn.commit()

    def add_task(self,task):
        self.cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, %s)", (task, False))
        self.conn.commit()

    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        return tasks

    def mark_as_done(self, task_id):
        self.cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (True, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            tasks = todo_list.view_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"{task[0]}. {task[1]} - {'Done' if task[2] else 'Not Done'}")
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            todo_list.mark_as_done(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    

if __name__ == "__main__":
    main()
