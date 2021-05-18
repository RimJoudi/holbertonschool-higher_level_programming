#!/usr/bin/python3
class Square:
    
    @property 
    def size(self):
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
    @property
    def position(self):
        return (self.__position)
    
    
    @position.setter 
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or type(value[1])!= int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0 or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position
            
              
        
    def area(self):
        return (self.__size ** 2)
        
          
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(0, self.__size):
                    print("#", end="")
                print() 

