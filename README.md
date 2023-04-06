# CropStar

CropStar is a Python project that automates the irrigation of plants and provides notifications for irrigation events. With CropStar, you can easily schedule and manage your plant watering needs, ensuring that your plants receive the right amount of water at the right time.

Features
CropStar includes the following features:

- Automated irrigation scheduling: You can set up watering schedules for your plants and CropStar will automatically water them according to your settings.
- Flexible scheduling options: CropStar offers a range of scheduling options, including daily, weekly, and custom schedules.
- Customizable watering settings: You can customize the amount of water and the frequency of watering for each plant, ensuring that each plant receives the right amount of water for its needs.
- Automatic notifications: CropStar can send you notifications when watering events occur, so you can stay informed about your plants' watering status.
- User-friendly interface: CropStar features an easy-to-use web interface that allows you to manage your plant watering needs with ease.


## Getting Started

To get started with CropStar, you'll need to install the required dependencies and set up your irrigation hardware. Once you've done that, you can configure your watering schedules and start automating your plant watering tasks.

## Requirements

- Python 3.9
- RPi.GPIO (if running on a Raspberry Pi)
- A compatible 120v relay module (if running on a Raspberry Pi)

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using pip: `pip install -r requirements.txt`.
3. Configure the `config.ini` file with your irrigation schedule and any other settings you need.
4. Run the `main.py` file to start the system: `python main.py`.

## Configuration

Updating AWS Access Key and Phone Number

Open your Python script in a text editor or IDE.
Locate the section of the script where the AWS access key material is defined. This is usually near the top of the script and will look something like this:
```python
sns = boto3.client('sns',
    region_name='us-east-1',
    aws_access_key_id='YOUR_ACCESS_KEY_HERE',
    aws_secret_access_key='YOUR_SECRET_KEY_HERE')
number = '+PHONE_NUMBER'
```

Replace the PHONE_NUMBER, YOUR_ACCESS_KEY_HERE and YOUR_SECRET_KEY_HERE placeholders with your phone number, AWS access key and secret key.

That's it! Your Python script should now be using the updated AWS access key material for all AWS operations. Be sure to keep your access key and secret key secure and never commit them to version control.

Changing Irrigation Schedule

```python
# Replenishment Shots
schedule.every().day.at("11:00").do(daily_steering, shot_time = 90)
schedule.every().day.at("11:20").do(daily_steering, shot_time = 90)
schedule.every().day.at("11:40").do(daily_steering, shot_time = 90)
schedule.every().day.at("12:00").do(daily_steering, shot_time = 90)
schedule.every().day.at("12:20").do(daily_steering, shot_time = 90)
schedule.every().day.at("12:40").do(daily_steering, shot_time = 90)
schedule.every().day.at("13:00").do(daily_steering, shot_time = 70)
# Refreshment Shots
schedule.every().day.at("15:00").do(daily_steering, shot_time = 70)
schedule.every().day.at("17:00").do(daily_steering, shot_time = 70)
schedule.every().day.at("19:00").do(daily_steering, shot_time = 10)
```
Usage
Once you have the system set up and configured, you can start it by running the main.py file:

```python
python main.py
```
The system will automatically turn on and off the irrigation system according to the schedule you configured in the config.ini file.


License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
