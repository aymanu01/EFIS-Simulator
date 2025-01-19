import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Plotta(QMainWindow):
    def __init__(self):
        super().__init__()

        # Charger les données depuis le fichier Excel
        self.data = pd.read_excel("flight_data.xlsx")

        # Créer la fenêtre principale
        self.setWindowTitle("Flight Data Visualization")
        self.setGeometry(100, 100, 1920, 1080)

        # Définir l'icône de la fenêtre
        self.setWindowIcon(QIcon('plooo.png'))  # Assurez-vous que plooo.png est dans le bon répertoire

        # Créer un widget central et un layout vertical
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Ajouter la barre d'outils Matplotlib
        toolbar = NavigationToolbar(FigureCanvas(plt.figure()), self)
        layout.addWidget(toolbar)

        # Créer le canevas de Matplotlib pour afficher les graphiques
        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)

        # Diviser la fenêtre en 6 zones pour afficher les courbes
        self.plot_data()

        # Mettre à jour l'apparence de l'interface
        central_widget.setStyleSheet("background-color: #2E2E2E;")
        self.setStyleSheet("background-color: #2E2E2E;")

        self.setCentralWidget(central_widget)

    def plot_data(self):
        # Définir un fond sombre pour Matplotlib
        plt.style.use('dark_background')

        # Créer un subplot avec 2 lignes et 3 colonnes (pour 6 graphiques)
        fig, axs = plt.subplots(2, 3, figsize=(16, 9))

        # Tracer les courbes sur les sous-graphes
        axs[0, 0].plot(self.data.index, self.data['altitude'], label="Altitude")
        axs[0, 0].set_title("Altitude", color='white')
        axs[0, 0].set_xlabel("Time", color='white')
        axs[0, 0].set_ylabel("Altitude (ft)", color='white')

        axs[0, 1].plot(self.data.index, self.data['pitch'], label="Pitch", color='orange')
        axs[0, 1].set_title("Pitch", color='white')
        axs[0, 1].set_xlabel("Time", color='white')
        axs[0, 1].set_ylabel("Pitch (degrees)", color='white')

        axs[0, 2].plot(self.data.index, self.data['roll'], label="Roll", color='green')
        axs[0, 2].set_title("Roll", color='white')
        axs[0, 2].set_xlabel("Time", color='white')
        axs[0, 2].set_ylabel("Roll (degrees)", color='white')

        axs[1, 0].plot(self.data.index, self.data['yaw'], label="Yaw", color='red')
        axs[1, 0].set_title("Yaw", color='white')
        axs[1, 0].set_xlabel("Time", color='white')
        axs[1, 0].set_ylabel("Yaw (degrees)", color='white')

        axs[1, 1].plot(self.data.index, self.data['speed'], label="Speed", color='purple')
        axs[1, 1].set_title("Speed", color='white')
        axs[1, 1].set_xlabel("Time", color='white')
        axs[1, 1].set_ylabel("Speed (knots)", color='white')

        axs[1, 2].plot(self.data.index, self.data['vario'], label="Vario", color='brown')
        axs[1, 2].set_title("Vario", color='white')
        axs[1, 2].set_xlabel("Time", color='white')
        axs[1, 2].set_ylabel("Vario (kt)", color='white')

        # Ajuster l'espacement entre les sous-graphes
        plt.tight_layout()

        # Afficher les graphiques sur le canvas
        self.canvas.figure = fig
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Plotta()
    main_window.show()
    sys.exit(app.exec_())
