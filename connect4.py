class Player:
    def __init__(self, name, x, y) -> None:
        self.name = name 
        self.x = x 
        self.y = y 
    
    def get_name(self):
        return self.name
    
    def get_coordinates(self):
        return self.x, self.y 

class Grid:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(self.cols)] for _  in range(self.rows)]
    
    def set_grid(self, player, x, y):
        res = 0
        if player == "X": res = 1
        elif player == "Y": res = 2
        if self.grid[x][y] == 0: 
            self.grid[x][y] = res
        else:
            print("incorrect move")
            return
    
    def check_consecutive(self, value, r, c, dr, dc):
        count = 0
        while r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.grid[r][c] == value:
            count += 1
            r += dr
            c += dc
        return count >= 4
    
    def predict_win(self, value, r, c):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  
        
        for dr, dc in directions:
            if self.check_consecutive(value, r, c, dr, dc):
                return True
        return False
        
    def check_win(self, player):
        res = 0
        if player == "X": res = 1
        else: res = 2

        for r in range(self.rows):
            for c in range(self.cols):
                if self.predict_win(res, r, c): return True 
        return False    


#moves = [["X", 1, 0], ["X", 2, 0], ["X", 3, 0], ["X", 4, 0]]
moves = [Player("X", 1, 0), Player("X", 2, 0), Player("X", 3, 0), Player("X", 4, 0)]
class Connect4:
    def __init__(self, moves, rows, cols) -> None:
        self.moves = moves
        self.rows = rows 
        self.cols = cols
    def play(self):
        grid = Grid(self.rows, self.cols)
        for m in self.moves:
            x, y = m.get_coordinates()
            grid.set_grid(m.name, x, y)
        if grid.check_win("X"): return "Player X wins"
        else: return "Player Y wins"

connect4 = Connect4(moves, 6, 6)
print(connect4.play())
        