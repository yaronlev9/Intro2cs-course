class Car:
    """class that makes the objects of the cars with their attributes
    (name, length,location and orientation) that includes methods."""
    VERTICAL = 0
    HORIZONTAL = 1
    MOVES = ('u', 'd', 'l', 'r')
    UP_MSG = "car can move up"
    DOWN_MSG = "car can move down"
    RIGHT_MSG = "car can move right"
    LEFT_MSG = "car can move left"

    def __init__(self, name, length, location, orientation):
        """ A constructor for a Car object
                param name: A string representing the car's name
                param length: A positive int representing the car's length.
                param location: A tuple representing the car's head (row, col) location
                param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)"""
        self.__name = name
        self.__length = length
        self.__location = tuple(location)
        self.__orientation = orientation

    def car_coordinates(self):
        """ return: A list of coordinates the car is in """
        coordinates=[]
        if self.__orientation==Car.VERTICAL:
            for i in range(self.__length):
                coordinates.append((self.__location[0]+i,self.__location[1]))
            return coordinates
        if self.__orientation == Car.HORIZONTAL:
            for i in range(self.__length):
                coordinates.append((self.__location[0],self.__location[1]+i))
            return coordinates

    def possible_moves(self):
        """ return: A dictionary of strings describing possible movements permitted by this car."""
        poss_moves={}
        if self.__orientation==Car.VERTICAL:
            poss_moves.update({Car.MOVES[0]: Car.UP_MSG})
            poss_moves.update({Car.MOVES[1]: Car.DOWN_MSG})
            return poss_moves
        if self.__orientation==Car.HORIZONTAL:
            poss_moves.update({Car.MOVES[2]: Car.LEFT_MSG})
            poss_moves.update({Car.MOVES[3]: Car.RIGHT_MSG})
            return poss_moves

    def movement_requirements(self, movekey):
        """ param movekey: A string representing the key of the required move.
            return: A list of cell locations which must be empty in order for this move to be legal."""
        coordinates = self.car_coordinates()
        mov_req=[]
        if movekey==Car.MOVES[0]:
            mov_req.append((coordinates[0][0]-1,
                                coordinates[0][1]))
            return mov_req
        if movekey==Car.MOVES[1]:
            mov_req.append((coordinates[-1][0]+1,
                                coordinates[-1][1]))
            return mov_req
        if movekey==Car.MOVES[2]:
            mov_req.append((coordinates[0][0],
                                coordinates[0][1]-1))
            return mov_req
        if movekey==Car.MOVES[3]:
            mov_req.append((coordinates[-1][0],
                                coordinates[-1][1]+1))
            return mov_req

    def move(self, movekey):
        """ param movekey: A string representing the key of the required move.
            return: True upon success, False otherwise """
        if movekey == Car.MOVES[0] and self.__orientation==Car.VERTICAL:
            self.__location = (self.__location[0]-1,self.__location[1])
            return True
        if movekey == Car.MOVES[1] and self.__orientation==Car.VERTICAL:
            self.__location = (self.__location[0]+1,self.__location[1])
            return True
        if movekey == Car.MOVES[2] and self.__orientation==Car.HORIZONTAL:
            self.__location = (self.__location[0], self.__location[1]-1)
            return True
        if movekey == Car.MOVES[3] and self.__orientation==Car.HORIZONTAL:
            self.__location = (self.__location[0], self.__location[1] + 1)
            return True
        return False

    def get_name(self):
        """ return: The name of this car."""
        return self.__name
