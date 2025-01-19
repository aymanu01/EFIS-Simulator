import pygame
import math

class RadarAltimeter:
    def __init__(self):
        self.surface = pygame.Surface((200, 200))  # Réduction à 50 % de la taille initiale
        self.center = (100, 100)  # Centre ajusté
        self.radius = 90  # Rayon réduit à 50 % de l'original

        # Police pour afficher le nom de l'instrument
        self.font = pygame.font.SysFont("Arial", 14)  # Taille ajustée

    def draw(self, altitude):
        self.surface.fill((0, 0, 0))  # Effacer la surface

        # Dessiner le cercle extérieur
        pygame.draw.circle(self.surface, (255, 255, 255), self.center, self.radius, 2)

        # Dessiner les graduations
        for i in range(0, 5):  # 0 à 5 mètres
            angle = math.radians(i * 72 - 90)  # -90 pour commencer en haut
            start_pos = (
                self.center[0] + (self.radius - 10) * math.cos(angle),
                self.center[1] + (self.radius - 10) * math.sin(angle)
            )
            end_pos = (
                self.center[0] + self.radius * math.cos(angle),
                self.center[1] + self.radius * math.sin(angle)
            )
            pygame.draw.line(self.surface, (255, 255, 255), start_pos, end_pos, 2)

        # Dessiner l'aiguille
        angle = math.radians(altitude * 0.72 - 90)  # Pour altimètre radar
        end_pos = (
            self.center[0] + (self.radius - 20) * math.cos(angle),
            self.center[1] + (self.radius - 20) * math.sin(angle)
        )
        pygame.draw.line(self.surface, (255, 0, 0), self.center, end_pos, 3)

        # Afficher le nom de l'instrument ("Radar Altimeter")
        label = self.font.render("Radar Altimeter", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.center[0], self.center[1] + 40))  # Position sous le cercle
        self.surface.blit(label, label_rect)

        return self.surface
