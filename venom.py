import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore
import random 
import os
os.system('clear')
w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
c = Fore.CYAN
y = Fore.YELLOW

colors = (w, g, r, b, c, y)
color = random.choice(colors)

banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ███████╗██████╗ ██████╗  ██████╗ ██████╗       ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗      ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝█████╗███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗╚════╝╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║      ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝      ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝

     [+] Created By Venom
     [+] Instagram -: i.m.gauravchaudhary                                                                                                                                                
     [+] Whatsapp -: +91 9910332273
     
'''

print(color + banner + color)
error = input(w + '    [+] ' + w + color + 'Enter your error: ' + color)
url = 'https://www.google.com/search?q=' + error
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
ok = soup.find_all('div', class_='kCrYT')
ok = str(ok)
new = re.findall('<a href="(.*?)"', ok)
new_link = len(new)
answer = []
solutions = []
x = 0
if new_link > 1:
    for i in new:
        i = str(i)
        if i.startswith('/url?q=') is True:
            i = i[7:-100]
            if i.startswith('https://stackoverflow.com/') is True:
                _response = requests.get(i)
                _soup = BeautifulSoup(_response.content, 'html.parser')     
                solution = _soup.find('div', id="answers")
                try:
                    for answers in solution.find_all('div', class_="s-prose js-post-body"):
                        print(w + '<----------------' + w + g + ' Answer ' + str(x) + g + w + '------------------->'+ w)
                        print(color + answers.get_text() + color)                   
                        x += 1
                except TypeError as e:
                    pass
            else:
                pass
        else:
            pass

