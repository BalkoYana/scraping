from requests import get
from bs4 import BeautifulSoup


BASE_URL = "https://kpi.ua"
URL = f"{BASE_URL}/kpi_faculty"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content,"html.parser")

fac_list = soup.find(class_="main-container")

ul = fac_list.select('div > ul')[1]

for li in ul.find_all("li"):
    a=li.find("a")
    name=a.find(string=True,recursive=False)
    fac_link=BASE_URL+ a.get("href")
    print(f"Назва факультету:{name}")
    print(f"URL:{fac_link}")
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    fac_page=get(fac_link,headers=HEADERS)
    soup=BeautifulSoup(fac_page.content,"html.parser")
    field_item=soup.select(".field-item > a")[3:6]
    if field_item:
        for li in field_item:
            dep_name = li.find(string=True, recursive=False)
            dep_url = BASE_URL + li.get("href")
            print(f" Назва кафедри:{dep_name}")
            print(f" URl:{dep_url}")
            #/////////////////////////////////////////////
            dep_page=get(f"{dep_url}",headers=HEADERS)
            soup=BeautifulSoup(dep_page.content,"html.parser")
            news_list=soup.find(class_="item-list")
            if news_list:
                for li in news_list.find_all("li"):
                    name=li.a.find(string=True,recursive=False)
                    print(f"новини  {name}")







