# guitar string dictionary
guitar_strings = {'E1': 1, 'A2': 2, 'D3': 3, 'G4': 4, 'B5': 5, 'E6': 6}

# guitar fret dictionary
guitar_frets = {'fret1': 1, 'fret2': 2, 'fret3': 3, 'fret4': 4, 'fret5': 5, 'fret6': 6,
                'fret7': 7, 'fret8': 8, 'fret9': 9, 'fret10': 10, 'fret11': 11, 'fret12': 12,
                'fret13': 13, 'fret14': 14, 'fret15': 15, 'fret16': 16, 'fret17': 17, 'fret18': 18}


def build_points(music):
    points = []
    for i, note in enumerate(music_list[f'{music}'], start=1):
        # get coordinates of note
        x, y = get_coordinates(note[0], note[1])
        points.append([x, y, note[2]])

    print(f'Music: {music}')
    return points


def get_coordinates(fret_number, string_number):
    x_coordinate = get_fret_coordinates(fret_number)
    y_coordinate = get_string_coordinates(string_number, x_coordinate)
    return x_coordinate, y_coordinate


def get_fret_coordinates(fret_number):
    # length in mm from the nut of the guitar to the bridge of the guitar
    scale_length = 650
    # accumulative length of all frets
    accumulative_length = 0

    # calculate coordinates of fret using the rule of 18 (17.82)
    for i, fret in enumerate(guitar_frets, start=1):
        fret_length = (scale_length - accumulative_length) / 17.82
        # add fret length to accumulative length
        accumulative_length += fret_length

        # reached selected fret
        if i == fret_number:
            # x = total length - half the length of the last fret - half the length of the first fret
            x_coordinate = accumulative_length - (fret_length / 2) - (scale_length / 17.82 / 2)
            return round(x_coordinate, 2)


def get_string_coordinates(string_number, x_coordinate):
    # string E1
    if string_number == 1:
        y_coordinate = 0.0323 * x_coordinate + 34.5027
    # string A2
    elif string_number == 2:
        y_coordinate = 0.0232 * x_coordinate + 28.5168
    # string D3
    elif string_number == 3:
        y_coordinate = 0.0196 * x_coordinate + 21.0004
    # string G4
    elif string_number == 4:
        y_coordinate = 0.0105 * x_coordinate + 14.5145
    # string B5
    elif string_number == 5:
        y_coordinate = 0.0042 * x_coordinate + 7.4858
    # string E6
    else:
        y_coordinate = 0.0022 * x_coordinate + 0.0122

    return y_coordinate


# Survivor – Eye of the tiger
survivor_eye_of_the_tiger = [[guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret1'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret1'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['A2'], 0],
                             [guitar_frets['fret3'], guitar_strings['E1'], 0],
                             [guitar_frets['fret4'], guitar_strings['E1'], 0]]

music_list = {'Survivor – Eye of the tiger': survivor_eye_of_the_tiger}
