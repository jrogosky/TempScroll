from microbit import *

def ScrollCurrentTemp():
    curr = temperature()
    curr = round((curr * 9) / 5 + 32)
    display.scroll(str(curr) + "°F")

def ScrollAvgTemp():
    total = 0
    for i in temps:
        total += i
    avg = round((((total / len(temps)) * 9) / 5) + 32)
    display.scroll(str(avg) + "°F")
    
def weather(temp):
    temp = round((temp * 9) / 5 + 32)
    if temp < 30:
        display.show(Image.XMAS)
    if temp >= 30 and temp < 50:
        display.show(Image.MEH)
    if temp >= 50 and temp < 80:
       display.show(Image.HAPPY)
    if temp >= 80:
        display.show(Image.SAD)
        
        
temps = []
while True:
    temp = temperature()
    temps.append(temp)
    if button_a.was_pressed():
        ScrollCurrentTemp()
    if button_b.was_pressed():
        ScrollAvgTemp()
    weather(temp)
    sleep(1000)
    if len(temps) == 600:
        temps[:]=[]
    