import pygame
import math

class VerticalGyro:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Same surface size
        self.center = (100, 100)  # Center of the surface
        self.radius = 90  # Radius of the circular area

    def draw(self, pitch, roll=0):  # Add default value for roll
        # Reset surface
        self.surface.fill((0, 0, 0))

        # Create horizon surface
        horizon_surface = pygame.Surface((400, 400))

        # Fill surface with black
        horizon_surface.fill((0, 0, 0))

        # Draw horizontal lines for pitch
        for i in range(-40, 41, 10):
            y_pos = 200 + i * 5
            line_length = 50 if i == 0 else 25
            pygame.draw.line(horizon_surface, (255, 255, 255),
                             (200 - line_length, y_pos),
                             (200 + line_length, y_pos), 2)

        # Rotate and translate for pitch and roll
        rotated = pygame.transform.rotate(horizon_surface, roll)
        rect = rotated.get_rect(center=(100, 100 + pitch * 2))

        # Create circular mask
        mask = pygame.Surface((200, 200), pygame.SRCALPHA)
        pygame.draw.circle(mask, (255, 255, 255, 255), self.center, self.radius)

        # Draw artificial horizon
        self.surface.blit(rotated, (rect.x, rect.y))
        self.surface.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # Draw white central vertical line
        #pygame.draw.line(self.surface, (255, 255, 255), (100, 0), (100, 200), 3)

        # Draw white horizontal indicator line
        pygame.draw.line(self.surface, (255, 255, 255), (0, 100), (200, 100), 3)

        # Draw outer circle
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Add title
        font = pygame.font.Font(None, 14)  # Reduced font size
        text = font.render("VERTICAL GYRO", True, (255, 255, 255))
        text_rect = text.get_rect(center=(100, 150))  # Positioned at the top
        self.surface.blit(text, text_rect)

        return self.surface