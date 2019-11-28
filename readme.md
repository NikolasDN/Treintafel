# Hoe werk het?

## Voorbereiding op de PI zelf
- installeer raspian als basis OS
- installeer samba en deel een "share" folder zodat je er vanuit windows aan kan
- zet ssh aan
- verbind met je wifi netwerk

## Voorbereiding op je windows
- installeer VS code
- installeer de VS code python extensie
- maak een netwerkverbinding met \\raspberrypi\share
- open de folder \\raspberrypi\share\Git\Treintafel in VS code
- je kan beginnen programmeren

## Het programma starten
- ssh pi@raspberrypi
- wachtwoord invullen
- gebruik deze commando's op naar het programma te gaan en het op te starten

        cd /share/Git/Treintafel
        python app.py
- het programma stoppen doe je met Ctrl-C

## Het programma als service installeren
Je kan ervoor zorgen dat het programma start als de raspberry pi boot, en zichzelf opstart als het crasht. Het zou ook leuk zijn als het zichzelf heropstart als je iets in de app.py file aanpast want zo worden de aanpassingen meteen actief.

        cd /share/Git/Treintafel/service
        sudo cp treinenapp.service /etc/systemd/system/treinenapp.service
        sudo cp treinenapp-watcher.service /etc/systemd/system/treinenapp-watcher.service
        sudo cp treinenapp-watcher.path /etc/systemd/system/treinenapp-watcher.path
        sudo systemctl start treinenapp.service
        sudo systemctl start treinenapp-watcher.service
        sudo systemctl stop treinenapp.service
        sudo systemctl stop treinenapp-watcher.service
        sudo systemctl enable treinenapp.service
        sudo systemctl enable treinenapp-watcher.service
        sudo systemctl enable treinenapp-watcher.path

