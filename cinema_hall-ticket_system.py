class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_hall(self)
        
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['0' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seats_book):
        if show_id in self._seats:
            for row, col in seats_book:

                if 0<= row < self._rows and 0<= col < self._cols:
                    if self._seats[show_id][row][col] == '0':
                        self._seats[show_id][row][col] = '1'
                    else:
                        print(f'seat {row}{col} is already booked')
                else:
                    print(f'Invalid seat number {row}{col}')
        else:
            print(f'Invalid Show Id.')

    def view_show_list(self):
        print(f'Id\tMovie Name\tTime')
        for view in self._show_list:
            print(f'{view[0]}\t{view[1]}\t{view[2]}')

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            for i in range(self._rows):
                for j in range(self._cols):
                    print(self._seats[show_id][i][j], end = " ")
                print()
        else:
            print('Invalid Show Id')



cinema = Star_Cinema()
hall1 = Hall(5, 5, 1)
hall1.entry_show('1', 'Avengers', '10:00 AM')
hall1.entry_show('2', "Jawan   ", '3:30 PM')

while True:
    print('---- Welcome to cinema ticket Bookinf System!! -----')
    print('1. View running shows')
    print('2. View Available seats')
    print('3. Book Ticket')
    print('4. Exit')

    choice = int(input('Enter your choice : '))

    if choice == 1:
        hall1.view_show_list()

    elif choice == 2:
        show_id = input('Enter Show ID : ')
        hall1.view_available_seats(show_id)
    
    elif choice == 3:
        show_id = input('Enter Show ID : ')
        n = int(input('How many tickets you want : '))
        for _ in range(n):
            seats_str = input('Enter seat number (row,col)-> max(4,4) : ')
            seats_to_book = [tuple(map(int, seats_str.split(','))) ]
            hall1.book_seats(show_id, seats_to_book)
    
    elif choice == 4:
        print('Thanks for using out Service!!')
        break
    else:
        print('Invalid choice')
    print()