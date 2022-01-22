import pygame

pygame.init()
window = pygame.display.set_mode((1920, 1080))

# zmienne
x = 400
y = 400
czas = 20
boost = 1
poziom = 1
wynik = 0

# obiekty
kilof = pygame.image.load("Kilof2.png")
width = kilof.get_width
height = kilof.get_height
button_upgrade1 = pygame.image.load("Button_upgrade.png")
button_upgrade1clicked = pygame.image.load("Button_upgrade_clicked.png")
tło = pygame.image.load("tlo.png")

# hitboxy
kilof_hitbox = pygame.rect.Rect(x, y, 330, 300)  # tworzy hitbox do kilofa
button_upgrade1_hitbox = pygame.rect.Rect(1000, 100, 300, 200)   # tworzy hitbox do przycisku

run = True

while run:

    keys = pygame.key.get_pressed() # klawisze 

    if keys[pygame.K_1] and wynik > boost : # sytem przyspieszania
        czas = czas - 2
        wynik = wynik - boost
        boost = boost * 2
        poziom += 1
  
    pygame.time.Clock().tick(60)  # maksymalnie 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False

    tekst_doswiadczenie = pygame.font.Font.render(pygame.font.SysFont("Calibri", 72), f"Doświadczenie : {wynik}", True, (100, 100, 100)) # generowanie tekstu
    Ulepszenie_boost = pygame.font.Font.render(pygame.font.SysFont("Calibri", 28), f"Ulepszenie prędkości | Level {poziom} | Koszt : {boost }", True, (255, 255, 255)) # generowanie tekstu 2
    
    # rysowanie obiektów
    kilof = pygame.image.load("Kilof2.png") # ładowanie obrazka
    window.blit(tło, (0, 0))  # rysowanie tła
    window.blit(button_upgrade1, (1000, 100)) # rysowanie przycisku
    window.blit(tekst_doswiadczenie, (224, 100)) # rysowanie tekstu
    window.blit(Ulepszenie_boost, (1150, 100)) # rysowanie tekstu 2

    # rysowanie hitboxów
    pygame.draw.rect(window, (90, 36, 32), kilof_hitbox) # rysowanie hitboxu do kilofa
    window.blit(kilof, (x, y)) # rysowanie kilofu
    #pygame.draw.rect(window), ()
    
    pygame.display.update()

    if kilof_hitbox.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pygame.time.wait(czas * 10)
            wynik += 1
    
