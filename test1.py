import PySimpleGUI as sg

layout = [
    [sg.Button("Do not click me", k="addBtn")],
    [sg.Text("You are lucky to run this app")]
]
win = sg.Window("This is a window", layout)
while True:
    events, value = win.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == "addBtn":
        print("Why?")
        
win.close()