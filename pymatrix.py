from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        find_initial_border(matrix)
        pass
        
def invert_values(lol):
    return [[-x for x in sublist] for sublist in lol]

def pyramid(listoflists):
    lol = invert_values(listoflists)
    matrix = PyMatrix(lol)
    border = find_initial_border(matrix)
    last_value = 1
    while len(border) > 0:
        border = find_next_border(matrix, border, last_value)
        last_value += 1
    print(matrix.matrix)

def find_initial_border(matrix):
    border = []
    for x in range(matrix.dimensions[0]):
        for y in range(matrix.dimensions[1]):
            neighbors = matrix.get_neighbors((x, y))
            neighbor_zeros = [True if n == 0 else False for n in neighbors.values()]
            if any(neighbor_zeros) and matrix[x, y] != 0:
                border.append([x, y])
                matrix[x, y] == 1
    return border

def find_next_border(matrix, last_border, last_value):
    new_border = []
    for position in last_border: 
        neighbors = matrix.get_neighbors(position)
        unset_neighbors = {position for position, value in neighbors.keys()
                if value == -1}
        new_border.append(unset_neighbors)
    new_border = set(new_border)
    for position in new_border:
        matrix[position] = last_value + 1
    return new_border 

class PyMatrix:
    def __init__(self, listoflists):
        self.matrix = listoflists
        try:
            self.dimensions = (len(listoflists), len(listoflists[0]))
        except TypeError:
            self.dimensions = (len(listoflists), 1)
    
    def __getitem__(self, position):
        row_index, column_index = position
        if self.__out_of_bounds__(position):
            raise IndexError("Accessed matrix out of bounds")
        row = self.matrix[row_index]
        value = row[column_index]
        return value
    
    def __setitem__(self, position, value):
        row_index, column_index = position
        row = self.matrix[row_index]
        row[column_index] = value
        
    def __out_of_bounds__(self, position):
        return out_of_bounds_position(position, self.matrix)
    
    def get_neighbors(self, position):
        positions = get_neighbor_positions(position, self.matrix)
        values = [self[position] for position in positions]
        result = dict(zip(positions, values))
        return result
    
def get_neighbor_positions(position, matrix):
    i = position[0]
    j = position[1]
    neighbors = []
    if out_of_bounds_position(position, matrix):
        raise IndexError("getting neighbors for position outside of matrix")
    for x_offset, y_offset in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            new_position = i + x_offset, j + y_offset
            if not out_of_bounds_position(new_position, matrix):
                neighbors.append(new_position)
    return neighbors

def out_of_bounds_position(position, matrix):
    """Checks whether a position is out of bounds for the 'matrix'."""
    x, y = position
    return (out_of_bounds(x, len(matrix)) or out_of_bounds(y, len(matrix)))
            
def out_of_bounds(i, N):
    """
    Checks if given i,j coordinates are inside the array, because this is some horrible list of list thing.
    """
    return (i < 0) or (i >= N)
    # Iterate over matrix elements:
    # 1) Check if zero and not all neighbors zero
    # 2) Add to boundary list
    
    # List of list: matrix[i][j] -> element
        
