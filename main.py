import pygame
import random
import sys
from numbers.constants import WIDTH, HEIGHT, NUMBERS

def generateRandomNumber():
    number = random.randint(1, 100)
    print('generated : ' + str(number))
    return number


def checkNumber(userInput, number):
    for key in NUMBERS:
        if NUMBERS[key] == number:
            if key == userInput:
                return True, ''
            else:
                return False, key


def main():
    pygame.init()
    pygame.display.set_caption('English Numbers')
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    #surface = pygame.image.load('texture.jpg')

    windowColor = (99, 82, 108)
    inputBoxColorPassive = (147, 225, 199)
    inputBoxColorActive = (237, 218, 249)
    tryAgainTextColor = (0, 0, 0)
    answerColor = (255, 251, 101)


    inputFont = pygame.font.Font(None, 28)
    numberFont = pygame.font.Font(None, 240)
    userInput = ''

    inputBox = pygame.Rect(274, 450, 250, 28)
    correctAnswerBox = pygame.Rect(274, 422, 250, 28)

    tryAgainButton = pygame.Rect(660, 20, 120, 28)
    #numberBox = pygame.Rect(300, 130, 200, 200)

    pygame.display.update()

    run = True
    active = False
    correct = False
    displayCorrect = False
    correctNumberText = ''
    number = generateRandomNumber()
    clock = pygame.time.Clock()

    # TODO: make score and punish for 3 incorrect attempts

    score = 0  

    while run:
        for event in pygame.event.get():
            numberColor = (255, 255, 255)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #randNum = generateRandomNumber()
                print('pressing mouse')
                if inputBox.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if tryAgainButton.collidepoint(event.pos):
                    print('try again')
                    displayCorrect = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        print('pressing backspace')
                        userInput = userInput[:-1]
                    elif event.key == pygame.K_RETURN:
                        correct, correctNumberText = checkNumber(userInput, number)
                        if correct:
                            print('correct')
                            numberColor = (132, 243, 132)
                            score += 10
                            number = generateRandomNumber()
                            userInput = ''
                        else:
                            displayCorrect = True
                            numberColor = (216, 66, 66)
                            pygame.event.wait()

                    else:
                        userInput += event.unicode

        WINDOW.fill(windowColor)

        if active:
            color = inputBoxColorActive
            #print('color active')
        else:
            color = inputBoxColorPassive


        pygame.draw.rect(WINDOW, color, inputBox, 1)

        numberText = numberFont.render(str(number), True, numberColor)
        numberSurface = numberText.get_rect(center = (400, 250))
        #pygame.draw.rect(WINDOW, color, numberSurface, 2)
        textSurface = inputFont.render(userInput, True, (255, 255, 255))
        WINDOW.blits([(textSurface, (inputBox.x + 5, inputBox.y + 5)),
                      (numberText, (numberSurface.x, numberSurface.y))])

        if displayCorrect:
            pygame.draw.rect(WINDOW, color, tryAgainButton)
            correctAnswerText = inputFont.render(correctNumberText, True, answerColor)
            tryAgainButtonSurface = inputFont.render('Try again', True, tryAgainTextColor)
            WINDOW.blits([(correctAnswerText, (correctAnswerBox.x, correctAnswerBox.y)),
                          (tryAgainButtonSurface, (tryAgainButton.x + 15, tryAgainButton.y + 5))])

        #correctAnswerText = inputFont.render(correctNumberText, True, windowColor)
        #WINDOW.blit(correctAnswerText, (correctAnswerBox.x, correctAnswerBox.y))

        #inputBox.w = max(200, textSurface.get_width() + 10)

        pygame.display.update()
        clock.tick(30)


main()