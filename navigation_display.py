import pygame
import math


class NavigationDisplay:
    def __init__(self):
        self.surface = pygame.Surface((500, 800))
        self.airports = {
            'CDG': (250, 200),  # Paris
            'CMN': (200, 600),  # Casablanca
            'JFK': (100, 400),  # New York
            'DOH': (400, 500)   # Doha
        }
        self.plane_pos = [250, 400]  # Position initiale de l'avion

    def draw(self, speed, yaw):
        # Réinitialise la surface
        self.surface.fill((0, 0, 0))

        # Dessiner les lignes de la grille
        for x in range(0, 501, 50):
            pygame.draw.line(self.surface, (50, 50, 50), (x, 0), (x, 800))
        for y in range(0, 801, 50):
            pygame.draw.line(self.surface, (50, 50, 50), (0, y), (500, y))

        # Dessiner les aéroports
        for code, pos in self.airports.items():
            pygame.draw.circle(self.surface, (0, 255, 0), pos, 5)
            font = pygame.font.Font(None, 24)
            text = font.render(code, True, (0, 255, 0))
            self.surface.blit(text, (pos[0] + 10, pos[1] - 10))

        # Réduction de la vitesse
        reduced_speed = speed / 200 # Divise la vitesse par 10 pour ralentir le mouvement

        # Mettre à jour la position de l'avion en fonction de la vitesse réduite et du cap (yaw)
        angle = math.radians(-yaw)  # Conversion en radians
        self.plane_pos[0] = (self.plane_pos[0] + math.cos(angle) * reduced_speed) % 500
        self.plane_pos[1] = (self.plane_pos[1] - math.sin(angle) * reduced_speed) % 800  # Y inversé

        # Dessiner l'avion comme un point
        pygame.draw.circle(self.surface, (255, 255, 255), (int(self.plane_pos[0]), int(self.plane_pos[1])), 5)

        return self.surface
