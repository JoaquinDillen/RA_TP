# guitar string dictionary
guitar_strings = {'E1': 1, 'B2': 2, 'G3': 3, 'D4': 4, 'A5': 5, 'E6': 6}

# guitar fret dictionary
guitar_frets = {'fret0': 0, 'fret1': 1, 'fret2': 2, 'fret3': 3, 'fret4': 4, 'fret5': 5, 'fret6': 6,
                'fret7': 7, 'fret8': 8, 'fret9': 9, 'fret10': 10, 'fret11': 11, 'fret12': 12,
                'fret13': 13, 'fret14': 14, 'fret15': 15, 'fret16': 16, 'fret17': 17, 'fret18': 18}

# tempos duration dictionary
tempos = {'semibreve': 1, 'minim': 1/2, 'crotchet': 1/4,
         'quaver': 1/8, 'semiquaver': 1/16, 'demisemiquaver': 1/32}

# time established per note
beat = 1


def build_points(music):
    points = []
    print('Music: ', music_list[f'{music}'])
    for i, note in enumerate(music_list[f'{music}'], start=1):
        # get coordinates of note
        x, y = get_coordinates(note[0], note[1])
        points.append([x, y, note[2]])

    return points


def get_coordinates(fret_number, string_number):
    if fret_number == 0:
        x_coordinate = -1
    else:
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
    # string B2
    elif string_number == 2:
        y_coordinate = 0.0232 * x_coordinate + 28.5168
    # string G3
    elif string_number == 3:
        y_coordinate = 0.0196 * x_coordinate + 21.0004
    # string D4
    elif string_number == 4:
        y_coordinate = 0.0105 * x_coordinate + 14.5145
    # string A5
    elif string_number == 5:
        y_coordinate = 0.0042 * x_coordinate + 7.4858
    # string E6
    else:
        y_coordinate = 0.0022 * x_coordinate + 0.0122

    return round(y_coordinate, 2)


# Test – Test
test = [[guitar_frets['fret1'], guitar_strings['E6'], 0]]

# Survivor – Eye of the tiger
survivor_eye_of_the_tiger = [[guitar_frets['fret3'], guitar_strings['A5'], tempos['minim'] * beat],
                             [guitar_frets['fret3'], guitar_strings['A5'], tempos['crotchet'] * beat],
                             [guitar_frets['fret1'], guitar_strings['A5'], tempos['crotchet'] * beat],
                             [guitar_frets['fret3'], guitar_strings['A5'], tempos['minim'] * beat],
                             [guitar_frets['fret3'], guitar_strings['A5'], tempos['crotchet'] * beat],
                             [guitar_frets['fret1'], guitar_strings['A5'], tempos['crotchet'] * beat],
                             [guitar_frets['fret3'], guitar_strings['A5'], tempos['minim'] * beat],
                             [guitar_frets['fret3'], guitar_strings['A5'], tempos['crotchet'] * beat],
                             [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                             [guitar_frets['fret4'], guitar_strings['E6'], tempos['semibreve'] * beat]]

# Queen – We Will Rock You
queen_we_will_rock_you = [[guitar_frets['fret9'], guitar_strings['A5'], tempos['minim'] * beat],
                          [guitar_frets['fret8'], guitar_strings['A5'], tempos['minim'] * beat],
                          [guitar_frets['fret6'], guitar_strings['A5'], tempos['minim'] * beat],
                          [guitar_frets['fret4'], guitar_strings['A5'], tempos['minim'] * beat],
                          [guitar_frets['fret6'], guitar_strings['A5'], tempos['crotchet'] * beat],
                          [guitar_frets['fret6'], guitar_strings['A5'], tempos['minim'] * beat],
                          [guitar_frets['fret6'], guitar_strings['A5'], tempos['crotchet'] * beat],
                          [guitar_frets['fret6'], guitar_strings['A5'], tempos['minim'] * beat]]

# Batman Theme
batman_theme = [[guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret0'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret1'], guitar_strings['A5'], tempos['demisemiquaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['quaver'] * beat],
                [guitar_frets['fret2'], guitar_strings['A5'], tempos['quaver'] * beat]]

# AC/DC – Dirty Deeds Done Dirt Cheap
acdc_dirty_deeds_done_dirt_cheap = [[guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret5'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret10'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret5'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret10'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret5'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret10'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret5'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat],
                                    [guitar_frets['fret10'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['semibreve'] * beat]]

# George Thorogood – Bad to the Bone
george_thorogood_bad_to_the_bone = [[guitar_frets['fret0'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret5'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret3'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['quaver'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['quaver'] * beat],
                                    [guitar_frets['fret0'], guitar_strings['E6'], tempos['quaver'] * beat]]

# The Troggs – Wild Thing
the_troggs_wild_thing = [[guitar_frets['fret0'], guitar_strings['E6'], tempos['quaver'] * beat],
                         [guitar_frets['fret0'], guitar_strings['E6'], tempos['minim'] * beat],
                         [guitar_frets['fret5'], guitar_strings['E6'], tempos['quaver'] * beat],
                         [guitar_frets['fret5'], guitar_strings['E6'], tempos['minim'] * beat],
                         [guitar_frets['fret7'], guitar_strings['E6'], tempos['quaver'] * beat],
                         [guitar_frets['fret7'], guitar_strings['E6'], tempos['minim'] * beat],
                         [guitar_frets['fret5'], guitar_strings['E6'], tempos['quaver'] * beat],
                         [guitar_frets['fret5'], guitar_strings['E6'], tempos['minim'] * beat]]

# The White Stripes – Seven Nation Army
the_white_stripes_seven_nation_army = [[guitar_frets['fret7'], guitar_strings['A5'], tempos['minim'] * beat],
                                       [guitar_frets['fret7'], guitar_strings['A5'], tempos['quaver'] * beat],
                                       [guitar_frets['fret10'], guitar_strings['A5'], tempos['quaver'] * beat],
                                       [guitar_frets['fret7'], guitar_strings['A5'], tempos['quaver'] * beat],
                                       [guitar_frets['fret5'], guitar_strings['A5'], tempos['quaver'] * beat],
                                       [guitar_frets['fret3'], guitar_strings['A5'], tempos['minim'] * beat],
                                       [guitar_frets['fret2'], guitar_strings['A5'], tempos['minim'] * beat]]

# Jimi Hendrix – All Along the Watchtower
jimi_hendrix_all_along_the_watchtower = [[guitar_frets['fret6'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret6'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                         [guitar_frets['fret8'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret8'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret8'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret8'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                         [guitar_frets['fret6'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret6'], guitar_strings['E6'], tempos['crotchet'] * beat],
                                         [guitar_frets['fret4'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret4'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret4'], guitar_strings['E6'], tempos['quaver'] * beat],
                                         [guitar_frets['fret4'], guitar_strings['E6'], tempos['crotchet'] * beat]]

music_list = {'test': test,
              'Survivor – Eye of the tiger': survivor_eye_of_the_tiger,
              'Queen – We Will Rock You': queen_we_will_rock_you,
              'Batman Theme': batman_theme,
              'AC/DC – Dirty Deeds Done Dirt Cheap': acdc_dirty_deeds_done_dirt_cheap,
              'George Thorogood – Bad to the Bone': george_thorogood_bad_to_the_bone,
              'The Troggs – Wild Thing': the_troggs_wild_thing,
              'Jimi Hendrix – All Along the Watchtower': jimi_hendrix_all_along_the_watchtower,
              'The White Stripes – Seven Nation Army': the_white_stripes_seven_nation_army,
              }
