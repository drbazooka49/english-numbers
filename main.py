import pygame
import random
import sys
#from numbers.constants import WIDTH, HEIGHT, NUMBERS, EASY_GAME_CHOICES

MENU_SCENE = 0
EASY_GAME_SCENE = 1
HARD_GAME_SCENE = 2

WINDOW_COLOR = (99, 82, 108)
TEXT_COLOR = (255, 255, 255)
WRONG_COLOR = (216, 66, 66)
CORRECT_COLOR = (132, 243, 132)

WIDTH = 800
HEIGHT = 600

NUMBERS = {
           'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
           'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
           'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15,
           'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20,
           'twenty-one':21, 'twenty-two':22, 'twenty-three':23, 'twenty-four':24, 'twenty-five':25,
           'twenty-six':26, 'twenty-seven':27, 'twenty-eight':28, 'twenty-nine':29, 'thirty':30,
           'thirty-one':31, 'thirty-two':32, 'thirty-three':33, 'thirty-four':34, 'thirty-five':35,
           'thirty-six':36, 'thirty-seven':37, 'thirty-eight':38, 'thirty-nine':39, 'forty':40,
           'forty-one':41, 'forty-two':42, 'forty-three':43, 'forty-four':44, 'forty-five':45,
           'forty-six':46, 'forty-seven':47, 'forty-eight':48, 'forty-nine':49, 'fifty':50,
           'fifty-one':51, 'fifty-two':52, 'fifty-three':53, 'fifty-four':54, 'fifty-five':55,
           'fifty-six':56, 'fifty-seven':57, ' fifty-eight':58, 'fifty-nine':59, 'sixty':60,
           'sixty-one':61, 'sixty-two':62, 'sixty-three':63, 'sixty-four':64, 'sixty-five':65,
           'sixty-six':66, 'sixty-seven':67, 'sixty-eight':68, 'sixty-nine':69, 'seventy':70,
           'seventy-one':71, 'seventy-two':72, 'seventy-three':73, 'seventy-four':74, 'seventy-five':75,
           'seventy-six':76, 'seventy-seven':77, 'seventy-eight':78, 'seventy-nine':79, 'eighty':80,
           'eighty-one':81, 'eighty-two':82, 'eighty-three':83, 'eighty-four':84, 'eighty-five':85,
           'eighty-six':86, 'eighty-seven':87, 'eighty-eight':88, 'eighty-nine':89, 'ninety':90,
           'ninety-one':91, 'ninety-two':92, 'ninety-three':93, 'ninety-four':94, 'ninety-five':95,
           'ninety-six':96, 'ninety-seven':97, 'ninety-eight':98, 'ninety-nine':99, 'one hundred':100
           }

EASY_GAME_CHOICES = {
            1:['one', 'oane'], 2:['two', 'to'], 3:['three', 'tree'],
            4:['four', 'for'], 5:['five', 'faive'], 6:['six', 'sex'],
            7:['seven', 'saven'], 8:['eight', 'eit'], 9:['nine', 'nain'],
            10:['ten', 'tan'], 11:['eleven', 'elevin'], 12:['twelve', 'twalve'],
            13:['thirteen', 'threteen'], 14:['fourteen', 'forteen'], 15:['fifteen', 'fiften'],
            16:['sixteen', 'sixtin'], 17:['seventeen', 'seventen'], 18:['eighteen', 'eigteen'],
            19:['nineteen', 'nainteen'], 20:['twenty', 'twanty'], 21:['twenty-one', 'twanty-one'],
            22:['twenty-two', 'twenty-to'], 23:['twenty-three', 'twenty-tree'], 24:['twenty-four', 'twanty-for'],
            25:['twenty-five', 'twanty-five'], 26:['twenty-six', 'twanty-six'], 27:['twenty-seven', 'twanty-seven'],
            28:['twenty-eight', 'twenty-eigt'], 29:['twenty-nine', 'twanty-nine'], 30:['thirty', 'threety'],
            31:['thirty-one', 'therty-one'], 32:['thirty-two', 'threety-two'], 33:['thirty-three', 'therty-three'],
            34:['thirty-four', 'therty-for'], 35:['thirty-five', 'therty-five'], 36:['thirty-six', 'therty-six'],
            37:['thirty-seven', 'thirty-saven'], 38:['thirty-eight', 'thirty-eiht'], 39:['thirty-nine', 'therty-nine'],
            40:['forty', 'fourty'], 41:['forty-one', 'fourty-one'], 42:['forty-two', 'fourty-two'],
            43:['forty-three', 'forty-tree'], 44:['forty-four', 'forty-for'], 45:['forty-five', 'fourty-five'],
            46:['forty-six', 'foty-six'], 47:['forty-seven', 'forty-sevan'], 48:['forty-eight', 'fourty-eight'],
            49:['forty-nine', 'forty-nien'], 50:['fiftt', 'fivty'], 51:['fifty-one', 'fivty-one'],
            52:['fifty-two', 'fifty-twu'], 53:['fifty-three', 'fivty-three'], 54:['fifty-four', 'fifty-for'],
            55:['fifty-five', 'fifty-fiev'], 56:['fifty-six', 'fivty-six'], 57:['fifty-seven', 'fifty-saven'],
            58:['fifty-eight', 'fivty-eight'], 59:['fifty-nine', 'fifti-nine'], 60:['sixty', 'sixtty'],
            61:['sixty-one', 'sixti-one'], 62:['sixty-two', 'sexty-two'], 63:['sixty-three', 'sixty-thre'],
            64:['sixty-four', 'sixtty-four'], 65:['sixty-five', 'sixty-fieve'], 66:['sixty-six', 'sixtty-six'],
            67:['sixty-seven', 'sixty-sevan'], 68:['sixty-eight', 'sixty-eght'], 69:['sixty-nine', 'sixty-neine'],
            70:['seventy', 'sevanty'], 71:['seventy-one', 'saventy-one'], 72:['seventy-two', 'sevanty-two'],
            73:['seventy-three', 'seventy-tre'], 74:['seventy-four', 'seventy-foor'], 75:['seventy-five', 'seventy-feive'],
            76:['seventy-six', 'saventy-six'], 77:['seventy-seven', 'seventy-seveen'], 78:['seventy-eight', 'seventy-eith'],
            79:['seventy-nine', 'seveenty-nine'], 80:['eighty', 'eihty'], 81:['eighty-one', 'eigty-one'],
            82:['eighty-two', 'eithy-two'], 83:['eighty-three', 'eigthy-three'], 84:['eighty-four', 'eighty-foor'],
            85:['eighty-five', 'eigty-five'], 86:['eighty-six', 'eity-six'], 87:['eighty-seven', 'eithy-seveen'],
            88:['eighty-eight', 'eighty-eighth'], 89:['eighty-nine', 'eigty-nine'], 90:['ninety', 'neinty'],
            91:['ninety-one', 'neinty-one'], 92:['ninety-two', 'neinty-two'], 93:['ninety-three', 'nienty-three'],
            94:['ninety-four', 'ninety-for'], 95:['ninety-five', 'ninty-five'], 96:['ninety-six', 'nainty-six'],
            97:['ninety-seven', 'nienty-seven'], 98:['ninety-eight', 'ninety-eighth'], 99:['ninety-nine', 'neinty-nein'],
            100:['one hundred', 'one hundreed']
            }

def generate_random_number():
    number = random.randint(1, 100)
    #print('generated : ' + str(number))
    return number


def generate_random_left_and_right_choices(generated_number):
    left_choice = ''
    right_choice = ''
    for key in EASY_GAME_CHOICES:
        if key == generated_number:
            left_choice = random.choice(EASY_GAME_CHOICES[key])
            #print('left_choice: ' + left_choice)
            index = EASY_GAME_CHOICES[key].index(left_choice)
            #print('index of left_choice in list: ' + str(index))
            if index == 0:
                right_choice = EASY_GAME_CHOICES[key][1]
            elif index == 1:
                right_choice = EASY_GAME_CHOICES[key][0]
            #print('right_choice: ' + right_choice)
    return left_choice, right_choice


def check_choice(number, choice):
    for key in EASY_GAME_CHOICES:
        if key == number:
            if EASY_GAME_CHOICES[key][0] == choice:
                #print('correct answer:--' + EASY_GAME_CHOICES[key][0] + '--')
                #print('choice:--' + choice +'--')
                return True, CORRECT_COLOR
            else:
                return False, WRONG_COLOR


def check_number(userInput, number):
    for key in NUMBERS:
        if NUMBERS[key] == number:
            if key == userInput:
                return True, ''
            else:
                return False, key


def easy_game(WINDOW):
    choice_color_passive = (237, 218, 249)
    black = (0, 0, 0)

    choice_font = pygame.font.Font(None, 28)
    number_font = pygame.font.Font(None, 240)

    left_choice_button = pygame.Rect(180, 400, 150, 28)
    right_choice_button = pygame.Rect(470, 400, 150, 28)
    back_to_menu_button = pygame.Rect(20, 560, 100, 28)
    score_box = pygame.Rect(20, 20, 120, 28)

    clock = pygame.time.Clock()

    score = 0

    left_correct = False
    right_correct = False
    display_correct = False
    number_color = TEXT_COLOR
    left_color_choice = choice_color_passive
    right_color_choice = choice_color_passive
    color_choice = choice_color_passive
    number = generate_random_number()
    left_choice, right_choice = generate_random_left_and_right_choices(number)

    prepare_for_next = pygame.USEREVENT + 0

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu_button.collidepoint(event.pos):
                    return MENU_SCENE
                if left_choice_button.collidepoint(event.pos):
                    left_correct, left_color_choice = check_choice(number, left_choice)
                    if left_correct:
                        #print('correct left choice')
                        score += 5
                    # else:
                    #     print('incorrect left choice')
                    pygame.time.set_timer(prepare_for_next, 1000, loops=1)

                elif right_choice_button.collidepoint(event.pos):
                    right_correct, right_color_choice = check_choice(number, right_choice)
                    if right_correct:
                        #print('correct right choice')
                        score += 5
                    # else:
                    #     print('incorrect right choice')
                    pygame.time.set_timer(prepare_for_next, 1000, loops=1)
            elif event.type == prepare_for_next:
                left_color_choice = choice_color_passive
                right_color_choice = choice_color_passive
                number = generate_random_number()
                left_choice, right_choice = generate_random_left_and_right_choices(number)

        WINDOW.fill(WINDOW_COLOR)


        easy_game_surface = pygame.Surface((WIDTH, HEIGHT)).convert(WINDOW)

        number_text = number_font.render(str(number), True, number_color)
        number_surface = number_text.get_rect(center=(400, 250))
        left_choice_surface = choice_font.render(left_choice, True, black)
        right_choice_surface = choice_font.render(right_choice, True, black)
        back_to_menu_surface = choice_font.render('Back', True, black)
        score_surface = choice_font.render('Score: ' + str(score), True, TEXT_COLOR)

        #FIX game logic: if pressed correct, gets green if wrong, gets red
        pygame.draw.rect(WINDOW, left_color_choice, left_choice_button, border_radius=10)
        pygame.draw.rect(WINDOW, right_color_choice, right_choice_button, border_radius=10)
        pygame.draw.rect(WINDOW, choice_color_passive, back_to_menu_button, border_radius=12)


        WINDOW.blits([(number_text, (number_surface.x, number_surface.y)),
                      (score_surface, (score_box.x, score_box.y)),
                      (back_to_menu_surface, (back_to_menu_button.x + 25, back_to_menu_button.y + 5)),
                      (left_choice_surface, (left_choice_button.x + 10, left_choice_button.y + 2)),
                      (right_choice_surface, (right_choice_button.x + 10, right_choice_button.y + 2))])

        pygame.display.update()


def hard_game(WINDOW):
    input_box_color_passive = (147, 225, 199)
    input_box_color_active = (237, 218, 249)
    try_again_text_color = (0, 0, 0)
    answer_color = (255, 251, 101)

    input_font = pygame.font.Font(None, 28)
    number_font = pygame.font.Font(None, 240)

    user_input = ''

    input_box = pygame.Rect(274, 450, 250, 28)
    correct_answer_box = pygame.Rect(274, 422, 250, 28)
    back_to_menu_button = pygame.Rect(20, 560, 100, 28)
    try_again_button = pygame.Rect(660, 20, 120, 28)
    score_box = pygame.Rect(20, 20, 120, 28)

    clock = pygame.time.Clock()

    score = 0
    active = False
    correct = False
    display_correct = False
    try_again_active = False
    correct_number_text = ''
    number_color = TEXT_COLOR
    number = generate_random_number()

    change_color_back = pygame.USEREVENT + 0
    generate_new_number = pygame.USEREVENT + 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if try_again_button.collidepoint(event.pos):
                    display_correct = False
                    user_input = ''
                elif back_to_menu_button.collidepoint(event.pos):
                    return MENU_SCENE

            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        correct, correct_number_text = check_number(user_input, number)
                        if correct:
                            score += 10
                            number_color = CORRECT_COLOR
                            user_input = ''
                            pygame.time.set_timer(change_color_back, 1000, loops=1)
                            pygame.time.set_timer(generate_new_number, 1000, loops=1)
                        else:
                            display_correct = True
                            try_again_active = True
                            number_color = WRONG_COLOR
                            pygame.time.set_timer(change_color_back, 1000, loops=1)
                    else:
                        user_input += event.unicode
            elif event.type == change_color_back:
                number_color = TEXT_COLOR
            elif event.type == generate_new_number:
                number = generate_random_number()


        WINDOW.fill(WINDOW_COLOR)

        if active:
            color = input_box_color_active
        else:
            color = input_box_color_passive

        if try_again_active:
            try_again_button_color = input_box_color_active
        else:
            try_again_button_color = input_box_color_passive

        hard_game_surface = pygame.Surface((WIDTH, HEIGHT)).convert(WINDOW)

        number_text = number_font.render(str(number), True, number_color)
        back_to_menu_surface = input_font.render('Back', True, try_again_text_color)

        number_surface = number_text.get_rect(center=(400, 250))
        text_surface = input_font.render(user_input, True, TEXT_COLOR)
        score_surface = input_font.render('Score: ' + str(score), True, TEXT_COLOR)

        pygame.draw.rect(WINDOW, color, input_box, 1)
        pygame.draw.rect(WINDOW, input_box_color_active, back_to_menu_button, border_radius=12)

        WINDOW.blits([(text_surface, (input_box.x + 5, input_box.y + 5)),
                      (number_text, (number_surface.x, number_surface.y)),
                      (score_surface, (score_box.x, score_box.y)),
                      (back_to_menu_surface, (back_to_menu_button.x + 25, back_to_menu_button.y + 5))])

        if display_correct:
            pygame.draw.rect(WINDOW, try_again_button_color, try_again_button, border_radius=12)

            correct_answer_text = input_font.render(correct_number_text, True, answer_color)
            try_again_button_surface = input_font.render('Try again', True, try_again_text_color)
            WINDOW.blits([(correct_answer_text, (correct_answer_box.x, correct_answer_box.y)),
                          (try_again_button_surface, (try_again_button.x + 15, try_again_button.y + 5))])

        pygame.display.update()
        clock.tick(30)


def menu(WINDOW):
    #Colors
    main_menu_color_passive = (208, 151, 164)
    main_menu_color_active = (178, 148, 209)

    #Font
    main_menu_font = pygame.font.Font(None, 70)

    #Rectangles for main menu buttons
    easy_button = pygame.Rect(320, 250, 160, 55)
    hard_button = pygame.Rect(320, 320, 160, 55)

    clock = pygame.time.Clock()
    start_easy_game = False
    start_hard_game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    start_easy_game = True
                    return EASY_GAME_SCENE
                elif hard_button.collidepoint(event.pos):
                    start_hard_game = True
                    return HARD_GAME_SCENE

        WINDOW.fill(WINDOW_COLOR)

        if start_easy_game:
            easy_button_color = main_menu_color_active
        else:
            easy_button_color = main_menu_color_passive

        if start_hard_game:
            hard_button_color = main_menu_color_active
        else:
            hard_button_color = main_menu_color_passive

        main_menu_surface = pygame.Surface((WIDTH, HEIGHT)).convert(WINDOW)

        #Draw rectangles for buttons
        pygame.draw.rect(WINDOW, easy_button_color, easy_button, border_radius=12)
        pygame.draw.rect(WINDOW, hard_button_color, hard_button, border_radius=12)

        #Surfaces for easy, hard buttons and game name text
        easy_button_surface = main_menu_font.render('Easy', True, TEXT_COLOR)
        hard_button_surface = main_menu_font.render('Hard', True, TEXT_COLOR)
        game_name_main_menu = main_menu_font.render('English Numbers', True, TEXT_COLOR)

        game_name_main_menu_surface = game_name_main_menu.get_rect(center = (400, 200))

        WINDOW.blits([(main_menu_surface, (WIDTH, HEIGHT)),
                      (easy_button_surface, (easy_button.x + 23, easy_button.y + 3)),
                      (hard_button_surface, (hard_button.x + 23, hard_button.y + 5)),
                      (game_name_main_menu, (game_name_main_menu_surface.x, game_name_main_menu_surface.y))])
        pygame.display.update()
        clock.tick(30)


def main():
    pygame.init()
    pygame.display.set_caption('English Numbers')
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    scene = MENU_SCENE
    run = True

    while run:
        if scene == MENU_SCENE:
            scene = menu(WINDOW)
        elif scene == EASY_GAME_SCENE:
            scene = easy_game(WINDOW)
        elif scene == HARD_GAME_SCENE:
            scene = hard_game(WINDOW)

main()
# while True:
#     pass
