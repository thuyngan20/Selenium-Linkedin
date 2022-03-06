from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep 

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./chromedriver",options=options)
driver.get("https://www.linkedin.com/login")

email = driver.find_element_by_id("username").send_keys("ngan23198@gmail.com")
passw = driver.find_element_by_id("password").send_keys("haikhongmuoitam")
submit = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').submit()

search_text = driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
search_text.send_keys("python developer"+ Keys.ENTER)
sleep(5)
see_all = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[2]/a').click()
sleep(10)
soup = BeautifulSoup(driver.page_source)
peoples = soup.find('ul', class_="reusable-search__entity-result-list list-style-none")
list_people = peoples.find_all('li', class_="reusable-search__result-container")
with open("text.txt","a+",encoding= "utf8") as f:
    f.write(str(peoples))
print(len(list_people))
# for p in list_people:
#     div_name = p.find('div', class_="t-roman t-sans")
#     name = div_name.find('a', class_="app-aware-link").getText()
#     print(name)
driver.close()
    

    