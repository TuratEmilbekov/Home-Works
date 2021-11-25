import sqlite3
import random
database = sqlite3.connect("todo_server.sqlite3")
sql = database.cursor()

# sql.execute(
#     """
#     CREATE TABLE todo(
#        id INT,
#        time TEXT, 
#        plan TEXT, 
#        done BIT
#     )
#     """
# )

database.commit()


def todoaddlist():
    global todo_id, todo_time, todo_plan, todo_done
    todo_id = input('id: ')
    todo_time = input('time: ')
    todo_plan = input('plan: ')
    todo_done = input('done: ')
    
    sql.execute("SELECT id FROM todo WHERE id = '{todo_id}'")
    done = random.randint(0,1)
    if sql.fetchone() is None:
        sql.execute("INSERT INTO todo VALUES (?,?,?,?)", 
            (todo_id, todo_time, todo_plan,done ))
        sql.execute("SELECT * FROM todo;")
        print(todo_id, todo_time, todo_plan, done)

        database.commit()
        print("Todolist allready done!!!")
    else:
        print("Todolist is not done!")
        for values in sql.execute("SELECT * FROM todo"):
            print(values)
        
todoaddlist()


def deletedonelist():
    sql.execute("DELETE FROM todo WHERE done = 1;")