import atexit
from gpiozero import LEDBoard
from time import sleep

print("Start brug-programma")

leds = LEDBoard(17, 18, 15, 27)

class Actie(object):
    def __init__(self, index, duurtijd, naam):
        self.index = index
        self.duurtijd = duurtijd
        self.naam = naam

acties = []
acties.append(Actie(0, 1, "Geel"))
acties.append(Actie(1, 1, "Groen"))
acties.append(Actie(2, 1, "Wit"))
acties.append(Actie(3, 1, "Rood"))


def exit_app():
    print("Stop brug-programma, doe alle leds uit")
    for led in leds[:]:
        led.off()

atexit.register(exit_app)

while True:
    for actie in acties:
        print(actie.naam)
        leds[actie.index].on()
        sleep(actie.duurtijd)
        leds[actie.index].off()