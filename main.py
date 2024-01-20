#import
import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
fps = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Age of War gam")
timer = pygame.time.Clock()
main_menu = False
font = pygame.font.SysFont('freesansbold.ttf', 24)

def draw_menu():
    pass

def draw_game():
    menu_btn = pygame.draw.rect(screen, "light gray", [230, 450, 260, 40],0, 5)
    pygame.draw.rect(screen, "dark gray", [230, 450, 260, 40], 5, 5)
    text = font.render("Main menu ", True, "black")
    screen.blit(text, (245, 457))
run = True
while run:
    screen.fill("light blue")
    timer.tick(fps)
    if main_menu:
        draw_menu()
    else:
        draw_game()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()