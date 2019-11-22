# Hoe laat je dit werken?

## Voorbereiding op de PI zelf
- installeer raspian als basis OS
- installeer samba en deel een "share" folder zodat je er vanuit windows aan kan
- zet ssh aan
- verbind met je wifi netwerk

## Voorbereiding op je windows
- installeer VS code
- installeer de VS code python extensie
- maak een netwerkverbinding met \\192.168.?.?\share
- open de folder \\192.168.?.?\share\Git\Treintafel

## Het programma starten
- ssh pi@192.168.?.?
- inloggen
- gebruik deze commando's op naar het programma te gaan en het op te starten

        cd /share/Git/Treintafel
        python brug.py
- het programma stoppen doe je met Ctrl-C

