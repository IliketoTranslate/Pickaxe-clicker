import pygame

icon = pygame.image.load("diamond_pickaxe.png")

screen_weight = 1750
screen_height = 980

pygame.init()
window = pygame.display.set_mode((screen_weight, screen_height))
pygame.display.set_caption('Pickaxe clicker')
pygame.display.set_icon(icon)


# zmienne
wytrzymałość_kilofa = 50
max_wytrzymałość_kilofa = 50
dodaj2 = 1
record = 0
game_version = "0.2.2"
last_update = "28.01.2022"
x_for_kilof = 400
y_for_kilof = 400
x_for_button1 = 1030
y_for_button1 = 80
x_for_button2 = 1030
y_for_button2 = 800
boost = 1
doswiadczenie = 0
dodaj = 1
max_dodaj = 1
kilof_upgrade = 100
choosed_kilof = 1

# obiekty
kilof = pygame.image.load("Drewniany_kilof.png")
kilof2 = pygame.image.load("Kamienny_kilof.png")
kilof3 = pygame.image.load("Zelazny_kilof.png")
kilof4 = pygame.image.load("Zloty_kilof.png")
kilof5 = pygame.image.load("Diamentowy_kilof.png")
button_upgrade = pygame.image.load("Button_upgrade.png")
button_upgrade_clicked = pygame.image.load("Button_upgrade_clicked.png")
button_upgrade2 = pygame.image.load("Button_upgrade2.png")
button_upgrade2_clicked = pygame.image.load("Button_upgrade2_clicked.png")
button_restart = pygame.image.load("Button_restart.png")
tlo = pygame.image.load("tlo.png")
tlo = pygame.transform.scale(tlo, (screen_weight, screen_height)) # skalowanie

# hitboxy
kilof_hitbox = pygame.rect.Rect(x_for_kilof, y_for_kilof, 160, 160)  # tworzy hitbox do kilofa
button_upgrade_hitbox = pygame.rect.Rect(x_for_button1, y_for_button1, 650, 100)   # tworzy hitbox do przycisku
button_upgrade2_hitbox = pygame.rect.Rect(x_for_button2, y_for_button2, 650, 100)


# funkcje
def draw_object(object, x, y) :
    window.blit(object, (x, y)) # rysowanie objektu
def draw_hitbox(object) :
    pygame.draw.rect(window, (93, 32, 32), object)
def zdarzenia_z_myszką() :
    wytrzymałość_kilofa = 50
    max_wytrzymałość_kilofa = 50
    dodaj2 = 1
    record = 0
    game_version = "0.2.2"
    last_update = "28.01.2022"
    x_for_kilof = 400
    y_for_kilof = 400
    x_for_button1 = 1030
    y_for_button1 = 80
    x_for_button2 = 1030
    y_for_button2 = 800
    boost = 1
    doswiadczenie = 0
    dodaj = 1
    max_dodaj = 1
    kilof_upgrade = 100
    choosed_kilof = 1

    kilof_upgrade2 = kilof_upgrade  - 1

    if wytrzymałość_kilofa == 0 :                                                                                                                        
        dodaj = 0                                                                                                                                
        dodaj2 = 0
    else :                                                                                                                                                                                                                                                             
        dodaj2 = 1
        dodaj = max_dodaj   

    if choosed_kilof > 0 and choosed_kilof < 5 :
        if button_upgrade2_hitbox.collidepoint(pygame.mouse.get_pos()) and doswiadczenie > kilof_upgrade2 : # jeżeli mysz dotyka hitboxa                       
            if pygame.mouse.get_pressed()[0]:                                                              # jeżeli naciśnieto lewy przycisk myszy             
                doswiadczenie = doswiadczenie - kilof_upgrade                                                                                                                                                                                                                                           
                if wytrzymałość_kilofa == 0 :                                                                                                                        
                    choosed_kilof = 1
                    kilof_upgrade = 100
                    dodaj = 0                                                                                                                                
                    dodaj2 = 0
                    wytrzymałość_kilofa = max_wytrzymałość_kilofa
                else :                                                                                                                                                                                                                                                             
                    dodaj2 = 1
                    choosed_kilof += 1
                    max_wytrzymałość_kilofa = max_wytrzymałość_kilofa * 2
                    kilof_upgrade = kilof_upgrade * 2
                    wytrzymałość_kilofa = max_wytrzymałość_kilofa
        pygame.time.wait(50)                    
    else :
        max_wytrzymałość_kilofa = 800
        kilof_upgrade = 10000000000
        if button_upgrade2_hitbox.collidepoint(pygame.mouse.get_pos()) and doswiadczenie > kilof_upgrade2 : # jeżeli mysz dotyka hitboxa                       
            if pygame.mouse.get_pressed()[0]:                                                               # jeżeli naciśnieto lewy przycisk myszy
                wytrzymałość_kilofa = max_wytrzymałość_kilofa
        pygame.time.wait(50)
                                                                                                        
    if kilof_hitbox.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pygame.time.wait(100)
            doswiadczenie += dodaj
            wytrzymałość_kilofa = wytrzymałość_kilofa - dodaj2

    boost2 = boost - 1

    if button_upgrade_hitbox.collidepoint(pygame.mouse.get_pos()) and doswiadczenie > boost2:
        if pygame.mouse.get_pressed()[0]:
            max_dodaj += choosed_kilof
            doswiadczenie = doswiadczenie - boost
            boost = boost * 2
            pygame.time.wait(100)

    if button_upgrade2_hitbox.collidepoint(pygame.mouse.get_pos()):
        draw_object(button_upgrade2_clicked, x_for_button2, y_for_button2) # rysowanie przycisku
        draw_object(text_kilof, 1040, 840) # rysowanie tekstu 2
    else :
        draw_object(button_upgrade2, x_for_button2, y_for_button2) # rysowanie przycisku
        draw_object(text_kilof, 1040, 840) # rysowanie tekstu 2

    if button_upgrade_hitbox.collidepoint(pygame.mouse.get_pos()):
        draw_object(button_upgrade_clicked, x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(text_ulepszenie, 1040, 110) # rysowanie tekstu 2
    else :
        draw_object(button_upgrade, x_for_button1, y_for_button1) # rysowanie przycisku
        draw_object(text_ulepszenie, 1040, 110) # rysowanie tekstu 2

run = True

while run:
    pygame.time.Clock().tick(100)  # maksymalnie 100 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] :
        run = False
                                                                                                                                                                                                                                                    
    # napisy
    kilof_upgrade2 = kilof_upgrade - 1
    text_wersja = pygame.font.Font.render(pygame.font.SysFont("Freemono", 50), f"Version : {game_version} | Last update : {last_update}", True, (255, 200, 100)) # generowanie tekstu 
    text_doswiadczenie = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 72), f"Doswiadczenie : {doswiadczenie}", True, (100, 100, 100)) # generowanie tekstu
    text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}", True, (255, 255, 255)) # generowanie tekstu 
    text_WIP = pygame.font.Font.render(pygame.font.SysFont("Waree", 25), f"W I P (WORK IN PROGRESS)", True, (255, 255, 255)) # generowanie tekstu 2
    text_wytrzymałość_kilofa = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 50), f"Wytrzymalosc kilofa : {wytrzymałość_kilofa}", True, (255, 255, 255)) # generowanie tekstu 2
    text_record = pygame.font.Font.render(pygame.font.SysFont("Liberation Serif", 50), f"Record : {record}", True, (150, 150, 150))
    if choosed_kilof > 0 and choosed_kilof < 5 : 
        if doswiadczenie > kilof_upgrade2 :
            text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}, Dostepne", True, (255, 255, 255)) # generowanie tekstu 2
        else :
            text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Kup kilof | Koszt : {kilof_upgrade}, Niedostepne", True, (255, 255, 255)) # generowanie tekstu 2
    elif choosed_kilof == 5 :
        text_kilof = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Nie ma wiecej dostepnych kilofow", True, (255, 255, 255)) # generowanie tekstu 2

    boost2 = boost - 1
    
    if doswiadczenie > boost2 :
        text_ulepszenie = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Dostepne", True, (255, 255, 255)) # generowanie tekstu 
    else :
        text_ulepszenie = pygame.font.Font.render(pygame.font.SysFont("Sawasdee", 25), f"Ulepszenie kilofa | Koszt : {boost}, Niedostepne", True, (255, 255, 255)) # generowanie tekstu 
    
    window.blit(tlo, (0, 0))  # rysowanie tła

    # rysowanie hitboxów
    draw_hitbox(kilof_hitbox) # rysowanie hitboxu do kilofa
    draw_hitbox(button_upgrade_hitbox) # rysowanie hitboxu do przycisku upgrade
    draw_hitbox(button_upgrade2_hitbox) # rysowanie hitboxu do przycisku upgrade2
        
    # rysowanie obiektów
     
    if choosed_kilof == 1 : draw_object(kilof, x_for_kilof, y_for_kilof) # rysowanie kilofu
    elif choosed_kilof == 2 : draw_object(kilof2, x_for_kilof, y_for_kilof)
    elif choosed_kilof == 3 : draw_object(kilof3, x_for_kilof, y_for_kilof)
    elif choosed_kilof == 4 : draw_object(kilof4, x_for_kilof, y_for_kilof)
    elif choosed_kilof == 5 or choosed_kilof > 5 : draw_object(kilof5, x_for_kilof, y_for_kilof)
    draw_object(button_upgrade, x_for_button1, y_for_button1) # rysowanie przycisku
    draw_object(button_upgrade2, x_for_button2, y_for_button2) # rysowanie przycisku 2
    draw_object(button_restart, 0, 0)
    draw_object(text_doswiadczenie, 224, 100) # rysowanie tekstu
    draw_object(text_ulepszenie, 1040, 110) # rysowanie tekstu 2
    draw_object(text_wersja, 10, 5) # rysowanie tekstu 3
    draw_object(text_kilof, 1040, 840)
    draw_object(text_WIP, 1170, 750)
    draw_object(text_wytrzymałość_kilofa, 250, 300)
    draw_object(text_record, 1280, 0)
    
    # sprawdzanie zdarzeń z myszką 
    
    zdarzenia_z_myszką()

    # sprawdzanie

    if doswiadczenie > record :
        record = doswiadczenie
    
    #if x_for_button1 > 80 :

    
    #if x_for_button2 > 800 :


    # wydrukuj
    pygame.display.update()