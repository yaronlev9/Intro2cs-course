class Board:
    """class that makes the objects of the board with it's attributes (height,width,car_lst)
    that includes methods."""
    MOVES = ('u', 'd', 'l', 'r')
    LINE = '-'
    UP_MSG = "car can move up"
    DOWN_MSG = "car can move down"
    RIGHT_MSG = "car can move right"
    LEFT_MSG = "car can move left"
    VERTICAL = 0
    HORIZONTAL = 1
    def __init__(self):
        self.__height=7
        self.__width=7
        self.__car_lst=[]

    def __str__(self):
        """ This function is called when a board object is to be printed.
            return: A string of the current status of the board"""
        board=''
        for row in range(self.__height):
            for col in range(self.__width):
                cell = self.cell_content((row,col))
                if cell is None:
                    board+=Board.LINE
                else:
                    board+=cell
                if row==3 and col==6:
                    board+='E'
            board+='\n'
        return board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
            return: list of coordinates"""
        cell_lst=[]
        for row in range(self.__height):
            for col in range(self.__width):
                cell_lst.append((row,col))
        cell_lst.append((3,7))
        return cell_lst

    def filled_cells(self):
        filled_cells=[]
        for car in self.__car_lst:
            coordinates = car.car_coordinates()
            for coordinate in coordinates:
                if coordinate not in filled_cells:
                    filled_cells.append(coordinate)
        return filled_cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
            return: list of tuples of the form (name,movekey,description)
            representing legal moves"""
        lst=[]
        for car in self.__car_lst:
            possible_moves = car.possible_moves()
            coordinates = car.car_coordinates()
            for move in possible_moves:
                required_coordinate = car.movement_requirements(move)
                if self.cell_content(required_coordinate[0]) != None:
                    continue
                if move == Board.MOVES[0] and coordinates[0][0]>0:
                        lst.append((car.get_name(),move,possible_moves[move]))
                if move == Board.MOVES[1] and coordinates[-1][0]<self.__height-1:
                    lst.append((car.get_name(),move,possible_moves[move]))
                if move == Board.MOVES[2] and coordinates[0][1]>0:
                    lst.append((car.get_name(),move,possible_moves[move]))
                if move == Board.MOVES[3] and (coordinates[-1][1]<self.__width-1 or coordinates[-1] == (3,6)):
                    lst.append((car.get_name(),move,possible_moves[move]))
        return lst

    def target_location(self):
        """This function returns the coordinates of the location which is to be filled for victory.
        return: (row,col) of goal location"""
        return (3,7)

    def cell_content(self, coordinate):
        """Checks if the given coordinates are empty.
            param coordinate: tuple of (row,col) of the coordinate to check
            return: The name if the car in coordinate, None if empty"""
        for car in self.__car_lst:
            car_cells = car.car_coordinates()
            if coordinate in car_cells:
                return car.get_name()
        return None

    def add_car(self, car):
        """ Adds a car to the game.
            param car: car object of car to add
            return: True upon success. False if failed"""
        filled_cells=self.filled_cells()
        for vehicle in self.__car_lst:
            if car.get_name() == vehicle.get_name():
                return False
        car_cells=car.car_coordinates()
        for cell in car_cells:
            if cell[0]>self.__height-1 or cell[0]<0 or cell[1]>self.__width-1 or cell[1]<0 or cell in filled_cells:
                return False
        self.__car_lst.append(car)
        return True

    def move_car(self, name, movekey):
        """ moves car one step in given direction.
            param name: name of the car to move
            param movekey: Key of move in car to activate
            return: True upon success, False otherwise"""
        for car in self.__car_lst:
            if car.get_name()==name:
                coordinate = car.movement_requirements(movekey)
                if self.cell_content(coordinate[0]) is None:
                    if movekey == Board.MOVES[0] and coordinate[0][0]>=0:
                        car.move(movekey)
                        return True
                    if movekey == Board.MOVES[1] and coordinate[0][0]<=self.__height-1:
                        car.move(movekey)
                        return True
                    if movekey == Board.MOVES[2] and coordinate[0][1]>=0:
                        car.move(movekey)
                        return True
                    if movekey == Board.MOVES[3] and (coordinate[0][1] <= self.__width - 1 or coordinate[0] == (3,7)):
                        car.move(movekey)
                        return True
        return False

