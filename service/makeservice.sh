#!/bin/bash

cd /share/Git/Treintafel/service
sudo cp treinenapp.service /etc/systemd/system/treinenapp.service
sudo cp treinenapp-watcher.service /etc/systemd/system/treinenapp-watcher.service
sudo cp treinenapp-watcher.path /etc/systemd/system/treinenapp-watcher.path
sudo systemctl enable treinenapp.service
sudo systemctl enable treinenapp-watcher.service
sudo systemctl enable treinenapp-watcher.path
sudo systemctl start treinenapp.service
sudo systemctl start treinenapp-watcher.service
sudo systemctl start treinenapp-watcher.path
