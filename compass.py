import pygame
import math

class Compass:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Taille de la surface
        self.center = (100, 100)  # Centre du cercle
        self.radius = 90  # Rayon du cercle

        # Font setup
        self.font = pygame.font.SysFont("Arial", 16)  # Police pour les points cardinaux
        self.label_font = pygame.font.SysFont("Arial", 12)  # Police pour "Compass"

    def draw(self, yaw):
        self.surface.fill((0, 0, 0))  # Effacer la surface

        # Dessiner le cercle extérieur
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Points cardinaux
        cardinal_points = {"N": 0, "E": 90, "S": 180, "W": 270}

        for cardinal, angle_deg in cardinal_points.items():
            angle_rad = math.radians(angle_deg - 90)  # Alignement vers le haut
            text_pos = (
                self.center[0] + (self.radius - 20) * math.cos(angle_rad),
                self.center[1] + (self.radius - 20) * math.sin(angle_rad)
            )
            text = self.font.render(cardinal, True, (255, 255, 255))
            text_rect = text.get_rect(center=text_pos)
            self.surface.blit(text, text_rect)

        # Tracer les graduations pour 360 degrés (tous les 30°)
        for i in range(0, 360, 30):
            angle_rad = math.radians(i - 90)  # Début au sommet
            start_pos = (
                self.center[0] + (self.radius - 10) * math.cos(angle_rad),
                self.center[1] + (self.radius - 10) * math.sin(angle_rad)
            )
            end_pos = (
                self.center[0] + self.radius * math.cos(angle_rad),
                self.center[1] + self.radius * math.sin(angle_rad)
            )
            pygame.draw.line(self.surface, (255, 255, 255), start_pos, end_pos, 2)

        # Aiguille
        needle_angle = math.radians(yaw - 90)
        needle_end_pos = (
            self.center[0] + (self.radius - 20) * math.cos(needle_angle),
            self.center[1] + (self.radius - 20) * math.sin(needle_angle)
        )
        pygame.draw.line(self.surface, (255, 0, 0), self.center, needle_end_pos, 3)

        # Nom du composant ("Compass")
        label = self.label_font.render("Compass", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.center[0], self.center[1] + 40))  # Ajusté à la taille
        self.surface.blit(label, label_rect)

        return self.surface
