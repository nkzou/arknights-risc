import PySimpleGUI as sg

sg.theme('Default 1')

menu_def = [
    ['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
    ['&Help', '&About...']
]

atk_frame = sg.Frame('Attacker', [[

]], font="Any 12")

spd_frame = sg.Frame('Attack Speed', [[

]], font="Any 12")

def_frame = sg.Frame('Defender', [[

]], font="Any 12")

mov_frame = sg.Frame('Defender Movement', [[

]], font="Any 12")

input_layout = [
    sg.Column([[atk_frame]], expand_x=True, expand_y=True),
    sg.Column([[spd_frame]], expand_x=True, expand_y=True),
    sg.Column([[def_frame]], expand_x=True, expand_y=True),
    sg.Column([[mov_frame]], expand_x=True, expand_y=True)
]

dps_frame = sg.Frame("Damage Breakdown", [[

]], font="Any 12")

output_layout = [
    sg.Column([[dps_frame]], expand_x=True, expand_y=True)
]

layout = [
    input_layout,
    output_layout
]

frames = [atk_frame, spd_frame, def_frame, mov_frame, dps_frame]

window = sg.Window('Rhodes Island Simulation Complex', layout, finalize=True, resizable=True, size=(900, 600))
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
