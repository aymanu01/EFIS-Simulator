import pygame
import sys
import pandas as pd
from altimeter import Altimeter
from attitude_indicator import AttitudeIndicator
from navigation_display import NavigationDisplay
from speedometer import Speedometer
from variometer import Variometer
from compass import Compass
from radar_altimeter import RadarAltimeter
from vertical_gyro import VerticalGyro  # Importation de VerticalGyro
from turn_indicator import TurnIndicator  # Importation de TurnIndicator

class FlightSimulator:
    def __init__(self):
        pygame.init()

        # Nouvelle taille de l'écran
        self.screen = pygame.display.set_mode((1000, 900))
        pygame.display.set_caption("Flight Simulator")

        # Set the icon for the window (taskbar)
        self.icon = pygame.image.load('icone.png')  # Make sure 'icone.png' is in the same directory
        pygame.display.set_icon(self.icon)

        # Initialize instruments
        self.altimeter = Altimeter()
        self.attitude = AttitudeIndicator()
        self.nav_display = NavigationDisplay()
        self.speedometer = Speedometer()
        self.variometer = Variometer()
        self.compass = Compass()
        self.radar_altimeter = RadarAltimeter()
        self.vertical_gyro = VerticalGyro()  # Initialisation de VerticalGyro
        self.turn_indicator = TurnIndicator()  # Initialisation de TurnIndicator

        # Initialize flight variables
        self.altitude = 0  # 0-20000 ft
        self.pitch = 0  # -40 to 40 degrees
        self.roll = 0  # -40 to 40 degrees
        self.yaw = 0  # -90 to 90 degrees
        self.speed = 0  # 0-1000 knots
        self.vario = 0  # 0-20 kt

        # Control variables
        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize data storage
        self.data = []  # List to store flight data

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Pitch control (Up/Down)
        if keys[pygame.K_UP] and self.pitch < 40:
            self.pitch += 1
        if keys[pygame.K_DOWN] and self.pitch > -40:
            self.pitch -= 1

        # Roll control (Left/Right)
        if keys[pygame.K_LEFT] and self.roll > -40:
            self.roll -= 1
        if keys[pygame.K_RIGHT] and self.roll < 40:
            self.roll += 1

        # Speed control (Z/S)
        if keys[pygame.K_z] and self.speed < 1000:
            self.speed += 2
        if keys[pygame.K_s] and self.speed > 0:
            self.speed -= 2

        # Yaw control (Q/D)
        if keys[pygame.K_q] and self.yaw > -90:
            self.yaw -= 1
        if keys[pygame.K_d] and self.yaw < 90:
            self.yaw += 1

        # Altitude control (E/A)
        if keys[pygame.K_e] and self.altitude < 20000:
            self.altitude += 50
        if keys[pygame.K_a] and self.altitude > 0:
            self.altitude -= 50

        # Calculate variometer (vertical speed indicator)
        self.vario = (self.pitch * self.speed) / 100
        if self.vario > 20:
            self.vario = 20
        elif self.vario < 0:
            self.vario = 0

    def save_data(self):
        """
        Save the current flight data to an Excel file.
        """
        # Append the current data to the list
        self.data.append({
            "altitude": self.altitude,
            "pitch": self.pitch,
            "roll": self.roll,
            "yaw": self.yaw,
            "speed": self.speed,
            "vario": self.vario,
        })

        # Convert to DataFrame and save to Excel
        df = pd.DataFrame(self.data)
        df.to_excel("flight_data.xlsx", index=False)
        print("Data saved to flight_data.xlsx")

    def run(self):
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Handle keyboard input
            self.handle_input()

            # Save flight data
            self.save_data()

            # Clear screen
            self.screen.fill((0, 0, 0))

            # Draw instruments
            # Adjusting positions to fit the screen size
            # Left side
            self.screen.blit(self.altimeter.draw(self.altitude), (50, 50))
            self.screen.blit(self.attitude.draw(self.pitch, self.roll), (50, 250))
            self.screen.blit(self.variometer.draw(self.vario), (50, 450))

            # Center (Navigation Display)
            nav_surface = self.nav_display.draw(self.speed, self.yaw)
            self.screen.blit(nav_surface, (250, 50))

            # Right side
            self.screen.blit(self.speedometer.draw(self.speed), (750, 50))
            self.screen.blit(self.compass.draw(self.yaw), (750, 250))
            self.screen.blit(self.radar_altimeter.draw(self.altitude), (750, 450))

            # Draw Vertical Gyro in the bottom-right corner
            self.screen.blit(self.vertical_gyro.draw(self.pitch), (750, 650))  # Ajuster la position

            # Draw Turn Indicator in the bottom-left corner
            self.screen.blit(self.turn_indicator.draw(self.roll), (50, 650))  # Positionnement du Turn Indicator

            # Update display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    simulator = FlightSimulator()
    simulator.run()
