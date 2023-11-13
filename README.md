# JPMC-assignment
## Author - Henri Magjistari

### Description
The project simulates an airline seat reservation system, where users can book or cancel seats based on seat avaiability provided at runtime via CLI arguments.

### Initial Setup
Since the application is run by executing the airplane_seats.sh script, the appropriate permissions might need to be given to the script. To do so, run the following command in the main project directory:
`chmod u+x airplane_seats.sh`

### Running the application
The above script is used to run the application. The appropriate command is passed as CLI argument, in the following format:
`[Action] [Starting Seat] [Number of consecutive seats]`

Where Action can be either `BOOK` or `CANCEL`. The entire output is passed without quotes or special characters, for example: 

`BOOK B2 2`

### Resetting the Seats
Each application run will update the seats.txt file. To allow users the ability to reset the seats, I added the seatInitializer.py file, which has the resetSeats() function that empties all seats. Users can call this function at any time to empty all seats. 

