import pygame, sys
from Button_class import Button

#
# github : Arshia-Danandeh
#

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

background_color = "black"
BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def choose_difficulty():
    global background_color
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(background_color)

        TITLE_TEXT = get_font(50).render("Choose Difficulty", True, "White" if background_color == "black" else "Black")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        EASY_BUTTON = Button(image=None, pos=(640, 300), text_input="EASY", font=get_font(55), base_color="Green", hovering_color="White")
        MEDIUM_BUTTON = Button(image=None, pos=(640, 400), text_input="MEDIUM", font=get_font(55), base_color="Yellow", hovering_color="White")
        HARD_BUTTON = Button(image=None, pos=(640, 500), text_input="HARD", font=get_font(55), base_color="Red", hovering_color="White")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MOUSE_POS):
                    play("EASY")
                if MEDIUM_BUTTON.checkForInput(MOUSE_POS):
                    play("MEDIUM")
                if HARD_BUTTON.checkForInput(MOUSE_POS):
                    play("HARD")

        pygame.display.update()

def play(difficulty):
    global background_color

    total_coins = 15
    player_turn = True 
    bot_last_move = 0  


    def bot_move(coins_left):
        import random

        if difficulty == "EASY":
            return random.randint(1, min(4, coins_left))
        
        elif difficulty == "MEDIUM":
            best_move = (coins_left - 1) % 5
            if best_move == 0 or random.random() < 0.3:  
                return random.randint(1, min(4, coins_left))
            else:
                return min(best_move, coins_left)
            
        elif difficulty == "HARD":
            best_move = (coins_left - 1) % 5
            if best_move == 0:
                return random.randint(1, min(4, coins_left))
            else:
                return min(best_move, coins_left)

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(background_color)

        COIN_TEXT = get_font(40).render(f"Coins Left: {total_coins}", True, "Cyan")
        SCREEN.blit(COIN_TEXT, (600, 50))

        TURN_TEXT = get_font(30).render("Your Turn!" if player_turn else "Bot's Turn!", True, "Yellow")
        SCREEN.blit(TURN_TEXT, (600, 120))

        BOT_MOVE_TEXT = get_font(30).render(f"Bot took: {bot_last_move}" if bot_last_move else "", True, "Red")
        SCREEN.blit(BOT_MOVE_TEXT, (600, 170))

        Num1_BUTTON = Button(image=None, pos=(300, 500), text_input="1", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        Num2_BUTTON = Button(image=None, pos=(500, 500), text_input="2", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        Num3_BUTTON = Button(image=None, pos=(700, 500), text_input="3", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        Num4_BUTTON = Button(image=None, pos=(900, 500), text_input="4", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        number_buttons = [Num1_BUTTON, Num2_BUTTON, Num3_BUTTON, Num4_BUTTON]

        for button in number_buttons:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 650), text_input="BACK", font=get_font(20), base_color="White", hovering_color="Red")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

                if player_turn:  
                    for i, button in enumerate(number_buttons):
                        if button.checkForInput(PLAY_MOUSE_POS):
                            coins_taken = i + 1
                            if total_coins >= coins_taken:
                                total_coins -= coins_taken
                                player_turn = False

        if not player_turn and total_coins > 0:
            pygame.time.wait(500)
            bot_last_move = bot_move(total_coins)
            total_coins -= bot_last_move
            player_turn = True

        if total_coins <= 0:
            winner = "Bot" if player_turn else "Player"
            WINNER_TEXT = get_font(50).render(f"{winner} Loses!", True, "Red")
            SCREEN.blit(WINNER_TEXT, (640, 300))

            RESTART_BUTTON = Button(image=None, pos=(640, 400), text_input="RESTART", font=get_font(40), base_color="Green", hovering_color="White")
            RESTART_BUTTON.changeColor(PLAY_MOUSE_POS)
            RESTART_BUTTON.update(SCREEN)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    choose_difficulty()

        pygame.display.update()

def options():    
    global background_color
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(background_color)

        OPTIONS_TEXT = get_font(45).render("OPTIONS", True, "White" if background_color == "black" else "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        COLOR_TOGGLE_BUTTON = Button(image=None, pos=(640, 400), text_input="TOGGLE BG COLOR", font=get_font(35), base_color="Blue", hovering_color="White")
        BACK_BUTTON = Button(image=None, pos=(640, 550), text_input="BACK", font=get_font(35), base_color="Green", hovering_color="White")

        for button in [COLOR_TOGGLE_BUTTON, BACK_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if COLOR_TOGGLE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    background_color = "white" if background_color == "black" else "black"


                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                    return

        pygame.display.update()
        
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    choose_difficulty()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()