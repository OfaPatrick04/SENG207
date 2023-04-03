import PySimpleGUI as sg
import qrcode

sg.theme('DarkBlue4')

layout = [[sg.Text('Enter Text: '), sg.InputText()],
          [sg.Button('Create')], 
          [sg.Image(key='-IMAGE-', size=(200, 100))]]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Create':
        data = values[0] 
        if data:
            img = qrcode.make(data)
            img.save('qrcode.png')
            window['-IMAGE-'].update(filename='qrcode.png')

window.close()