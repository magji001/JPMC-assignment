def resetSeats():
    rows = "ABCDEFGHIJKLMNOPQRST"

    seatDict = {
        0 : "E",
        1 : "E",
        2 : "E",
        3 : "E",
        4 : "E",
        5 : "E",
        6 : "E",
    }

    initialSeats = {}

    for letter in rows:
        initialSeats[letter] = seatDict

    with open("seats.txt", 'w') as f:
        f.write('%s' % initialSeats)