import pygame #impordib pygame
pygame.init() #Koostab selle programmi
#ekraani seaded
screen=pygame.display.set_mode([300,700]) #valib ekraani suuruse
pygame.display.set_caption("Valgusfoor") #Lisab aknale nime

#joonistamine
pygame.draw.rect(screen, [255, 255, 255], [90, 10, 130, 280], 2) #loob ristküliku [värv], [[x, y, w, h], joone_paksus)
pygame.draw.circle(screen, [255, 0, 0], [155,63], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen, [236, 240, 0], [155,152], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.circle(screen,[0, 255, 0], [155,240], 40, 0) #loob ringi [värv] ,[(screen, värv, tsentri_pos, raadius, joone_paksus)
pygame.draw.line,[1, 15, 400]
pygame.display.flip() #värskendab aknaid
running = True #Hoiab programmi tööle

while running: #Loop
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get(): # Alustab programm mis paneb akna kinni
        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False