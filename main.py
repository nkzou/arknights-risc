import PySimpleGUI as sg

sg.theme('Default 1')

menu_def = [
    ['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
    ['&Help', '&About...']
]

atk_frame = sg.Frame('Source Stats', [
    [sg.Text("Base Attack", font="Any 12")],
    [sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

spd_frame = sg.Frame('Source Attack Speed', [
    [sg.Text("Base Interval", font="Any 12")],
    [sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

def_frame = sg.Frame('Target Stats', [
    [sg.Text("Base Defense", font="Any 12")],
    [sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

mov_frame = sg.Frame('Target Walk Speed', [
    [sg.Text("Movement Speed", font="Any 12")],
    [sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

phy_frame = sg.Frame('Physical Damage', [
    [sg.Text("Attack Scale", font="Any 12"),
     sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

art_frame = sg.Frame('Arts Damage', [
    [sg.Text("Attack Scale", font="Any 12"),
     sg.InputText(size=(20, None), font="Any 12")]
], font="Any 14")

dps_frame = sg.Frame("Damage Breakdown", [[

]], font="Any 14")

layout = [
    [sg.Column([[atk_frame]], expand_y=True),
     sg.Column([[spd_frame]], expand_y=True),
     sg.Column([[def_frame]], expand_y=True),
     sg.Column([[mov_frame]], expand_y=True)],
    [sg.Column([[phy_frame]], expand_x=True, expand_y=True),
     sg.Column([[art_frame]], expand_x=True, expand_y=True)],
    [sg.Column([[dps_frame]], expand_x=True, expand_y=True)]
]

frames = [atk_frame, spd_frame, def_frame,
          mov_frame, dps_frame, phy_frame, art_frame]

window = sg.Window('Rhodes Island Simulation Complex', layout, finalize=True)

for frame in frames:
    frame.expand(expand_x=True, expand_y=True)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
