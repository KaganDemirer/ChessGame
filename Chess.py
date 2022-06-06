import pygame

screen_x = 399
screen_y = 399

selected = []

options = []

grid = [[0 for x in range(0, screen_x, 50)] for y in range(screen_y//50+1)]

class Rook:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "Rook"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        for hor in range(self.x+1,8):
            if grid[self.y][hor] == 0:
                possibilities.append([self.y, hor])
            else:
                if grid[self.y][hor].team != self.team:
                    possibilities.append([self.y, hor])
                break
        for hor in range(self.x-1,-1,-1):
            if grid[self.y][hor] == 0:
                possibilities.append([self.y, hor])
            else:
                if grid[self.y][hor].team != self.team:
                    possibilities.append([self.y, hor])
                break
        for ver in range(self.y+1,8):
            if grid[ver][self.x] == 0:
                possibilities.append([ver, self.x])
            else:
                if grid[ver][self.x].team != self.team:
                    possibilities.append([ver, self.x])
                break
        for ver in range(self.y-1,-1,-1):
            if grid[ver][self.x] == 0:
                possibilities.append([ver, self.x])
            else:
                if grid[ver][self.x].team != self.team:
                    possibilities.append([ver, self.x])
                break
        return possibilities

    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self

class Knight:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "Knight"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        try:
            if self.y -2 >= 0:
                if grid[self.y-2][self.x+1] == 0:
                    possibilities.append([self.y-2, self.x+1])
                else:
                    if grid[self.y-2][self.x+1].team != self.team:
                        possibilities.append([self.y-2, self.x+1])
        except:
            pass
        try:
            if self.y -2 >= 0 and self.x -1 >= 0:
                if grid[self.y-2][self.x-1] == 0:
                    possibilities.append([self.y-2, self.x-1])
                else:
                    if grid[self.y-2][self.x-1].team != self.team:
                        possibilities.append([self.y-2, self.x-1])
        except:
            pass
        try:
            if grid[self.y+2][self.x+1] == 0:
                possibilities.append([self.y+2, self.x+1])
            else:
                if grid[self.y+2][self.x+1].team != self.team:
                    possibilities.append([self.y+2, self.x+1])
        except:
            pass
        try:
            if self.x -1 >= 0:
                if grid[self.y+2][self.x-1] == 0:
                    possibilities.append([self.y+2, self.x-1])
                else:
                    if grid[self.y+2][self.x-1].team != self.team:
                        possibilities.append([self.y+2, self.x-1])
        except:
            pass
        try:
            if self.y -1 >= 0:
                if grid[self.y-1][self.x+2] == 0:
                    possibilities.append([self.y-1, self.x+2])
                else:
                    if grid[self.y-1][self.x+2].team != self.team:
                        possibilities.append([self.y-1, self.x+2])
        except:
            pass
        try:
            if self.x -2 >= 0 and self.y -1 >= 0:
                if grid[self.y-1][self.x-2] == 0:
                    possibilities.append([self.y-1, self.x-2])
                else:
                    if grid[self.y-1][self.x-2].team != self.team:
                        possibilities.append([self.y-1, self.x-2])
        except:
            pass
        try:
            if grid[self.y+1][self.x+2] == 0:
                possibilities.append([self.y+1, self.x+2])
            else:
                if grid[self.y+1][self.x+2].team != self.team:
                    possibilities.append([self.y+1, self.x+2])
        except:
            pass
        try:
            if self.x -2 >= 0:
                if grid[self.y+1][self.x-2] == 0:
                    possibilities.append([self.y+1, self.x-2])
                else:
                    if grid[self.y+1][self.x-2].team != self.team:
                        possibilities.append([self.y+1, self.x-2])
        except:
            pass
        return possibilities

    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self

class Bishop:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "Bishop"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        for hor in range(1,8):
            if self.x + hor > 7 or self.y + hor > 7:
                break
            if grid[self.y+hor][self.x+hor] == 0:
                possibilities.append([self.y+hor, self.x+hor])
            else:
                if grid[self.y+hor][self.x+hor].team != self.team:
                    possibilities.append([self.y+hor, self.x+hor])
                break

        for hor in range(1,8):
            if self.x - hor < 0 or self.y - hor < 0:
                break
            if grid[self.y-hor][self.x-hor] == 0:
                possibilities.append([self.y-hor, self.x-hor])
            else:
                if grid[self.y-hor][self.x-hor].team != self.team:
                    possibilities.append([self.y-hor, self.x-hor])
                break

        for hor in range(1,8):
            if self.x + hor > 7 or self.y - hor < 0:
                break
            if grid[self.y-hor][self.x+hor] == 0:
                possibilities.append([self.y-hor, self.x+hor])
            else:
                if grid[self.y-hor][self.x+hor].team != self.team:
                    possibilities.append([self.y-hor, self.x+hor])
                break

        for hor in range(1,8):
            if self.x - hor < 0 or self.y + hor > 7:
                break
            if grid[self.y+hor][self.x-hor] == 0:
                possibilities.append([self.y+hor, self.x-hor])
            else:
                if grid[self.y+hor][self.x-hor].team != self.team:
                    possibilities.append([self.y+hor, self.x-hor])
                break
        return possibilities


    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self

class Queen:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "Queen"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        for hor in range(1,8):
            if self.x + hor > 7 or self.y + hor > 7:
                break
            if grid[self.y+hor][self.x+hor] == 0:
                possibilities.append([self.y+hor, self.x+hor])
            else:
                if grid[self.y+hor][self.x+hor].team != self.team:
                    possibilities.append([self.y+hor, self.x+hor])
                break

        for hor in range(1,8):
            if self.x - hor < 0 or self.y - hor < 0:
                break
            if grid[self.y-hor][self.x-hor] == 0:
                possibilities.append([self.y-hor, self.x-hor])
            else:
                if grid[self.y-hor][self.x-hor].team != self.team:
                    possibilities.append([self.y-hor, self.x-hor])
                break

        for hor in range(1,8):
            if self.x + hor > 7 or self.y - hor < 0:
                break
            if grid[self.y-hor][self.x+hor] == 0:
                possibilities.append([self.y-hor, self.x+hor])
            else:
                if grid[self.y-hor][self.x+hor].team != self.team:
                    possibilities.append([self.y-hor, self.x+hor])
                break

        for hor in range(1,8):
            if self.x - hor < 0 or self.y + hor > 7:
                break
            if grid[self.y+hor][self.x-hor] == 0:
                possibilities.append([self.y+hor, self.x-hor])
            else:
                if grid[self.y+hor][self.x-hor].team != self.team:
                    possibilities.append([self.y+hor, self.x-hor])
                break

        for hor in range(self.x+1,8):
            if grid[self.y][hor] == 0:
                possibilities.append([self.y, hor])
            else:
                if grid[self.y][hor].team != self.team:
                    possibilities.append([self.y, hor])
                break
        for hor in range(self.x-1,-1,-1):
            if grid[self.y][hor] == 0:
                possibilities.append([self.y, hor])
            else:
                if grid[self.y][hor].team != self.team:
                    possibilities.append([self.y, hor])
                break
        for ver in range(self.y+1,8):
            if grid[ver][self.x] == 0:
                possibilities.append([ver, self.x])
            else:
                if grid[ver][self.x].team != self.team:
                    possibilities.append([ver, self.x])
                break
        for ver in range(self.y-1,-1,-1):
            if grid[ver][self.x] == 0:
                possibilities.append([ver, self.x])
            else:
                if grid[ver][self.x].team != self.team:
                    possibilities.append([ver, self.x])
                break
        return possibilities


    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self

class King:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "King"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        try:
            if grid[self.y+1][self.x] == 0:
                possibilities.append([self.y+1, self.x])
            else:
                if grid[self.y+1][self.x].team != self.team:
                    possibilities.append([self.y+1, self.x])
        except:
            pass
        try:
            if self.y > 0:
                if grid[self.y-1][self.x] == 0:
                    possibilities.append([self.y-1, self.x])
                else:
                    if grid[self.y-1][self.x].team != self.team:
                        possibilities.append([self.y-1, self.x])
        except:
            pass
        try:
            if grid[self.y][self.x+1] == 0:
                possibilities.append([self.y, self.x+1])
            else:
                if grid[self.y][self.x+1].team != self.team:
                    possibilities.append([self.y, self.x+1])
        except:
            pass
        try:
            if self.x > 0:
                if grid[self.y][self.x-1] == 0:
                    possibilities.append([self.y, self.x-1])
                else:
                    if grid[self.y][self.x-1].team != self.team:
                        possibilities.append([self.y, self.x-1])
        except:
            pass
        try:
            if grid[self.y+1][self.x+1] == 0:
                possibilities.append([self.y+1, self.x+1])
            else:
                if grid[self.y+1][self.x+1].team != self.team:
                    possibilities.append([self.y+1, self.x+1])
        except:
            pass
        try:
            if self.y > 0 and self.x > 0:
                if grid[self.y-1][self.x-1] == 0:
                    possibilities.append([self.y-1, self.x-1])
                else:
                    if grid[self.y-1][self.x-1].team != self.team:
                        possibilities.append([self.y-1, self.x-1])
        except:
            pass
        try:
            if self.y-1 > 0 :
                if grid[self.y-1][self.x+1] == 0:
                    possibilities.append([self.y-1, self.x+1])
                else:
                    if grid[self.y-1][self.x+1].team != self.team:
                        possibilities.append([self.y-1, self.x+1])
        except:
            pass
        try:
            if self.x - 1 > 0:
                if grid[self.y+1][self.x-1] == 0:
                    possibilities.append([self.y+1, self.x-1])
                else:
                    if grid[self.y+1][self.x-1].team != self.team:
                        possibilities.append([self.y+1, self.x-1])
        except:
            pass
        return possibilities


    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self

class Pawn:
    def __init__(self, y,x, team):
        self.x = x
        self.y = y
        self.type = "Pawn"
        self.team = team
        self.image = pygame.image.load(f"pics/{self.type}_{team}.png")
        grid[self.y][self.x] = self

    def get_options(self):
        possibilities = []
        if self.team == "black":
            if self.y == 1:
                if grid[self.y+1][self.x] == 0:
                    possibilities.append([self.y+1, self.x])
                if grid[self.y+2][self.x] == 0 and grid[self.y+1][self.x] == 0:
                    possibilities.append([self.y+2, self.x])
            else:
                if grid[self.y+1][self.x] == 0:
                    possibilities.append([self.y+1, self.x])
        else:
            if self.y == 6:
                if grid[self.y-1][self.x] == 0:
                    possibilities.append([self.y-1, self.x])
                if grid[self.y-2][self.x] == 0 and grid[self.y-1][self.x] == 0:
                    possibilities.append([self.y-2, self.x])
            else:
                if grid[self.y-1][self.x] == 0:
                    possibilities.append([self.y-1, self.x])
        if self.team == "black":
            if self.y == 1:
                try:
                    if grid[self.y+1][self.x+1] != 0:
                        if grid[self.y+1][self.x+1].team != self.team:
                            possibilities.append([self.y+1, self.x+1])
                except:
                    pass
                try:
                    if grid[self.y+1][self.x-1] != 0:
                        if grid[self.y+1][self.x-1].team != self.team:
                            possibilities.append([self.y+1, self.x-1])
                except:
                    pass
            else:
                try:
                    if grid[self.y+1][self.x+1] != 0:
                        if grid[self.y+1][self.x+1].team != self.team:
                            possibilities.append([self.y+1, self.x+1])
                except:
                    pass
                try:
                    if grid[self.y+1][self.x-1] != 0:
                        if grid[self.y+1][self.x-1].team != self.team:
                            possibilities.append([self.y+1, self.x-1])
                except:
                    pass
        else:
            if self.y == 6:
                try:
                    if grid[self.y-1][self.x+1] != 0:
                        if grid[self.y-1][self.x+1].team != self.team:
                            possibilities.append([self.y-1, self.x+1])
                except:
                    pass
                try:
                    if grid[self.y-1][self.x-1] != 0:
                        if grid[self.y-1][self.x-1].team != self.team:
                            possibilities.append([self.y-1, self.x-1])
                except:
                    pass
            else:
                try:
                    if grid[self.y-1][self.x+1] != 0:
                        if grid[self.y-1][self.x+1].team != self.team:
                            possibilities.append([self.y-1, self.x+1])
                except:
                    pass
                try:
                    if grid[self.y-1][self.x-1] != 0:
                        if grid[self.y-1][self.x-1].team != self.team:
                            possibilities.append([self.y-1, self.x-1])
                except:
                    pass
        return possibilities

    def move_to(self,y,x):
        grid[self.y][self.x] = 0
        self.y = y
        self.x = x
        grid[self.y][self.x] = self
        if self.team == "black":
            if self.y == 7:
                grid[self.y][self.x] = Queen(self.y,self.x,self.team)
        else:
            if self.y == 0:
                grid[self.y][self.x] = Queen(self.y,self.x,self.team)

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Chess Game @DevMade")

def draw_grid():
    for x in range(-1, screen_x, 50):
        pygame.draw.line(screen, (255,255,255), (x, 0), (x, screen_y))
    for y in range(0, screen_y, 50):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (screen_x, y))

def set_player():
    Rook(0,0, "black")
    Rook(0,7, "black")
    Rook(7,0, "white")
    Rook(7,7, "white")
    Knight(0,1, "black")
    Knight(0,6, "black")
    Knight(7,1, "white")
    Knight(7,6, "white")
    Bishop(0,2, "black")
    Bishop(0,5, "black")
    Bishop(7,2, "white")
    Bishop(7,5, "white")
    Queen(0,3, "black")
    Queen(7,3, "white")
    King(0,4, "black")
    King(7,4, "white")
    for x in range(8):
        Pawn(1,x, "black")
        Pawn(6,x, "white")

def draw_player():
    for x in grid:
        for y in x:
            if y != 0:
                if y.team == turn:
                    pic = pygame.transform.scale(y.image, (50,50))
                    screen.blit(pic, (y.x*50, y.y*50))
                else:
                    pic = pygame.transform.scale(y.image, (40,40))
                    screen.blit(pic, (y.x*50+5, y.y*50+5))

def draw_options():
    for option in options:
        s = pygame.Surface((50,50))
        s.set_alpha(120)
        s.fill((0,200,0))
        screen.blit(s, (option[1]*50, option[0]*50))

def draw_background():
    black = True
    for x in range(0, screen_x, 50):
        for y in range(0, screen_y, 50):
            if black == True:
                pygame.draw.rect(screen, (187,133,80), (x, y, 50, 50))
                black = False
            else:
                pygame.draw.rect(screen, (234,195,159), (x, y, 50, 50))
                black = True
        black = not black
    enemy_king = get_king(turn)
    if [enemy_king.y, enemy_king.x] in get_all_player_options_from_team("white" if turn == "black" else "black"):
        s = pygame.Surface((50,50))
        s.set_alpha(120)
        s.fill((255,0,0))
        screen.blit(s, (enemy_king.x*50, enemy_king.y*50))

def get_all_player_options_from_team(team):
    all_player_options = []
    for x in grid:
        for y in x:
            if y != 0:
                if y.team == team:
                    all_player_options.extend(y.get_options())
    return all_player_options

def get_king(team):
    for x in grid:
        for y in x:
            if y != 0:
                if y.type == "King" and y.team == team:
                    return y

def check_for_lose(team):
    print("Check for Lose!")
    king = get_king(team)
    for x in grid:
        for y in x:
            if y != 0:
                if y.team == team:
                    for option in y.get_options():
                        attempt_y, attempt_x = option[0], option[1]
                        old_x , old_y = y.x, y.y
                        temp_char = grid[attempt_y][attempt_x]
                        y.move_to(attempt_y, attempt_x)
                        if [king.y, king.x] not in get_all_player_options_from_team("white" if team == "black" else "black"):
                            y.move_to(old_y, old_x)
                            grid[attempt_y][attempt_x] = temp_char
                            print("No Lose!")
                            return False
                        else:
                            y.move_to(old_y, old_x)
                            grid[attempt_y][attempt_x] = temp_char
    print("Lose!")
    return True

set_player()
turn = "white"

# main loop
running = True
while running:
    draw_background()
    draw_options()
    draw_grid()
    draw_player()
    pygame.display.flip()
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            pos = pygame.mouse.get_pos()
            # get grid position
            x = pos[0] // 50
            y = pos[1] // 50
            # check if grid position is empty
            clicked_object = grid[y][x]
            if clicked_object != 0 and clicked_object.team == turn:
                selected = [y, x]
                options = clicked_object.get_options()
            elif [y,x] in options:
                old_x , old_y = selected
                temp_char = grid[y][x]
                grid[selected[0]][selected[1]].move_to(y,x)
                king = get_king(turn)
                enemy_king = get_king("white" if turn == "black" else "black")
                if turn == "white":
                    if [king.y, king.x] not in get_all_player_options_from_team("black"):
                        turn = "black" if turn == "white" else "white"
                        selected = []
                        options = []
                        if [enemy_king.y, enemy_king.x] in get_all_player_options_from_team("white"):
                            print("Schach!")
                            if check_for_lose("black"):
                                print("white wins")
                                running = False
                    else:
                        grid[y][x].move_to(old_x,old_y)
                        pygame.draw.rect(screen, (255,0,0), (x*50, y*50, 50, 50))
                        draw_grid()
                        pygame.display.flip()
                        pygame.time.delay(200)
                        grid[y][x] = temp_char
                else:
                    if [king.y, king.x] not in get_all_player_options_from_team("white"):
                        turn = "white" if turn == "black" else "black"
                        selected = []
                        options = []
                        if [enemy_king.y, enemy_king.x] in get_all_player_options_from_team("white"):
                            print("Schach!")
                            if check_for_lose("white"):
                                print("black wins")
                                running = False
                    else:
                        grid[y][x].move_to(old_x,old_y)
                        pygame.draw.rect(screen, (255,0,0), (x*50, y*50, 50, 50))
                        draw_grid()
                        pygame.display.flip()
                        pygame.time.delay(200)
                        grid[y][x] = temp_char