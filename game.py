import pygame

pygame.init()
window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Pickaxe clicker')

# funkcje
def draw_object(object, x, y) :
    window.blit(object, (x, y)) # rysowanie objektu
def draw_hitbox(object) :
    pygame.draw.rect(window, (93, 32, 32), object)

# zmienne
game_version = 0.7
last_update = 23.01
x_for_kilof = 400
y_for_kilof = 400
x_for_button1 = 1150
y_for_button1 = 100
boost = 1
doswiadczenie = 0
dodaj = 1
kilof_upgrade = 50

# obiekty
kilof = pygame.image.load("Kilof.png")
button_upgrade = pygame.image.load("Button_upgrade.png")
button_upgrade_clicked = pygame.image.load("Button_upgrade_clicked.png")
button_upgrade2 = pygame.image.load("Button_upgrade2.png")
button_upgrade2_clicked = pygame.image.load("Button_upgrade2_clicked.png")
tlo = pygame.image.load("tlo.png")


# hitboxy
kilof_hitbox = pygame.rect.Rect(x_for_kilof, y_for_kilof, 330, 300)  # tworzy hitbox do kilofa
button_upgrade_hitbox = pygame.rect.Rect(1150, 100, 650, 100)   # tworzy hitbox do przycisku
button_upgrade2_hitbox = pygame.rect.Rect(1160, 880, 550, 100)

run = True

while run:
    pygame.time.Clock().tick(60)  # maksymalnie 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False

    text_wersja = pygame.font.Font.render(pygame.font.SysFont("Freemono", 50), f"Version : {game_version} | Last update : {last_update}", True, (255, 200, 100)) # generowanie tekstu 3
    text_doswiadczenie = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 72), f"Doswiadczenie : {doswiadczenie}", True, (100, 100, 100)) # generowanie tekstu
    text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}", True, (255, 255, 255)) # generowanie tekstu 2
    if doswiadczenie > boost :
        text_ulepszenie = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Dostepne", True, (255, 255, 255)) # generowanie tekstu 2
    else :
        text_ulepszenie = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Niedostepne", True, (255, 255, 255)) # generowanie tekstu 2

    if doswiadczenie > kilof_upgrade :
        text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}, Dostepne", True, (255, 255, 255)) # generowanie tekstu 2
    else :
        text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}, Niedostepne", True, (255, 255, 255)) # generowanie tekstu 2

    window.blit(tlo, (0, 0))  # rysowanie tła

    # rysowanie hitboxów
    draw_hitbox(kilof_hitbox) # rysowanie hitboxu do kilofa
    draw_hitbox(button_upgrade_hitbox) # rysowanie hitboxu do przycisku upgrade
    draw_hitbox(button_upgrade2_hitbox) # rysowanie hitboxu do przycisku shop
        
    # rysowanie obiektów
        
    draw_object(kilof, x_for_kilof, y_for_kilof) # rysowanie kilofu
    draw_object(button_upgrade, x_for_button1, y_for_button1) # rysowanie przycisku
    draw_object(button_upgrade2, 1160, 880) # rysowanie przycisku 2
    draw_object(text_doswiadczenie, 224, 100) # rysowanie tekstu
    draw_object(text_ulepszenie, 1160, 135) # rysowanie tekstu 2
    draw_object(text_wersja, 10, 5) # rysowanie tekstu 3
    draw_object(text_kilof, 1165, 920)
        

    # sprawdzanie zdarzeń z myszką
    if kilof_hitbox.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pygame.time.wait(100)
            doswiadczenie += dodaj
        
    if button_upgrade_hitbox.collidepoint(pygame.mouse.get_pos()) and doswiadczenie > boost :
        if pygame.mouse.get_pressed()[0]:
            dodaj += 1
            doswiadczenie = doswiadczenie - boost
            boost = boost * 2
            pygame.time.wait(100)

    if button_upgrade_hitbox.collidepoint(pygame.mouse.get_pos()):
        draw_object(button_upgrade_clicked, x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(text_ulepszenie, 1160, 135) # rysowanie tekstu 2
    else :
        draw_object(button_upgrade, x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(text_ulepszenie, 1160, 135) # rysowanie tekstu 2

    if button_upgrade2_hitbox.collidepoint(pygame.mouse.get_pos()):
        draw_object(button_upgrade2_clicked, 1160, 880) # rysowanie przycisku
        draw_object(text_kilof, 1165, 920) # rysowanie tekstu 2
    else :
        draw_object(button_upgrade2, 1160, 880) # rysowanie przycisku
        draw_object(text_kilof, 1165, 920) # rysowanie tekstu 2

    # wydrukuj
    pygame.display.update()
