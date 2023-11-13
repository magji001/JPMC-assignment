import sys
import ast

def bookAction(row, seatNumber, totalSeats):

    for i in range(seatNumber, seatNumber+totalSeats):
        if seats[row][i] == 'B':
            print("FAIL")
            return
        else:
            seats[row][i] = "B"

    with open("seats.txt", 'w') as f:
        f.write('%s' % seats)

    print("SUCCESS")

def cancelAction(row, seatNumber, totalSeats):

    for i in range(seatNumber, seatNumber+totalSeats):
        if seats[row][i] == 'E':
            print("FAIL")
            return
        else:
            seats[row][i] = "E"

    with open("seats.txt", 'w') as f:
        f.write('%s' % seats)

    print("SUCCESS")

## Booking action
def updateSeats(inputAction, startingSeat, totalSeats):
    row = startingSeat[0]
    seatNumber = int(startingSeat[1])

    if inputAction == "BOOK":
        bookAction(row, seatNumber, totalSeats)

    elif inputAction == "CANCEL":
        cancelAction(row, seatNumber, totalSeats)

    else:
        return "FAIL"


if __name__ == "__main__":
    with open('seats.txt') as f:
        seats = ast.literal_eval(f.read())
    try:
        inputAction = sys.argv[1]
        startingSeat = sys.argv[2]
        totalSeats = int(sys.argv[3])
        updateSeats(inputAction, startingSeat, totalSeats)
    except:
        print("FAIL")

