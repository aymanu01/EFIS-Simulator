EFIS (Electronic Flight Instrument System) Simulation

Project Description

This project simulates a cockpit display system for an Electronic Flight Instrument System (EFIS). It includes key flight instruments such as the Attitude Indicator, Altimeter, Airspeed Indicator, Navigation Display, and Vertical Speed Indicator. The simulation is designed to provide an interactive environment to control and visualize critical flight parameters.

Features and Controls

Attitude Control (Pitch):

Arrow Up (↑): Increase pitch by 1 degree (maximum 40°).

Arrow Down (↓): Decrease pitch by 1 degree (minimum -40°).

Roll Control:

Arrow Left (←): Decrease roll by 1 degree (minimum -40°).

Arrow Right (→): Increase roll by 1 degree (maximum 40°).

Speed Control:

Key Z: Increase speed by 2 knots (maximum 1000 knots).

Key S: Decrease speed by 2 knots (minimum 0 knots).

Yaw Control (Lateral Movement):

Key Q: Decrease yaw by 1 degree (minimum -90°).

Key D: Increase yaw by 1 degree (maximum 90°).

Altitude Control:

Key E: Increase altitude by 50 feet (maximum 20,000 feet).

Key A: Decrease altitude by 50 feet (minimum 0 feet).

Requirements

Python: Version 3.8 or higher.

Libraries:

Pygame for graphical interface.

Pandas for data management.

Installation

Clone the repository:

git clone <repository-url>

Install the required libraries:

pip install pygame pandas

Run the simulation:

python main.py

Future Enhancements

Add more flight instruments for enhanced realism.

Implement 3D visualization for immersive experience.

Introduce real-time flight scenarios and dynamic weather conditions.

Enable network-based collaborative simulation.

Connect to real-world aeronautical data for live simulation.

Integrate with physical controls (joysticks, throttles, etc.).

License

This project is open-source and available under the MIT License.