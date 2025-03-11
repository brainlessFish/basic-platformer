import pygame
pygame.init()

def main():

    clock = pygame.time.Clock()
     
    #Window 
    window = pygame.display.set_mode((500,500))
    title = pygame.display.set_caption("Basic Platformer gam")

    #Background
    bg = pygame.Surface(window.get_size()).convert()

    #Text
    text1 = pygame.font.Font("Pixeltype.ttf",25).render("Use arrows keys to move",None,"White")
    text1Box = text1.get_rect(center=(250,50))
    
    #objects

    #Player
    player = pygame.Surface((20,20)).convert()
    pBox = player.get_rect(midleft=(0,480))
    player.fill("White")
    gravity = 1

    while True:
        
        #Update
        bg.blit(text1,(text1Box))
        bg.blit(player,(pBox))
        window.blit(bg,(0,0))
        bg.fill("black")
        
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #Movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_SPACE] or key[pygame.K_UP]) and key[pygame.K_RIGHT]:
            pBox.x += 3
            if pBox.y >= 475:
                gravity -= 20
        elif (key[pygame.K_SPACE] or key[pygame.K_UP]) and key[pygame.K_LEFT]:
            pBox.x -= 3
            if pBox.y >= 475:
                gravity -= 20
        else:
            if key[pygame.K_RIGHT]: pBox.x += 3
            elif key[pygame.K_LEFT]: pBox.x -= 3
            elif key[pygame.K_SPACE] or key[pygame.K_UP]: 
                if pBox.y >= 475:
                    gravity -= 20
        
        #Player Gravity
        pBox.y += gravity
        gravity += 1
        if pBox.y >= 480:
            gravity = 1
            pBox.y = 480

    
        clock.tick(60)
        pygame.display.flip()
        
        
main()