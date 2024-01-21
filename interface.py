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
        self.GRAY = (169, 169, 169)

        # Définir la police
        self.font = pygame.font.Font(None, 36)

        # État initial (page principale)
        self.current_page = "main"

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

        # Boutons de difficulté
        self.difficulty_buttons = self.create_difficulty_buttons()

    def create_difficulty_buttons(self):
        # Définir les dimensions des boutons pour la page des difficultés
        button_width = 200
        button_height = 50

        # Calculer les positions des boutons pour les placer au centre
        button_easy_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 - 150,
                                        button_width, button_height)
        button_medium_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 - 50,
                                        button_width, button_height)
        button_hard_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 + 50,
                                        button_width, button_height)
        button_hardest_rect = pygame.Rect((self.screen_width - button_width) // 2, self.screen_height // 2 + 150,
                                        button_width, button_height)

        button_alpha = 150  # Ajustez la transparence ici (0 pour complètement transparent, 255 pour opacité complète)

        button_easy_color = self.GRAY + (button_alpha,)
        button_medium_color = self.GRAY + (button_alpha,)
        button_hard_color = self.GRAY + (button_alpha,)
        button_hardest_color = self.GRAY + (button_alpha,)

        button_easy_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        button_medium_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        button_hard_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        button_hardest_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)

        button_easy_surface.fill(button_easy_color)
        button_medium_surface.fill(button_medium_color)
        button_hard_surface.fill(button_hard_color)
        button_hardest_surface.fill(button_hardest_color)

        button_easy_text = self.font.render("Easy", True, self.BLACK)
        button_medium_text = self.font.render("Medium", True, self.BLACK)
        button_hard_text = self.font.render("Hard", True, self.BLACK)
        button_hardest_text = self.font.render("Hardest", True, self.BLACK)

        return {
            "easy": {"rect": button_easy_rect, "surface": button_easy_surface, "text": button_easy_text},
            "medium": {"rect": button_medium_rect, "surface": button_medium_surface, "text": button_medium_text},
            "hard": {"rect": button_hard_rect, "surface": button_hard_surface, "text": button_hard_text},
            "hardest": {"rect": button_hardest_rect, "surface": button_hardest_surface, "text": button_hardest_text}
        }

    def check_button_click(self, button_rect, button_index, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    print(f"Button {button_index} clicked")
                    if button_index == 3:  # Bouton "Quitt"
                        pygame.quit()
                        sys.exit()
                    elif button_index == 2:  # Bouton "1 VS IA"
                        self.current_page = "difficulty"
                    elif self.current_page == "difficulty":
                        for difficulty, button_info in self.difficulty_buttons.items():
                            if button_info["rect"].collidepoint(event.pos):
                                print(f"{difficulty.capitalize()} difficulty selected")

    def draw_buttons(self):
        if self.current_page == "main":
            self.screen.blit(self.button1_surface, self.button1_rect.topleft)
            self.screen.blit(self.button2_surface, self.button2_rect.topleft)
            self.screen.blit(self.button3_surface, self.button3_rect.topleft)

            # Dessinez le texte des boutons
            self.screen.blit(self.button1_text, (self.button1_rect.x + 20, self.button1_rect.y + 15))
            self.screen.blit(self.button2_text, (self.button2_rect.x + 20, self.button2_rect.y + 15))
            self.screen.blit(self.button3_text, (self.button3_rect.x + 20, self.button3_rect.y + 15))
        elif self.current_page == "difficulty":
            for button_info in self.difficulty_buttons.values():
                self.screen.blit(button_info["surface"], button_info["rect"].topleft)
                self.screen.blit(button_info["text"], (button_info["rect"].x + 20, button_info["rect"].y + 15))

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
