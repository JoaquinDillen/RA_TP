from py_openshowvar import openshowvar


def send_points_to_kuka(points):
    print(f'Points: {points}')
    # connect to kuka
    client = openshowvar("192.168.10.254", 7000)

    # write points to kuka
    for i, point in enumerate(points, start=1):
        # write guitar fret variable
        client.write(f'POINTS[{i}].POINT.X', f'{point[0]}', debug=False)
        # write guitar string variable
        client.write(f'POINTS[{i}].POINT.Y', f'{point[1]}', debug=False)
        # write tempo variable
        client.write(f'POINTS[{i}].TEMPO', f'{point[2]}', debug=False)

    # give start order to kuka
    client.write('KUSTIC_START', 'TRUE', debug=False)

    # close connection with kuka
    client.close()


def send_stop_order_to_kuka():
    # connect to kuka
    client = openshowvar("192.168.10.254", 7000)

    # reset stop order
    client.write('KUSTIC_STOP', 'TRUE', debug=False)

    # close connection with kuka
    client.close()
