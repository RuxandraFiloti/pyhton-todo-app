#from functions import get_todos, write_todos
import time
from modules import functions

text = """
Principles of productivity:
Managing ypu inner flow.
Systemizing everything that repeats.
"""
now = time.strftime("%b %d, %Y %H:%M:%S") 
print("It is ", now)
  
# exemplu facut cu if-else
while True:
    #Get user input and remove space chars from it 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    

    if user_action.startswith("add"):
    #if 'add' in user_action or 'new' in user_action:  #if 'add' not in user_action:
           # todo = input("Enter a todo: ") + "\n"
            todo = user_action[4:] # adauga dupa 'add' ce este introdus in inputul cu enter a todo -> list slice operation
            # 4 este char cu indice 4 
            # poate fi si [4:8] - interval de la char ul care incepe pana la cel final
            todos = functions.get_todos()

            todos.append(todo + '\n') 

            functions.write_todos(todos)

           

    elif user_action.startswith("show"):
        
           todos = functions.get_todos()

           for index, item in enumerate(todos):
               item = item.strip('\n') 
               item = item.title()
               row = f"{index + 1}-{item}"
               #print(index, '.', item)
               print(row)
    elif user_action.startswith("edit"):
              try:
            #number = int(input("Number of todo list to edit: "))
                number = int(user_action[5:])
                number = number - 1

                todos = functions.get_todos()

                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo + '\n'
              
                functions.write_todos(todos)
              except ValueError:
                   print("Your command is not valid.")
                   continue

    elif user_action.startswith("complete"):
              try:
           # number = int(input("Number of todo list to complete: "))
                number = int(user_action[9:])

                todos = functions.get_todos()

                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)

                message = f"Todo {todo_to_remove} was removed from the list"
                print(message)
              except IndexError:
                   print("There is no item with that number.")
                   continue 
              
    elif user_action.startswith("exit"):
            break
    else:
         print("Command is not valid!")
       
print("Bye!")


# exemplu facut cu match-case
# while True:
#     #Get user input and remove space chars from it 
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
    
#     match user_action:
#         #check if user action is "add"
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"

#             # file = open('files/todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()

#             # with context manager -> reduce din cod
#             with open('files/todos.txt', 'r') as file:
#                  todos = file.readlines()

#             todos.append(todo) #modificare in fisier -> pastreaza in memorie cele deja scrise si adauga unele noi

#             #write todos in the file
#             # file = open('files/todos.txt', 'w')
#             # file.writelines(todos)
#             # file.close()
#             with open('files/todos.txt', 'w') as file:
#                 file.writelines(todos)

#         case "show" | 'display':
#         #    file = open('files/todos.txt', 'r')
#         #    todos = file.readlines()
#         #    file.close()
#            with open('files/todos.txt', 'r') as file:
#               todos = file.readlines()
#            #new_todo = [item.strip('\n') for item in todos] # elimina spatiile intre elemente (ENTER)

#            #echivalent a ce este scris sus este aici
#         #    new_todo = []

#         #    for item in todos:
#         #        new_item = item.strip('\n')
#         #        new_todo.append(new_item)

#            for index, item in enumerate(todos):
#                item = item.strip('\n') # elimina spatiul ENTER dintre elemente
#                item = item.title()
#                row = f"{index + 1}-{item}"
#                #print(index, '.', item)
#                print(row)
#         case "edit":
#             number = int(input("Number of todo list to edit: "))
#             number = number - 1

#             with open('files/todos.txt', 'r') as file:
#               todos = file.readlines()

#             new_todo = input("Enter a new todo: ")
#             todos[number] = new_todo + '\n'
#             # existing_todo = todos[number] 
#             # print(existing_todo)
           
#             with open('files/todos.txt', 'w') as file:
#                 file.writelines(todos)

#         case "complete":
#             number = int(input("Number of todo list to complete: "))

#             with open('files/todos.txt', 'r') as file:
#               todos = file.readlines()

#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)

#             with open('files/todos.txt', 'w') as file:
#                 file.writelines(todos)

#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         case 'exit':
#             break
#         # case _:   #_ folosita in loc de variabila, semnifica whatever - conventie programatori
#         #     print("Hey, you're wrong!")
# print("Bye!")



   
   

