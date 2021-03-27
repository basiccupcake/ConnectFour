print("\n \n \n \n \n Hello! Welcome to Joshua's ConnectFour!")

game_won = None
lst = []
grid = """

 •••••••••••••••••••••••••••••••••••••••••••
6•     •     •     •     •     •     •     •
6•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
5•     •     •     •     •     •     •     •
5•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
4•     •     •     •     •     •     •     •
4•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
3•     •     •     •     •     •     •     •
3•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
2•     •     •     •     •     •     •     •
2•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
1•     •     •     •     •     •     •     •
1•     •     •     •     •     •     •     •
 •••••••••••••••••••••••••••••••••••••••••••
    AA    BB    CC    DD    EE    FF    GG
"""
print(grid)

def invalid():
    print("Invalid choice")
    xy = input("Input your choice again eg: A2, F5 \n")
    while len(xy) != 2:
        x, y, xy = invalid()
    x, y= ord((xy[0]).upper()), int(xy[1])
    return x, y, xy

def xchoice():
    xy = input("X's turn:")
    while len(xy) != 2:
        x, y, xy = invalid()
    x, y= ord((xy[0]).upper()), int(xy[1])
    return x, y, xy

def ochoice():
    xy = input("O's turn:")
    while len(xy) != 2:
        x, y, xy = invalid()
    x, y= ord((xy[0]).upper()), int(xy[1])
    return x, y, xy

def reverse(y):
    reverse_list = [0, 6, 5, 4, 3, 2, 1]
    return reverse_list[y]

print(reverse(6))
def convert_x(x):
    return x - 64 + ((x - 64 - 1) * 5) + 4

def convert_y1(y):
    return 45*reverse(y) + 45*(reverse(y)-1)*2

def convert_y2(y):
    return 45*reverse(y)+45 + 45*(reverse(y)-1)*2

def update_grid_x(grid, x, y):
    grid = grid[:convert_x(x) + convert_y1(y)] + "XXX" + grid[convert_x(x) + convert_y1(y) + 3:convert_x(x) + convert_y2(y)] + "XXX" + grid[convert_x(x) + convert_y2(y) + 3:]
    return grid

def update_grid_o(grid, x, y):
    grid = grid[:convert_x(x) + convert_y1(y)] + "OOO" + grid[convert_x(x) + convert_y1(y) + 3:convert_x(x) + convert_y2(y)] + "OOO" + grid[convert_x(x) + convert_y2(y) + 3:]
    return grid

def check_game_won():
    X_or_O = ""
    for x in range(65,68):
        for y in range(1,7):
            X_or_O = grid[convert_x(x) + convert_y1(y)]
            if X_or_O == 'X' or X_or_O == 'O':
                if X_or_O == grid[convert_x(x) + convert_y1(y) + 6] and X_or_O == grid[convert_x(x) + convert_y1(y) + 12] and X_or_O == grid[convert_x(x) + convert_y1(y) + 18]:
                    print("{} won!".format(X_or_O))
                    return True
    for x in range(65,72):
        for y in range(1,4):
            X_or_O = grid[convert_x(x) + convert_y1(y)]
            if X_or_O == 'X' or X_or_O == 'O':
                if X_or_O == grid[convert_x(x) + convert_y1(y) - 135] and X_or_O == grid[convert_x(x) + convert_y1(y) - 270] and X_or_O == grid[convert_x(x) + convert_y1(y) - 405]:
                    print("{} won!".format(X_or_O))
                    return True
    for x in range(65,69):
        for y in range(1,4):
            X_or_O = grid[convert_x(x) + convert_y1(y)]
            if X_or_O == 'X' or X_or_O == 'O':
                if X_or_O == grid[convert_x(x) + convert_y1(y) - 135 + 6] and X_or_O == grid[convert_x(x) + convert_y1(y) - 270 + 12] and X_or_O == grid[convert_x(x) + convert_y1(y) - 405 + 18]:
                    print("{} won!".format(X_or_O))
                    return True
    for x in range(68,72):
        for y in range(1,4):
            X_or_O = grid[convert_x(x) + convert_y1(y)]
            if X_or_O == 'X' or X_or_O == 'O':
                if X_or_O == grid[convert_x(x) + convert_y1(y) - 135 - 6] and X_or_O == grid[convert_x(x) + convert_y1(y) - 270 - 12] and X_or_O == grid[convert_x(x) + convert_y1(y) - 405 - 18]:
                    print("{} won!".format(X_or_O))
                    return True
     

                    


while game_won == None:
    x = 0
    y = 0
    cond = False
    x, y ,xy = xchoice()
    while cond == False:
        cond = True
        if len(xy) != 2:
            print("Length")
            x, y, xy = invalid()
            cond = False

        if x <= 64 or x >= 72:
            print("x")
            x, y, xy = invalid()
            cond = False

        if y <= 0 or y >= 7:
            print("y")
            x, y, xy = invalid()
            cond = False

        if xy.upper() in lst:
            print("xy")
            x, y, xy= invalid()
            cond = False

        try:
            modcond = (grid[convert_x(x) + convert_y1(y) + 135] != "X" and grid[convert_x(x) + convert_y1(y) + 135] != "O")
            if grid[convert_x(x) + convert_y1(y) + 135] != "X" and grid[convert_x(x) + convert_y1(y) + 135] != "O":
                if cond == True:
                    if y == 1:
                        break
                print("The square below is unfilled")
                x, y, xy = invalid()
                cond = False
        except IndexError:
            cond = False

    
    grid = update_grid_x(grid, x, y)
    print(grid)
    print(grid[convert_x(x) + convert_y1(y) + 135])
    lst.append(xy.upper())

    game_won = check_game_won()
    if game_won == True:
        break


    x, y, xy = ochoice()
    cond = False
    while cond == False:
        cond = True
        if len(xy) != 2:
            print("Length")
            x, y, xy = invalid()
            cond = False

        if x <= 64 or x >= 72:
            print("x")
            x, y, xy = invalid()
            cond = False

        if y <= 0 or y >= 7:
            print("y")
            x, y, xy = invalid()
            cond = False

        if xy.upper() in lst:
            print("xy")
            x, y, xy= invalid()
            cond = False

        try:
            modcond = (grid[convert_x(x) + convert_y1(y) + 135] != "X" and grid[convert_x(x) + convert_y1(y) + 135] != "O")
            if grid[convert_x(x) + convert_y1(y) + 135] != "X" and grid[convert_x(x) + convert_y1(y) + 135] != "O":
                if cond == True:
                    if y == 1:
                        break
                print("The square below is unfilled")
                x, y, xy = invalid()
                cond = False
        except IndexError:
            cond = False


    grid = update_grid_o(grid, x, y)
    print(grid)
    print(grid[convert_x(x) + convert_y1(y) + 135])
    lst.append(xy.upper())

    game_won = check_game_won()

print('I hope you had fun!')