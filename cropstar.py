#!/usr/bin/python

import time
from datetime import datetime
from time import sleep
from uptime import uptime

import boto3
import RPi.GPIO as GPIO
import schedule

relay_pin = 17
sns = boto3.client('sns',
    region_name='us-east-1',
    aws_access_key_id='',
    aws_secret_access_key='')
number = '+'

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def daily_steering(shot_time):
    GPIO.output(relay_pin, True)
    print("Daily Steering - Turned Relay ON")
    send_sms_message("ON")

    sleep(shot_time)
    
    GPIO.output(relay_pin, False)
    print("Daily Steering - Turned Relay OFF")
    send_sms_message("OFF")

def send_sms_message(pump_state):
    try:
        sns.publish(PhoneNumber = number, Message='Irrigation Pump Power %s - DateTime: %s '%(pump_state, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    except:
        print("SMS Delivery Failed")
     
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
