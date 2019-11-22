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
acties.append(Actie(0, 5, "Geel"))
acties.append(Actie(1, 5, "Groen"))
acties.append(Actie(2, 5, "Wit"))
acties.append(Actie(3, 5, "Rood"))

while True:
    for actie in acties:
        print(actie.naam)
        leds[actie.index].on()
        sleep(actie.duurtijd)
        leds[actie.index].off()