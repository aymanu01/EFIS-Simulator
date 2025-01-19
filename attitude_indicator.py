import pygame
import math


class AttitudeIndicator:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Nouvelle taille de la fenêtre
        self.center = (100, 100)  # Centre du cercle ajusté
        self.radius = 90  # Rayon du cercle ajusté

    def draw(self, pitch, roll):
        # Reset surface
        self.surface.fill((0, 0, 0))

        # Create sky and ground surfaces
        horizon_surface = pygame.Surface((400, 400))  # Taille d'origine pour l'horizon

        # Fill sky (blue) and ground (brown)
        horizon_surface.fill((135, 206, 235))  # Sky blue
        pygame.draw.rect(horizon_surface, (139, 69, 19), (0, 200, 400, 200))  # Brown ground (ajusté)

        # Draw horizontal lines for pitch
        for i in range(-40, 41, 10):
            y_pos = 200 + i * 5  # Ajusté pour la nouvelle échelle
            line_length = 50 if i == 0 else 25  # Ligne plus courte
            pygame.draw.line(horizon_surface, (255, 255, 255),
                             (200 - line_length, y_pos),
                             (200 + line_length, y_pos), 2)

        # Rotate and translate for pitch and roll
        rotated = pygame.transform.rotate(horizon_surface, roll)
        rect = rotated.get_rect(center=(100, 100 + pitch * 2))  # Ajusté à la taille réduite

        # Create circular mask
        mask = pygame.Surface((200, 200), pygame.SRCALPHA)  # Surface plus petite
        pygame.draw.circle(mask, (255, 255, 255, 255), self.center, self.radius)

        # Draw artificial horizon
        self.surface.blit(rotated, (rect.x, rect.y))
        self.surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw outer circle
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        return self.surface
