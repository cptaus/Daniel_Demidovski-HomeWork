from modules.class_grid import Grid


def greeting():
    print("""
  _______ _   _______      _______         _ 
 |__   __(_) |__   __|    |__   __|       | |
    | |   _  ___| | __ _  ___| | ___   ___| |
    | |  | |/ __| |/ _` |/ __| |/ _ \ / _ \ |
    | |  | | (__| | (_| | (__| | (_) |  __/_|
    |_|  |_|\___|_|\__,_|\___|_|\___/ \___(_)
---------------------------------------------
    Made by Daniel Demidovski (ps never use VIM again)                                                                       
    """)


def pre_game():
    player = input("Please insert first player name: ").strip(), input("Please insert second player name: ").strip()
    grid_size = int(input("Please insert desired game table size 3-9: ").strip())
    game_grid = Grid(grid_size)
    return game_grid, player


def player_move(player_name):
    move_ls = [0, 0]
    print(f"{player_name} Turn!")
    move_ls[0] = int(input(f"{player_name} Please insert column number: ").strip())
    move_ls[1] = int(input(f"{player_name} Please insert row number: ").strip())
    return move_ls


def main():
    turn = 0
    game_end = False
    greeting()
    game_grid, player = pre_game()
    while not game_end:
        print("turn:", turn)
        if turn == int(game_grid.grid_layout+2):
            print("Out of moves!")
            game_end = True
            break
        else:
            for player_now in player:
                if turn % 2 == 0:
                    symbol = "X"
                else:
                    symbol = "O"
                turn += 1
                game_grid.grid_ui_show(player[0], player[1])
                game_grid.player_move(player_move(player_now), symbol)
                if game_grid.grid_checker("X") or game_grid.grid_checker("O"):
                    game_grid.grid_ui_show(player[0], player[1])
                    game_end = True
                    break
