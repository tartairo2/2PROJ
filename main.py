import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Age of empire")

# Chargez l'image de fond
background_image = pygame.image.load("bg.jpeg")  # Assurez-vous de mettre le bon nom de fichier

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    # Dessinez l'image de fond
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# Déplacez pygame.quit() en dehors de la boucle while
pygame.quit()
