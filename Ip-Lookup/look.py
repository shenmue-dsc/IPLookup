import requests
import os
import pystyle
from pystyle import *
from colorama import *
import time

shenmue = "Le plus beau"
os.system('clear' if os.name == 'posix' else 'cls')

intro = """
                                                    By Shenmue & Sakunaxv2

                            ██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
                            ██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
                            ██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
                            ╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     

                                Veuillez cliquez sur entrez pour acceder au programme                                                                
"""
Anime.Fade(Center.Center(intro), Colors.blue_to_purple, Colorate.Vertical, interval=0.035, enter=True)

print(f"""{Fore.LIGHTBLUE_EX}
                            ██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
                            ██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
                            ██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
                            ██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
                            ██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
                            ╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                                                                                                                                                              
""")

ip = input("IP : ")
ipr = requests.get(f"http://ip-api.com/{ip}").text
print(ipr)
time.sleep(20)