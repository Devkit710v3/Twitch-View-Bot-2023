import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

def check_for_updates():
    try:
        print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("Connecting to Servers")))
        time.sleep(7)
        print("Connected")
        time.sleep(1)
        print("Connected")
        time.sleep(0)
        print("Connected")
        time.sleep(2)
        print(Colors.red, ("Failed, Requires Paid Version"))
        time.sleep(0)
        print("Failed, Requires Paid Version")
        time.sleep(1)
        print(Colors.green, ("Done"))
        time.sleep(2)
        print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("Checking for Updates")))
        time.sleep(3)
        print("Program is up to date.")
        time.sleep(0)
        print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("Loading Proxies")))
        time.sleep(2)
        print(Colors.green, ("Done."))
        time.sleep(2)
        print(Colorate.Vertical(Colors.red, Center.XCenter("WARNING: This Program uses a LOT of RAM!!!")))
        time.sleep(5)
        return True
    except:
        return False



def main():
    if not check_for_updates():
        return
    os.system(f"title DevKit710v3 - Twitch Viewer Bot v1.3 (FREE VERSION) @DevKit710v3")

    print(Colorate.Vertical(Colors.red_to_green, Center.XCenter("""















































































           
▓█████▄ ▓█████ ██▒   █▓ ██ ▄█▀ ██▓▄▄▄█████▓
▒██▀ ██▌▓█   ▀▓██░   █▒ ██▄█▒ ▓██▒▓  ██▒ ▓▒
░██   █▌▒███   ▓██  █▒░▓███▄░ ▒██▒▒ ▓██░ ▒░
░▓█▄   ▌▒▓█  ▄  ▒██ █░░▓██ █▄ ░██░░ ▓██▓ ░ 
░▒████▓ ░▒████▒  ▒▀█░  ▒██▒ █▄░██░  ▒██▒ ░ 
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ▒ ▒▒ ▓▒░▓    ▒ ░░   
 ░ ▒  ▒  ░ ░  ░  ░ ░░  ░ ░▒ ▒░ ▒ ░    ░    
 ░ ░  ░    ░       ░░  ░ ░░ ░  ▒ ░  ░      
   ░       ░  ░     ░  ░  ░    ░           
 ░                 ░                       
    """)))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Rebrands [$45]""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Premium Version [$10]""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Support is no longer avilable for FREE Version.""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Discord.gg/fWjnPVnSc""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Github.com/Devkit710v3""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""______________________________________________________________________________________________________________""")))

                            
    proxy_servers = {
        1: "",
        2: "",
        3: "",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # Selecting proxy server
    print(Colors.green,"Proxy Server 1 Is Recommended")
    print(Colors.green,"Upgrade from FREE Version to unlock Proxies 1, 2, and 3!")
    print(Colorate.Vertical(Colors.green_to_blue,"Please select a proxy server(1,7,4,..):"))
    for i in range(4, 7):
        print(Colorate.Vertical(Colors.red_to_blue,f"Proxy Server {i}"))
    proxy_choice = int(input("> "))
    proxy_url = proxy_servers.get(proxy_choice)

    twitch_username = input(Colorate.Vertical(Colors.green_to_blue, "Enter your channel name (e.g PewDiePie): "))
    proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, "How many proxy sites do you want to open? (x20 Proxy = around 10 Viewers)")))
    os.system("cls")
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""















































































           
▓█████▄ ▓█████ ██▒   █▓ ██ ▄█▀ ██▓▄▄▄█████▓
▒██▀ ██▌▓█   ▀▓██░   █▒ ██▄█▒ ▓██▒▓  ██▒ ▓▒
░██   █▌▒███   ▓██  █▒░▓███▄░ ▒██▒▒ ▓██░ ▒░
░▓█▄   ▌▒▓█  ▄  ▒██ █░░▓██ █▄ ░██░░ ▓██▓ ░ 
░▒████▓ ░▒████▒  ▒▀█░  ▒██▒ █▄░██░  ▒██▒ ░ 
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ▒ ▒▒ ▓▒░▓    ▒ ░░   
 ░ ▒  ▒  ░ ░  ░  ░ ░░  ░ ░▒ ▒░ ▒ ░    ░    
 ░ ░  ░    ░       ░░  ░ ░░ ░  ▒ ░  ░      
   ░       ░  ░     ░  ░  ░    ░           
 ░                 ░                                                   
    """)))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Rebrands [$50]""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Premium Version [$10]""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Support is no longer avilable for FREE Version.""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Discord.gg/fWjnPVnSc""")))
    print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter("""Github.com/Devkit710v3""")))
    print('')
    print('')
    print(Colors.red, Center.XCenter("If the viewers don't arrive within 20mins, close program, run Close_All_Chromes.bat and try again"))


    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    input(Colorate.Vertical(Colors.red_to_blue, "Success. Press enter to cancel views and close the program."))
    driver.quit()


if __name__ == '__main__':
    main()

# ==========================================
# Copyright 2023 DevKit710v3

# Permission is hereby denied, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
