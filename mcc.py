import requests
import json
import keyboard
import time

print("""
██████╗░██╗███╗░░██╗██╗░░██╗░░░░░░██╗░░░░░░█████╗░██████╗░
██╔══██╗██║████╗░██║██║░██╔╝░░░░░░██║░░░░░██╔══██╗██╔══██╗
██████╦╝██║██╔██╗██║█████═╝░█████╗██║░░░░░███████║██████╦╝
██╔══██╗██║██║╚████║██╔═██╗░╚════╝██║░░░░░██╔══██║██╔══██╗
██████╦╝██║██║░╚███║██║░╚██╗░░░░░░███████╗██║░░██║██████╦╝
╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░
      
This code is made for the purpose of learning how to use the minecraft api.
      """)

def check_username(username):
    url = "https://api.mojang.com/users/profiles/minecraft/" + username
    response = requests.get(url)
    data = json.loads(response.text)
    return data

username = input("Enter the username: ")
data = check_username(username)
if "errorMessage" in data:
    print("Username avaliable")
else:
    print(username + """ is taken
          """)

if "id" in data:
    print("The ID of this username is: " + data["id"])

print("""
Made with love by sidney 
Github: https://github.com/Bink-lab/Minecraft-Name-Checker
      """)

print("Press 'esc' to exit")
keyboard.wait("esc")