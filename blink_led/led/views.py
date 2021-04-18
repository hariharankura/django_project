from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO

LED_PIN = 24

def home(request):
    return HttpResponse('<h1>Control LED</h1>')

def turnOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 1)
    return HttpResponse('<h1>Turning on LED</h1>')

def turnOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 0)
    return HttpResponse('<h1>Turning off LED</h1>')