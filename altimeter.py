import pygame
import math


class Altimeter:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Réduction à 50 % de la taille initiale
        self.center = (100, 100)  # Centre ajusté
        self.radius = 90  # Rayon réduit à 50 % de l'original

    def draw(self, altitude):
        # Reset surface
        self.surface.fill((0, 0, 0))

        # Draw outer circle
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Draw graduations
        for i in range(0, 10):
            angle = math.radians(i * 36 - 90)  # -90 to start at top
            start_pos = (
                self.center[0] + (self.radius - 10) * math.cos(angle),
                self.center[1] + (self.radius - 10) * math.sin(angle)
            )
            end_pos = (
                self.center[0] + self.radius * math.cos(angle),
                self.center[1] + self.radius * math.sin(angle)
            )
            pygame.draw.line(self.surface, (255, 255, 255), start_pos, end_pos, 2)

            # Draw numbers
            font = pygame.font.Font(None, 18)  # Taille de police réduite
            value = i * 1000
            text = font.render(str(value), True, (255, 255, 255))
            text_pos = (
                self.center[0] + (self.radius - 20) * math.cos(angle) - text.get_width() / 2,
                self.center[1] + (self.radius - 20) * math.sin(angle) - text.get_height() / 2
            )
            self.surface.blit(text, text_pos)

        # Draw needle
        angle = math.radians((altitude % 10000) * 0.036 - 90)  # 360 degrees / 10000 ft = 0.036
        end_pos = (
            self.center[0] + (self.radius - 20) * math.cos(angle),
            self.center[1] + (self.radius - 20) * math.sin(angle)
        )
        pygame.draw.line(self.surface, (255, 0, 0), self.center, end_pos, 3)

        # Draw central text
        font = pygame.font.Font(None, 18)  # Taille de police réduite
        text = font.render("ALTIMETER", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.center)
        self.surface.blit(text, text_rect)

        return self.surface
