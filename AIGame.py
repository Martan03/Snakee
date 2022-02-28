from typing import Tuple
from Directions import *
from Food import Food
from Snake import Snake

class AIGame:
    def __init__(self,
                 board_size: Tuple[int, int],
                 snake: Snake,
                 food: Food):
        self.board_size = board_size
        self.moves = []
        self.snake = snake
        self.food = food

    def set_input(self, input):
        self.input = input

    # return next snake move
    def get_move(self):
        if len(self.moves) <= 0:
            self.generate_moves()

        if not self.moves:
            return RIGHT

        return self.moves.pop(0)

    # generate path to the food
    def generate_moves(self):
        path = self.__shortest_opt(self.snake, self.food.get_pos()[0])

        if not path:
            return

        moves = []

        for i in range(1, len(path)):
            moves.append(self.__sub_dir(path[i], path[i - 1]))

        self.moves = moves

    # finding shortest path
    def __shortest(self, snake, food):
        queue = [[snake.get_head()]]

        while queue:
            path = queue.pop(0)
            cur_head = path[-1]

            for node in self.__get_neighbours(cur_head):
                if (self.__in_snake(path, node) or
                    not self.__check_boundary(node) or
                    node in path):
                    continue

                next_path = list(path)
                next_path.append(node)
                
                if node == food:
                    return next_path

                queue.append(next_path)
        return []

    # finding shortest path with optimization
    def __shortest_opt(self, snake, food):
        queue = [[snake.get_head()]]
        were_found = []

        while queue:
            path = queue.pop(0)
            cur_head = path[-1]

            for node in self.__get_neighbours(cur_head):
                if (self.__in_snake(path, node) or
                    not self.__check_boundary(node) or
                    node in were_found or
                    node in path):
                    continue

                next_path = list(path)
                next_path.append(node)
                
                if node == food:
                    return next_path
                
                were_found.append(node)
                queue.append(next_path)
        return []

    # get all node neighbours and chech validity
    def __get_neighbours(self, node):
        # getting all neighbours around node
        neighbours = [self.__add_dir(node, (0, 1)),
                      self.__add_dir(node, (1, 0)),
                      self.__add_dir(node, (0, -1)),
                      self.__add_dir(node, (-1, 0))]
        
        # checking validity of neighbours
        for n in neighbours:
            if not self.__check_boundary(n):
                neighbours.remove(n)
                
        return neighbours

    # return if node in snake
    def __in_snake(self, path, node):
        pos = path[::-1] + self.snake.pos[1:]
        return node in pos[:self.snake.length]

    # check if node in boundary
    def __check_boundary(self, node):
        return (0 < node[0] < self.board_size[0] - 1 and
                0 < node[1] < self.board_size[1] - 1)

    # sum two directions / tuples
    def __add_dir(self, dir1, dir2):
        return (dir1[0] + dir2[0], dir1[1] + dir2[1])

    # subtracts two directions / tuples
    def __sub_dir(self, dir1, dir2):
        return (dir1[0] - dir2[0], dir1[1] - dir2[1])
