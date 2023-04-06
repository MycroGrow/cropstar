# CropStar

This Python project provides a command-line interface (CLI) for managing irrigation by schedule. With this system, you can set up a schedule for when you want your plants to be watered, and the system will automatically turn on and off the irrigation system at the appropriate times.

## Requirements

- Python 3.x
- RPi.GPIO (if running on a Raspberry Pi)
- A compatible relay module (if running on a Raspberry Pi)

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using pip: `pip install -r requirements.txt`.
3. Configure the `config.ini` file with your irrigation schedule and any other settings you need.
4. Run the `main.py` file to start the system: `python main.py`.

## Configuration

The `config.ini` file contains the settings for the irrigation schedule and other options. Here's an example configuration:

```ini
[irrigation]
# Start time for the irrigation (24-hour format)
start_time = 6:00

# End time for the irrigation (24-hour format)
end_time = 7:00

# Duration of irrigation in seconds
duration = 60

# Interval between irrigation cycles in seconds
interval = 86400

[system]
# Pin number for the relay (BCM mode)
pin = 18

# Set to True if the relay is active low
active_low = False
```
Usage
Once you have the system set up and configured, you can start it by running the main.py file:

```sh
python main.py
```
The system will automatically turn on and off the irrigation system according to the schedule you configured in the config.ini file.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
