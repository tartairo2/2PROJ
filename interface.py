import sys
import pygame

class Interface:
    def __init__(self):
        pygame.init()

        # Obtenir la taille de l'écran du moniteur principal
        info_object = pygame.display.Info()
        self.screen_width = info_object.current_w
        self.screen_height = info_object.current_h

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Age of Empire")

        self.clock = pygame.time.Clock()
        self.running = True

        # Chargement de l'image de fond et redimensionnement
        self.background_image = pygame.image.load("bg.jpeg")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))

        # Définir les couleurs
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (225, 255, 255)

        # Définir la police
        self.font = pygame.font.Font(None, 36)

        # Créer les boutons
        self.create_buttons()

    def create_buttons(self):
        # Définir les dimensions des boutons
        button_width = 150
        button_height = 50

        # Calculer les positions des boutons pour les placer au centre
        self.button1_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 - 100,
                                        button_width, button_height)
        self.button2_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2, button_width,
                                        button_height)
        self.button3_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 + 100,
                                        button_width, button_height)
        self.button_alpha = 150  # Ajustez la transparence ici (0 pour complètement transparent, 255 pour opacité complète)

        self.button1_color = self.GRAY + (self.button_alpha,)
        self.button2_color = self.GRAY + (self.button_alpha,)
        self.button3_color = self.GRAY + (self.button_alpha,)

        self.button1_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        self.button2_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        self.button3_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)

        self.button1_surface.fill(self.button1_color)
        self.button2_surface.fill(self.button2_color)
        self.button3_surface.fill(self.button3_color)

        self.button1_text = self.font.render(" 1 VS 1", True, self.BLACK)
        self.button2_text = self.font.render(" 1 VS IA", True, self.BLACK)
        self.button3_text = self.font.render("Quitt", True, self.BLACK)

    def check_button_click(self, button_rect, button_index, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    print(f"Button {button_index} clicked")
                    if button_index == 3:  # Bouton "Quitt"
                        pygame.quit()
                        sys.exit()

    def draw_buttons(self):
        self.screen.blit(self.button1_surface, self.button1_rect.topleft)
        self.screen.blit(self.button2_surface, self.button2_rect.topleft)
        self.screen.blit(self.button3_surface, self.button3_rect.topleft)

        # Dessinez le texte des boutons
        self.screen.blit(self.button1_text, (self.button1_rect.x + 20, self.button1_rect.y + 15))
        self.screen.blit(self.button2_text, (self.button2_rect.x + 20, self.button2_rect.y + 15))
        self.screen.blit(self.button3_text, (self.button3_rect.x + 20, self.button3_rect.y + 15))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_button_click(self.button1_rect, 1, events)
                    self.check_button_click(self.button2_rect, 2, events)
                    self.check_button_click(self.button3_rect, 3, events)


    def update(self):
        pass

    def draw(self):
        # Dessinez l'image de fond redimensionnée
        self.screen.blit(self.background_image, (0, 0))

        # Dessinez les boutons
        self.draw_buttons()

        pygame.display.update()
        self.clock.tick(60)