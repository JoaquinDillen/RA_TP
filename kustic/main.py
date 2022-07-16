from py_openshowvar import openshowvar
import cv2

# guitar string dictionary
guitar_strings = {'E1': 1, 'A2': 2, 'D3': 3, 'G4': 4, 'B5': 5, 'E6': 6}
# guitar fret dictionary
guitar_frets = {'fret1': 1, 'fret2': 2, 'fret3': 3, 'fret4': 4, 'fret5': 5, 'fret6': 6,
                'fret7': 7, 'fret8': 8, 'fret9': 9, 'fret10': 10, 'fret11': 11, 'fret12': 12,
                'fret13': 13, 'fret14': 14, 'fret15': 15, 'fret16': 16, 'fret17': 17, 'fret18': 18}

# length in cm from the nut of the guitar to the bridge of the guitar
scale_length = 650
# accumulative length of all frets
accumulative_length = 0


def main():
    # connect to kuka
    client = openshowvar("192.168.10.254", 7000)

    # initialize music array
    music = [[guitar_frets['fret1'], guitar_strings['E1'], 0],
             [guitar_frets['fret2'], guitar_strings['A2'], 0],
             [guitar_frets['fret3'], guitar_strings['D3'], 0],
             [guitar_frets['fret4'], guitar_strings['G4'], 0],
             [guitar_frets['fret5'], guitar_strings['B5'], 0],
             [guitar_frets['fret6'], guitar_strings['E6'], 0],
             [guitar_frets['fret7'], guitar_strings['E1'], 0],
             [guitar_frets['fret8'], guitar_strings['A2'], 0],
             [guitar_frets['fret9'], guitar_strings['D3'], 0],
             [guitar_frets['fret10'], guitar_strings['G4'], 0]]

    # write points to kuka
    for i, note in enumerate(music):
        # write guitar fret variable
        client.write(f'POINTS[{i+1}].POINT.X', f'{get_fret_coordinates(note[0])}', debug=False)
        # write guitar string variable
        client.write(f'POINTS[{i+1}].POINT.Y', f'{get_string_coordinates(note[1])}', debug=False)

    # give start order to kuka
    client.write('KUSTIC_START', 'TRUE', debug=False)

    client.close()


def get_fret_coordinates(fret_number):
    # use global variable accumulative_length
    global accumulative_length

    # calculate coordinates of fret using the rule of 18 (17.82)
    for i, fret in enumerate(guitar_frets, start=1):
        fret_length = ((scale_length - accumulative_length) / 17.82)
        # add fret length to accumulative length
        accumulative_length += fret_length

        # reached selected fret
        if i == fret_number:
            # x = total length - half the length of the last fret - the length of the first fret
            x_coordinate = accumulative_length - (fret_length / 2) - (scale_length / 17.82 / 2)
            # reset accumulative length
            accumulative_length = 0
            print(f'fret: {i} x: {round(x_coordinate, 2)}')
            return round(x_coordinate, 2)

    """
    x_coordinate = -0.0003*fret_number**5 + 0.0158*fret_number**4 - 0.3406*fret_number**3 + \
                   2.6362*fret_number**2 + 20.366*fret_number - 25.707
    return x_coordinate
    """


def get_string_coordinates(string_number):
    y_coordinate = 0
    return y_coordinate


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
