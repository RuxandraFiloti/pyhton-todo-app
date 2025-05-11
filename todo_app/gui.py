import modules.functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo')

window = sg.Window('My ToDo App', layout = [[label, input_box]]) #400x400 = layout
window.read()
window.close()