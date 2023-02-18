import functions
import PySimpleGUI
import time

PySimpleGUI.theme("Black")

clock = PySimpleGUI.Text('', key='clock')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%H:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first.")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select an item first.")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()