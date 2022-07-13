import enum
import time
import cv2
from py_openshowvar import openshowvar


# creating guitar string enumerations using class
class GuitarStrings(enum.Enum):
    E1 = 10
    A2 = 20
    D3 = 30
    G4 = 40
    B5 = 50
    E6 = 60


# creating guitar string enumerations using class
class GuitarFrets(enum.Enum):
    fret1 = 10
    fret2 = 20
    fret3 = 30
    fret4 = 40
    fret5 = 50
    fret6 = 60
    fret7 = 70
    fret8 = 80
    fret9 = 90
    fret10 = 100
    fret11 = 110
    fret12 = 120
    fret13 = 130
    fret14 = 140
    fret15 = 150
    fret16 = 160
    fret17 = 170
    fret18 = 180


def main():
    # connect to kuka
    client = openshowvar("192.168.10.254", 7000)

    # initialize music array
    music = [[GuitarFrets.fret1.value, GuitarStrings.E1.value, 1],
             [GuitarFrets.fret1.value, GuitarStrings.A2.value, 2],
             [GuitarFrets.fret1.value, GuitarStrings.D3.value, 3],
             [GuitarFrets.fret1.value, GuitarStrings.G4.value, 4],
             [GuitarFrets.fret1.value, GuitarStrings.B5.value, 5],
             [GuitarFrets.fret1.value, GuitarStrings.E6.value, 6]]
    
    # write points to kuka
    for i, note in enumerate(music):
        # write guitar fret variable
        client.write(f'POINTS[{i}].POINT.X', f'{note[0]}')
        # write guitar string variable
        client.write(f'POINTS[{i}].POINT.Y', f'{note[1]}')

    client.write('KUSTIC_START', 'TRUE')

    client.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
