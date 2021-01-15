import requests
from bs4 import BeautifulSoup
import urllib
url = "https://bubbletrends.herokuapp.com/trends"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
response = requests.get(url,headers=header)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
trends = []
for i in soup.find_all('tr'):
    number = i.find_all('td')[0].get_text()
    pdt_name = i.find_all('td')[1].get_text()
    no_of_results = i.find_all('td')[2].get_text()
    trends.append(f"{pdt_name} {no_of_results}")
    print(f"kindi {number}")
    print(pdt_name)
    print(no_of_results)
print(trends)    
# soup = BeautifulSoup(response.text,'html-parser')
# print(soup)