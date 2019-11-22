# Hoe werk het?

## Voorbereiding op de PI zelf
- installeer raspian als basis OS
- installeer samba en deel een "share" folder zodat je er vanuit windows aan kan
- zet ssh aan
- verbind met je wifi netwerk

## Voorbereiding op je windows
- installeer VS code
- installeer de VS code python extensie
- maak een netwerkverbinding met \\192.168.?.?\share
- open de folder \\192.168.?.?\share\Git\Treintafel in VS code
- je kan beginnen programmeren

## Het programma starten
- ssh pi@192.168.?.?
- wachtwoord invullen
- gebruik deze commando's op naar het programma te gaan en het op te starten

        cd /share/Git/Treintafel
        python app.py
- het programma stoppen doe je met Ctrl-C

