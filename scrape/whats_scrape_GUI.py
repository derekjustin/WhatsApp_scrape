import PySimpleGUI as sg

layout = [
            [sg.Column([[sg.Text('Welcome to the WhatsApp Web Scraping Tool', font=['Comic',30,'bold'], text_color='#ffffff', background_color='#2e9688')]],
                background_color='#2e9688'
                )],
            [sg.Column([[sg.Text('Please Choose One Of The Following Options!', font=['Comic',20,'bold'], text_color='#000000', background_color='#d8dbd4')]],
                background_color='#d8dbd4',
                justification='center',
                pad=(50,50)
                )],
            [sg.Column([[sg.Button('Join Group'),
                         sg.Button('Join Multiple Groups'), 
                         sg.Button('Print Groups')]],
                background_color='#d8dbd4',
                justification='center'
                )]
            ]

# Create the Window
window = sg.Window('Window Title', layout=layout, background_color='#d8dbd4', button_color=['#000000','#2e9688'], margins=[0,0])
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
