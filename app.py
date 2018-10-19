"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = [0] * len(line)
    index = 0
    for num in line:
        if(num != 0 and num != result[index]):
            if(result[index] != 0):
                index += 1
                result[index] = num
            else:
                result[index] = num
        elif(num != 0 and num == result[index]):
            result[index] += num
            index += 1
  
    return result     


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._directions = {}
        self.reset()
        self.create_directions_dict()
    
    def create_directions_dict(self):
        """ This function creates a dictionary which stores
        indices for the offsets
        """
        self._directions[UP] = [(0, col)for col in range(self._grid_width)]
        self._directions[DOWN] = [(self._grid_height-1, col)for col in range(self._grid_width)]
        self._directions[LEFT] = [(row, 0) for row in range(self._grid_height)]
        self._directions[RIGHT] = [(row, self._grid_width-1) for row in range(self._grid_height)]
        
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[ 0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile() 
        self.new_tile()
       
       
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        grid = ""
        return grid.join(str(row) + '\n' for row in self._grid)
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if(direction == 1 or direction == 2):
            way = self._grid_height
        else:
            way = self._grid_width
        grid_change = False
        tile_start = self._directions.get(direction)
        off_set = OFFSETS.get(direction)
        # Iterate over the entries of the associate row or columns
        temp_list = []
        
        for tile in tile_start:
            # go in the direction
            for step in range(way):
                row = tile[0] + step * off_set[0]
                col = tile[1] + step * off_set[1]
                temp_list.append(self.get_tile(row, col))
            
            merged_list = merge(temp_list)
            if(self.merge_tiles(merged_list, tile, off_set)):
                grid_change = True
            temp_list = []
        if(grid_change):
            self.new_tile()
    def merge_tiles(self, merged_list, start_tile, off_set):
        """
        This is a helper function for the move method
        it places a merged line into the grid
        """
        put_new_tile = False
        
        for step in range(len(merged_list)):
                row = start_tile[0] + step * off_set[0]
                col = start_tile[1] + step * off_set[1]
                if(self.get_tile(row,col) != merged_list[step]):
                    put_new_tile = True
                    
                self.set_tile(row, col, merged_list[step])
         
        if(put_new_tile):
            return True

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        two_or_four = [2,2,2,2,2,2,2,2,2,4]
        value = random.choice(two_or_four)
       
        row = random.randrange(0, self._grid_height)
        col = random.randrange(0, self._grid_width)
        # In case
        while(self._grid[row][col] != 0):
            row = random.randrange(0, self._grid_height)
            col = random.randrange(0, self._grid_width)
            
        self.set_tile(row, col, value)
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
