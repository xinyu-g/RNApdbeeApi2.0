from selenium import webdriver

driver = webdriver.Chrome("C:/Users/zaloguj/IdeaProjects/RNApdbee/driver/chromedriver.exe")

driver.get('http://rnapdbee.cs.put.poznan.pl')

for i in driver.find_elements_by_name("basePairAnalyzer"):
    i.click()