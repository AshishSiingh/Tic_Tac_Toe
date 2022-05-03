import pygame, random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

boardPos = {1: [0, 0], 2: [1, 0], 3: [2, 0],
            4: [0, 1], 5: [1, 1], 6: [2, 1],
            7: [0, 2], 8: [1, 2], 9: [2, 2]}

def botMove():
    global first

    bestScore = -1000
    bestMove = 0
    if first == "bot":
        first = ""
        guess = random.randrange(1, 10)
        board[guess] = 'X'
        Game.add(boardPos[guess], 1)
        return

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(board, 0, -1000, 1000, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    board[bestMove] = 'X'
    Game.add(boardPos[bestMove], 1)
    return

def playerMove(position):
    pos = position
    pos[0] = (pos[0])//100
    pos[1] = (pos[1])//100
    if pos in Game.position:
        return False
    board[list(boardPos.keys())[list(boardPos.values()).index(pos)]] = 'O'
    Game.add(pos, 0)
    return True

def draw():
    for i in board.keys():
        if board[i] == ' ':
            return False
    return True

def win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        Game.address = [[0, 0], [1, 0], [2, 0]]
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        Game.address = [[0, 1], [1, 1], [2, 1]]
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        Game.address = [[0, 2], [1, 2], [2, 2]]
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        Game.address = [[0, 0], [0, 1], [0,2]]
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        Game.address = [[1, 0], [1, 1], [1, 2]]
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        Game.address = [[2, 0], [2, 1], [2, 2]]
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        Game.address = [[0, 0], [1, 1], [2, 2]]
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        Game.address = [[0, 2], [1, 1], [2, 0]]
        return True
    else:
        return False

def whoWon(key):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == key):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == key):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == key):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == key):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == key):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == key):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == key):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == key):
        return True
    else:
        return False

def minimax(board, depth, alpha, beta, isMax):
    if whoWon('X'):
        return 10
    elif whoWon('O'):
        return -10
    elif draw():
        return 0

    if isMax:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, depth + 1, alpha, beta, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score - depth
                alpha = max(alpha, bestScore)

                if(beta <= alpha):
                    break
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, depth + 1, alpha, beta, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score + depth
                beta = min(beta, bestScore)

                if(beta <= alpha):
                    break
        return bestScore


########################################################################################################################
########################################################################################################################
pygame.init()

resolution = (300, 300)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tic Tac Toe")


class TicTacToe(object):
    position = []
    address = []
    keys = []
    anim = []

    def __init__(self):
        pass

    def add(self, pos, key):
        if pos not in self.position:
            self.position.append(pos)
            self.keys.append(key)
            self.anim.append(25.0)
    
    def draw(self, surface):
        color = (255, 255, 255)
        for pos in range(len(self.position)):
            if self.position[pos] in self.address:
                color = (0, 250, 0)
            else:
                color = (255, 255, 255)
            animCount = int(self.anim[pos])
            if self.keys[pos] == 0:
                pygame.draw.circle(surface, color, (100*self.position[pos][0]+50, 100*self.position[pos][1]+50), 30-animCount, 5)
                if self.anim[pos] > 0:
                    self.anim[pos] -= 0.15
            else:
                pygame.draw.line(surface, color, (100*self.position[pos][0]+25+animCount, 100*self.position[pos][1]+25+animCount), (100*self.position[pos][0]+75-animCount, 100*self.position[pos][1]+75-animCount), 5)
                pygame.draw.line(surface, color, (100*self.position[pos][0]+75-animCount, 100*self.position[pos][1]+25+animCount), (100*self.position[pos][0]+25+animCount, 100*self.position[pos][1]+75-animCount), 5)
                if self.anim[pos] > 0:
                    self.anim[pos] -= 0.15

    def reset(self):
        global board
        self.position = []
        self.address = []
        self.keys = []
        self.anim = []

        board = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}

 
def moves(num):
    global first, Game

    if not win() and not draw():
        if num % 2 != 0:
            if first != "":
                botMove()
                first = ""
            else:
                if pygame.mouse.get_pressed()[0]:
                    pos = list(pygame.mouse.get_pos())
                    if playerMove(pos):
                        first = "player"
        else:
            if first == "player":
                if pygame.mouse.get_pressed()[0]:
                    pos = list(pygame.mouse.get_pos())
                    if playerMove(pos):
                        first = ""
            else:
                botMove()
                first = "player"

def result(surface):
    global count

    if count > 100:
        count = 0
    else:
        count += 0.1

    pygame.font.init()
    myfont = pygame.font.SysFont('Consolas', 50)
    myfont2 = pygame.font.SysFont('Consolas', 15)
    text = myfont.render("", False, (255, 255, 255))
    text2 = myfont2.render("Press 'R' to reset", False, (0, 100, 250))
    gameOver = False
    draa = False

    if win():
        if Game.keys[len(Game.keys)-1] == 1:
            text = myfont.render("Bot Wins", False, (255, 255, 255))
        else:
            text = myfont.render("You Win", False, (255, 255, 255))
        gameOver = True
    elif draw():
        text = myfont.render("Draw", False, (255, 255, 255))
        gameOver = True
        draa = True

    if gameOver and count < 50:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 100, 300, 100))
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 100, 300, 100), 2)
        surface.blit(text2, (10, 180))
        if draa:
            surface.blit(text, (100, 125))
        else:
            surface.blit(text, (20, 125))

def drawGrid(surface):
    for i in range(1, 3):
        pygame.draw.line(surface, (255, 255, 255), (i*100, 0), (i*100, 300))
        pygame.draw.line(surface, (255, 255, 255), (0, i*100), (300, i*100))

def draw_window(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    Game.draw(surface)
    result(window)
    pygame.display.update()

def main():
    global Game, first, count
    clock = pygame.time.Clock()
    isPlaying = True
    Game = TicTacToe()

    first = "player"
    count = 0

    num = random.randrange(0, 10)
    if num % 2 != 0:
        first = "bot"

    while isPlaying:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            moves(num)

        if (win() or draw()) and pygame.key.get_pressed()[pygame.K_r]:
            Game.reset()
            first = "player"
            #x = random.randrange(1, 8)
            num = random.randrange(1, 1000)
            if num % 2 != 0:
                first = "bot"

        clock.tick(0)
        draw_window(window)


if __name__ == "__main__":
    main()
