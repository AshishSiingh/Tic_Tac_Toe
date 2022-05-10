import pygame, random

pygame.init()

resolution = (300, 300)
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tic Tac Toe")

# creating the game board
class Game(object):
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    boardPos = {1: [0, 0], 2: [1, 0], 3: [2, 0],
                4: [0, 1], 5: [1, 1], 6: [2, 1],
                7: [0, 2], 8: [1, 2], 9: [2, 2]}

    first = "player"

    def __init__(self):
        pass
    
    # calculating the bot's move
    def botMove(self):
        bestScore = -1000
        bestMove = 0

        if self.first == "bot":
            self.first = ""
            guess = random.randrange(1, 10)
            self.board[guess] = 'X'
            ui.add(self.boardPos[guess], 1)

            return

        for key in self.board.keys():

            if self.board[key] == ' ':
                self.board[key] = 'X'
                score = self.minimax(0, -1000, 1000, False)
                self.board[key] = ' '

                if score > bestScore:
                    bestScore = score
                    bestMove = key

        self.board[bestMove] = 'X'
        ui.add(self.boardPos[bestMove], 1)
        
        return

    # getting the player's move
    def playerMove(self, position):
        pos = position
        pos[0] = (pos[0]) // 100
        pos[1] = (pos[1]) // 100

        if pos in ui.position:
            return False

        self.board[list(self.boardPos.keys())[list(self.boardPos.values()).index(pos)]] = 'O'
        ui.add(pos, 0)

        return True

    # check if the game is draw or not
    def draw(self):
        for i in self.board.keys():
            if self.board[i] == ' ':
                return False

        return True

    # checking if anyone won the game and the game is over or not
    def win(self):
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != ' '):
            ui.address = [[0, 0], [1, 0], [2, 0]]
            return True
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != ' '):
            ui.address = [[0, 1], [1, 1], [2, 1]]
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != ' '):
            ui.address = [[0, 2], [1, 2], [2, 2]]
            return True
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != ' '):
            ui.address = [[0, 0], [0, 1], [0,2]]
            return True
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' '):
            ui.address = [[1, 0], [1, 1], [1, 2]]
            return True
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != ' '):
            ui.address = [[2, 0], [2, 1], [2, 2]]
            return True
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != ' '):
            ui.address = [[0, 0], [1, 1], [2, 2]]
            return True
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != ' '):
            ui.address = [[0, 2], [1, 1], [2, 0]]
            return True
        else:
            return False

    # finding who won the game
    def whoWon(self, key):
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] == key):
            return True
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] == key):
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] == key):
            return True
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] == key):
            return True
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] == key):
            return True
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] == key):
            return True
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] == key):
            return True
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] == key):
            return True
        else:
            return False

    # algorithm for finding optimal moves for the bot
    def minimax(self, depth, alpha, beta, isMax):
        if self.whoWon('X'):
            return 10
        elif self.whoWon('O'):
            return -10
        elif self.draw():
            return 0

        if isMax:
            bestScore = -1000

            for key in self.board.keys():

                if self.board[key] == ' ':
                    self.board[key] = 'X'
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[key] = ' '

                    if score > bestScore:
                        bestScore = score - depth

                    alpha = max(alpha, score)

                    if(beta <= alpha):
                        break

            return bestScore
        else:
            bestScore = 1000

            for key in self.board.keys():

                if self.board[key] == ' ':
                    self.board[key] = 'O'
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[key] = ' '

                    if score < bestScore:
                        bestScore = score + depth

                    beta = min(beta, score)

                    if(beta <= alpha):
                        break

            return bestScore

# creating the UI of the game
class Ui(object):
    position = []
    address = []
    keys = []
    anim = []

    def __init__(self):
        pass

    # adding the positions of bot's and player's moves
    def add(self, pos, key):
        if pos not in self.position:
            self.position.append(pos)
            self.keys.append(key)
            self.anim.append(25.0)
    
    # creating the O and X on the game screen
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

    # reset the game to start a new match
    def reset(self):
        self.position = []
        self.address = []
        self.keys = []
        self.anim = []

        game.board = {1: ' ', 2: ' ', 3: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}

# checking if the move is valid or not
def moves(num):
    if not game.win() and not game.draw():
        if num % 2 != 0:
            if game.first != "":
                game.botMove()
                game.first = ""
            else:
                if pygame.mouse.get_pressed()[0]:
                    pos = list(pygame.mouse.get_pos())

                    if game.playerMove(pos):
                        game.first = "player"
        else:
            if game.first == "player":
                if pygame.mouse.get_pressed()[0]:
                    pos = list(pygame.mouse.get_pos())

                    if game.playerMove(pos):
                        game.first = ""
            else:
                game.botMove()
                game.first = "player"

# displaying the result after the game is over
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
    drawn = False

    if game.win():

        if ui.keys[len(ui.keys)-1] == 1:
            text = myfont.render("Bot Wins", False, (255, 255, 255))
        else:
            text = myfont.render("You Win", False, (255, 255, 255))

        gameOver = True

    elif game.draw():
        text = myfont.render("Draw", False, (255, 255, 255))
        gameOver = True
        drawn = True

    if gameOver and count < 50:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 100, 300, 100))
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 100, 300, 100), 2)
        surface.blit(text2, (10, 180))

        if drawn:
            surface.blit(text, (100, 125))
        else:
            surface.blit(text, (20, 125))

# creating the board's grid on screen
def drawGrid(surface):
    for i in range(1, 3):
        pygame.draw.line(surface, (255, 255, 255), (i*100, 0), (i*100, 300))
        pygame.draw.line(surface, (255, 255, 255), (0, i*100), (300, i*100))

# drawing the game window
def draw_window(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    ui.draw(surface)
    result(surface)
    pygame.display.update()

def main():
    global game, ui, count

    clock = pygame.time.Clock()
    isPlaying = True

    ui = Ui()
    game = Game()

    count = 0

    num = random.randrange(0, 10)
    if num % 2 != 0:
        game.first = "bot"

    while isPlaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            moves(num)

        if (game.win() or game.draw()) and pygame.key.get_pressed()[pygame.K_r]:
            ui.reset()
            game.first = "player"
            num = random.randrange(1, 1000)
            
            if num % 2 != 0:
                game.first = "bot"

        clock.tick(0)
        draw_window(window)


if __name__ == "__main__":
    main()
