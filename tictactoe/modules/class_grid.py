class Grid:
    """MAIN CLASS FOR THE GAME
        METHODS:
            create_grid: Building 2d list
            grid_ui_show: Checking and showing table to the user
            player_move: method for updating the table with players moves
            check_board_row/col/dig: checking methods to see if one of the players wins
        PARAMS:
            grid_layout: size of the table
            grid: 2d list holder for the table
    """
    def __init__(self, num):
        """num: wanted number of table columns (table = num*num)"""
        self.grid_layout = num
        self.grid = []
        self.create_grid()

    def create_grid(self):
        """creating grid from the chosen num in Grid.__init__"""
        row = []
        for cell in range(self.grid_layout):
            for cell_d in range(self.grid_layout):
                row.append("-")
            self.grid.append(row.copy())
            row.clear()

    def grid_ui_show(self, player_1, player_2):
        """Main UI method"""
        counter = 0
        print()
        print(f"X-{player_1} vs O-{player_2}:")
        for row in self.grid:
            for cell in row:
                if counter == self.grid_layout:
                    counter = 0
                    print()
                if counter == self.grid_layout-1:
                    print(cell, end="")
                else:
                    print(cell, end="|")
                counter += 1
        print("\n")

    def player_move(self, place: list, player_symbol: str):
        """Method to use for updating table when player make a move"""
        self.grid[place[0]-1][place[1]-1] = player_symbol

    def grid_checker(self, symbol):
        """method to organize 1 check"""
        if self.check_board_row(symbol) or self.check_board_col(symbol) or self.check_board_dig(symbol):
            return True

    def check_board_row(self, symbol: str):
        """check if player won on 1 row"""
        symbol = symbol
        grid_in = 0
        count = 0
        for cell in range(len(self.grid)):
            for in_cell in range(len(self.grid[cell])):
                if self.grid[grid_in][in_cell] == symbol:
                    # print(grid_in, self.grid[grid_in].index(symbol))
                    count += 1
                    continue
                count = 0
            if count == self.grid_layout:
                print(f"{symbol} Wins!")
                return True
            grid_in += 1

    def check_board_col(self, symbol: str):
        """check if player won on 1 column"""
        symbol = symbol
        grid_in = 0
        count = 0
        for cell in range(len(self.grid)):
            for in_cell in range(len(self.grid[cell])):
                if self.grid[in_cell][grid_in] == symbol:
                    count += 1
                    continue
                count = 0
            if count == self.grid_layout:
                print(f"{symbol} Wins!")
                return True
            grid_in += 1

    def check_board_dig(self, symbol: str):
        symbol = symbol
        count = 0
        count_rev = self.grid_layout-1
        for row in self.grid:
            if row[count] == symbol:
                count += 1
            if count == self.grid_layout:
                return True
            if row[count_rev] == symbol:
                count_rev -= 1
            if count_rev == -1:
                return True

