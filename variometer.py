import pygame
import math


class Variometer:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Surface réduite à 50 % de la taille initiale
        self.center = (100, 100)  # Centre ajusté
        self.radius = 90  # Rayon réduit à 50 % de l'original

    def draw(self, vario):
        # Reset surface
        self.surface.fill((0, 0, 0))

        # Draw outer circle
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Draw graduations
        for i in range(21):  # 0 to 20 in steps of 1
            angle = math.radians(i * 13.5 - 225)  # Spread 270 degrees
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
            if i % 2 == 0:  # Draw numbers every 2 kt
                font = pygame.font.Font(None, 18)  # Font size reduced
                text = font.render(str(i), True, (255, 255, 255))
                text_pos = (
                    self.center[0] + (self.radius - 20) * math.cos(angle) - text.get_width() / 2,
                    self.center[1] + (self.radius - 20) * math.sin(angle) - text.get_height() / 2
                )
                self.surface.blit(text, text_pos)

        # Draw needle
        angle = math.radians(vario * 13.5 - 225)  # 270 degrees / 20 kt
        end_pos = (
            self.center[0] + (self.radius - 20) * math.cos(angle),
            self.center[1] + (self.radius - 20) * math.sin(angle)
        )
        pygame.draw.line(self.surface, (255, 0, 0), self.center, end_pos, 3)

        # Draw text
        font = pygame.font.Font(None, 18)  # Font size reduced
        text = font.render("VARIO", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.center[0], self.center[1] + 25))  # Adjusted position
        self.surface.blit(text, text_rect)

        return self.surface
