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
game_version = 0.6
last_update = 23.01
x_for_kilof = 400
y_for_kilof = 400
x_for_button1 = 1150
y_for_button1 = 100
boost = 1
doswiadczenie = 0
dodaj = 1

# obiekty
kilof = pygame.image.load("Kilof.png")
width = kilof.get_width
height = kilof.get_height
button_upgrade1 = pygame.image.load("Button_upgrade.png")
button_upgrade1clicked = pygame.image.load("Button_upgrade_clicked.png")
tło = pygame.image.load("tlo.png")

# hitboxy
kilof_hitbox = pygame.rect.Rect(x_for_kilof, y_for_kilof, 330, 300)  # tworzy hitbox do kilofa
button_upgrade1_hitbox = pygame.rect.Rect(1150, 100, 650, 100)   # tworzy hitbox do przycisku

run = True

while run:

    pygame.time.Clock().tick(60)  # maksymalnie 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False

    wersja = pygame.font.Font.render(pygame.font.SysFont("Freemono", 50), f"Version : {game_version} | Last update : {last_update}", True, (255, 200, 100)) # generowanie tekstu 3
    tekst_doswiadczenie = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 72), f"Doswiadczenie : {doswiadczenie}", True, (100, 100, 100)) # generowanie tekstu
    if doswiadczenie > boost :
        Ulepszenie_boost = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Dostepne", True, (255, 255, 255)) # generowanie tekstu 2
    else :
        Ulepszenie_boost = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Niedostepne", True, (255, 255, 255)) # generowanie tekstu 2

    window.blit(tło, (0, 0))  # rysowanie tła

    # rysowanie hitboxów
    draw_hitbox(kilof_hitbox) # rysowanie hitboxu do kilofa
    draw_hitbox(button_upgrade1_hitbox) # rysowanie hitboxu do przycisku
      
    # rysowanie obiektów
    
    draw_object(kilof, x_for_kilof, y_for_kilof) # rysowanie kilofu
    draw_object(button_upgrade1, x_for_button1, y_for_button1) # rysowanie przycisku
    draw_object(tekst_doswiadczenie, 224, 100) # rysowanie tekstu
    draw_object(Ulepszenie_boost, 1160, 135) # rysowanie tekstu 2
    draw_object(wersja, 10, 5) # rysowanie tekstu 3    

    # sprawdzanie zdarzeń z myszką
    if kilof_hitbox.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pygame.time.wait(200)
            doswiadczenie += dodaj
    
    if button_upgrade1_hitbox.collidepoint(pygame.mouse.get_pos()) and doswiadczenie > boost :
        if pygame.mouse.get_pressed()[0]:
            dodaj += 1
            doswiadczenie = doswiadczenie - boost
            boost = boost * 2
            pygame.time.wait(200)

    if button_upgrade1_hitbox.collidepoint(pygame.mouse.get_pos()):
        draw_object(button_upgrade1clicked, x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(Ulepszenie_boost, 1160, 135) # rysowanie tekstu 2
    else :
        draw_object(button_upgrade1,x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(Ulepszenie_boost, 1160, 135) # rysowanie tekstu 2

    # wydrukuj
    pygame.display.update()

