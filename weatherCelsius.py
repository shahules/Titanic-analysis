
# coding: utf-8



#coder:Shahules786 
import requests
from bs4 import BeautifulSoup
from math import floor as f
from termcolor import colored

res=requests.get("https://www.msn.com/en-us/weather")
bsobj=BeautifulSoup(res.text,"html.parser")
ftemp=bsobj.find("span",{"class":"current"})
temp=int(ftemp.get_text())
tempc=(temp-32)*5/9
print(colored(str(f(tempc))+"°C","white"))





