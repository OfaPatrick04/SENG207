import pyttsx3
import PySimpleGUI as sg

engine = pyttsx3.init()

layout = [
    [sg.Text('Enter text to speak: '), sg.Input(key='-INPUT-')],
    [sg.Text('Select voice type: '), sg.DropDown(['Male', 'Female'], key='-VOICE-')],
    [sg.Button('speak', key='-SPEAK-')]
]

window = sg.Window('Text-to-speech App', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-SPEAK-':
        text = values['-INPUT-']
        
        voice = 'english+m' if values['-VOICE-'] == 'Male' else 'english+f'
        engine.setProperty('voice', voice)
        
        engine.say(text)
        engine.runAndWait()
        
engine.stop()
engine.shutdown()
