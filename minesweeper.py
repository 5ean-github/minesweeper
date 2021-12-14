import pygame
import random

mine_0 = pygame.transform.scale(pygame.image.load('0.png'),(60,60))
mine_1 = pygame.transform.scale(pygame.image.load('1.png'),(60,60))
mine_2 = pygame.transform.scale(pygame.image.load('2.png'),(60,60))
mine_3 = pygame.transform.scale(pygame.image.load('3.png'),(60,60))
mine_4 = pygame.transform.scale(pygame.image.load('4.png'),(60,60))
mine_5 = pygame.transform.scale(pygame.image.load('5.png'),(60,60))
mine_6 = pygame.transform.scale(pygame.image.load('6.png'),(60,60))
mine_7 = pygame.transform.scale(pygame.image.load('7.png'),(60,60))
mine_8 = pygame.transform.scale(pygame.image.load('8.png'),(60,60))
mine_img = pygame.transform.scale(pygame.image.load('mine.png'),(60,60))
flag = pygame.transform.scale(pygame.image.load('flag.png'),(60,60))
unopened = pygame.transform.scale(pygame.image.load('unopened.png'),(60,60))
board = []
opened = []
visit=[0 for x in range(82)]

def generateBoard(level):
    if level == 'beginner':
        mines = []
        while True:
            mine = random.randint(1, 81)
            if mines.count(mine) == 0:
                mines.append(mine)
            if len(mines) == 10:
                break
        board.append('X')
        opened.append('X')
        for i in range(1,82):
            opened.append('no')
            if mines.count(i) == 0:
                    board.append('0')
            else:
                board.append('mine')
        for i in range(1,82):
            if board[i] != 'mine':
                surround = 0
                if i-10>=1 and i%9!=1 and board[i-10] == 'mine':
                    surround += 1
                if i-9>=1 and board[i-9] == 'mine':
                    surround += 1
                if i-8>=1 and i%9!=0 and board[i-8] == 'mine':
                    surround += 1
                if i-1>=1 and i%9!=1 and board[i-1] == 'mine':
                    surround += 1
                if i+1<=81 and i%9!=0 and board[i+1] == 'mine':
                    surround += 1
                if i+8<=81 and i%9!=1 and board[i+8] == 'mine':
                    surround += 1
                if i+9<=81 and board[i+9] == 'mine':
                    surround += 1
                if i+10<=81 and i%9!=0 and board[i+10] == 'mine':
                    surround += 1
                board[i]=surround

def posToSquare(pos):
    i=int(pos[0]/60)+1
    j=int(pos[1]/60)
    return i+j*9

def bfs(n):
    q = [n]
    opened[n] = 'yes'
    visit[n]=1
    while len(q)>0:
        i = q[0]
        if i-9>=1 and visit[i-9]== 0:
            visit[i-9]=1
            opened[i-9] = 'yes'
            if board[i-9]==0:
                q.append(i-9)
        if i-1>=1 and i%9!=1 and visit[i-1] == 0:
            visit[i-1]=1
            opened[i-1] = 'yes'
            if board[i-1] == 0:
                q.append(i-1)
        if i+1<=81 and i%9!=0 and visit[i+1] == 0:
            visit[i+1]=1
            opened[i+1] = 'yes'
            if board[i+1] == 0:
                q.append(i+1)
        if i+9<=81 and visit[i+9] == 0:
            visit[i+9]=1
            opened[i+9] = 'yes'
            if board[i+9] == 0:
                q.append(i+9)
        q.pop(0)

def start(level):
    generateBoard(level)
    running = True
    while running == True:
        running = False
        for i in range(1,82):
            if not (opened[i] == 'yes' or board[i] == 'mine'):
                running = True
        for i in range(9):
            for j in range(9):
                if opened[i*9+j+1] == 'no':
                    screen.blit(unopened, (60*j,60*i))
                elif opened[i*9+j+1] == 'flag':
                    screen.blit(flag, (60*j,60*i))
                else:
                    if board[i*9+j+1] == 0:
                        screen.blit(mine_0, (60*j,60*i))
                        if visit[i*9+j+1] == 0:
                            bfs(i*9+j+1)
                    if board[i*9+j+1] == 1:
                        screen.blit(mine_1, (60*j,60*i))
                    if board[i*9+j+1] == 2:
                        screen.blit(mine_2, (60*j,60*i))
                    if board[i*9+j+1] == 3:
                        screen.blit(mine_3, (60*j,60*i))
                    if board[i*9+j+1] == 4:
                        screen.blit(mine_4, (60*j,60*i))
                    if board[i*9+j+1] == 5:
                        screen.blit(mine_5, (60*j,60*i))
                    if board[i*9+j+1] == 6:
                        screen.blit(mine_6, (60*j,60*i))
                    if board[i*9+j+1] == 7:
                        screen.blit(mine_7, (60*j,60*i))
                    if board[i*9+j+1] == 8:
                        screen.blit(mine_8, (60*j,60*i))
                    if board[i*9+j+1] == 'mine':
                        screen.blit(mine_img, (60*j,60*i))
                        return False
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if opened[posToSquare(pos)] == 'no':
                    opened[posToSquare(pos)] = 'yes'
            if event.type  == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                if opened[posToSquare(pos)] == 'no':
                    opened[posToSquare(pos)] = 'flag'
                elif opened[posToSquare(pos)] == 'flag':
                    opened[posToSquare(pos)] = 'no'

        pygame.display.update()
        clock.tick(60)
    return True


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((540,540))
level = 'beginner'
result = start(level)
if not result:
    text = font.render('Game Over', True, (255, 0, 0))
else:
    text = font.render('You Won', True, (0, 255, 0))
time = pygame.time.get_ticks()
while pygame.time.get_ticks()<=time+2000:
    temp_surface = pygame.Surface(text.get_size())
    temp_surface.fill((192, 192, 192))
    temp_surface.blit(text, (0, 0))
    screen.blit(temp_surface, (200, 250))
    pygame.display.update()
    clock.tick(60)

