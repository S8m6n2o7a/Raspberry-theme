#!/usr/bin/env python3

import subprocess

icons = input("Do you have .icons folder y/n\n").lower()
if icons == "y":
    subprocess.run('mkdir /home/pi/.icons', shell=True)
    
themes = input("Do you have .themes folder y/n\n").lower()
if themes == "y":
    subprocess.run('mkdir /home/pi/.themes', shell=True)
    
fonts = input("Do you have .fonts folder y/n\n").lower()
if fonts == "y":
    subprocess.run('mkdir /home/pi/.fonts', shell=True)
'''
subprocess.run('cd MacOs', shell=True)
subprocess.run('chmod +x *', shell=True)
subprocess.run('bash install.sh', shell=True)
'''
subprocess.run('sudo cp conky -rf /home/pi/.config/', shell=True)

subprocess.run('cd ..', shell=True)
subprocess.run('cd Dracula', shell=True)
subprocess.run('cp -rf * /home/pi/.themes', shell=True)

subprocess.run('cd ..', shell=True)
subprocess.run('cd Fonts', shell=True)
subprocess.run('cp -rf * /home/pi/.fonts', shell=True)

subprocess.run('cd ..', shell=True)
subprocess.run('cd Sweet-Rainbow', shell=True)
subprocess.run('cp -rf * /home/pi/.icons', shell=True)

subprocess.run('lxappearance', shell=True)