import pygame
import math

class TurnIndicator:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Taille de la surface
        self.center = (100, 100)  # Centre de l'indicateur
        self.radius = 90  # Rayon du cercle principal
        self.ball_radius = 10  # Rayon de la bille
        self.max_displacement = self.radius - 20  # Déplacement maximal de la bille

    def draw(self, roll):
        """
        Dessine l'indicateur de virage avec une bille.

        :param roll: Angle de roulis en degrés (-30 à +30 recommandé).
        """
        # Réinitialiser la surface
        self.surface.fill((0, 0, 0))

        # Dessiner le cercle extérieur
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Dessiner la ligne horizontale centrale
        pygame.draw.line(self.surface, (255, 255, 255), (10, 100), (190, 100), 2)

        # Calculer et limiter le déplacement de la bille
        displacement = (roll / 30) * self.max_displacement
        displacement = max(-self.max_displacement, min(self.max_displacement, displacement))

        # Dessiner la bille (noire avec un contour blanc)
        ball_x = self.center[0] + displacement
        ball_y = self.center[1] + 0  # Position sous la ligne centrale
        pygame.draw.circle(self.surface, (0, 0, 0), (int(ball_x), int(ball_y)), self.ball_radius)
        pygame.draw.circle(self.surface, (255, 255, 255), (int(ball_x), int(ball_y)), self.ball_radius, 2)

        # Ajouter le titre en bas
        font = pygame.font.Font(None, 14)  # Taille de la police
        text = font.render("TURN INDICATOR", True, (255, 255, 255))
        text_rect = text.get_rect(center=(100, 50))  # Positionnement
        self.surface.blit(text, text_rect)

        return self.surface


#
pygame.quit()
