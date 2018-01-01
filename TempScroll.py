from microbit import *

#Scrolls the current temperature on the dipslay
def ScrollCurrentTemp():
    curr = temperature() - 3
    curr = round((curr * 9) / 5 + 32)
    display.scroll(str(curr) + "F")

#Scrolls the average temperature on the display.  Uses getAvg
def ScrollAvgTemp():
    avg = getAvg()   
    display.scroll(str(avg) + "F")
    
#Displays a symbol corresponding to the temperature    
def weather(temp):
    temp = round((temp * 9) / 5 + 32)
    if temp < 30:
        #needs replaced. this is a "tree"
        display.show(Image.XMAS)
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
    avg = round((((total / len(temps)) * 9) / 5) + 32)
    return avg
     
#initialize the main list     
temps = []
#loop FOREVER
while True:
    #gets the temperature from the board, -3 to adjust for the board heating up
    temp = (temperature() - 3)
    #adds the temp to the list
    temps.append(temp)
    if button_a.was_pressed():
        ScrollCurrentTemp()
    if button_b.was_pressed():
        ScrollAvgTemp()
    weather(temp)
    sleep(1000)
    #prints the average temperature every minute
    if len(temps) == 60:
        print(str(getAvg()))
    #clears the average after 10 minutes
    if len(temps) == 600:
        temps[:]=[]
        
    