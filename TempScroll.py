from microbit import *

#Scrolls the current temperature on the dipslay
def ScrollCurrentTemp(curr):
    display.scroll("CURRENT TEMP: " + str(curr) + "F")

#Scrolls the average temperature on the display.  Uses getAvg
def ScrollAvgTemp(avg):   
    display.scroll("AVG TEMP: " + str(avg) + "F")
    
#Displays a symbol corresponding to the temperature    
def weather(temp):
    if temp < 30:
        display.show(snow)
    if temp >= 30 and temp < 50:
        display.show(Image.MEH)
    if temp >= 50 and temp < 80:
       display.show(Image.HAPPY)
    if temp >= 80:
        display.show(Image.SAD)
        
#calculates the average temperature over a minute
def getAvg():
    total = 0
    for i in temps:
        total += i
    avg = round(total / len(temps))
    return avg
    
#scrolls the trend up, down or neutral
def ScrollTrend(temp, avg):
    if avg - temp < 0:
        display.show(Image.ARROW_N)
    elif avg - temp == 0:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.ARROW_S)
     
#initialize the main list and the snow image
snow = Image("90909:"
             "09990:"
             "99099:"
             "09990:"
             "90909")
temps = []
#init previous average
preAvg = (round(((temperature() - 3) * 9) / 5 + 32))
#loop FOREVER
while True:
    #gets the temperature from the board, -3 to adjust for the board heating up
    temp = (round(((temperature() - 3) * 9) / 5 + 32))
    #adds the temp to the list
    temps.append(temp)
    sleep(500)
    ScrollCurrentTemp(temp)
    sleep(800)
    #shows the weather images
    weather(temp)
    sleep(500)
    #shows the average
    ScrollAvgTemp(getAvg())
    weather(temp)
    #shows the trend
    ScrollTrend(temp, getAvg())
    sleep(1000)
    #clears the average after 5 minutes
    if len(temps) == 300:
        temps[:]=[]
        
    