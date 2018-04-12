from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities.FIREFOX
caps['marionette'] = False
binary = FirefoxBinary(r'F:\Program Files (x86)\Mozilla Firefox\firefox.exe')
fp = webdriver.FirefoxProfile()
fp = fp.set_preference("permissions.default.stylesheet",2)
driver = webdriver.Firefox(firefox_binary=binary,firefox_profile=fp,capabilities=caps)
# driver = webdriver.Chrome()
for i in range(20):
    driver.get("https://zh.airbnb.com/s/Shenzhen-China/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=_45KiJet&section_offset="+str(i))
    rent_list = driver.find_elements_by_css_selector("div._v72lrv")
    for eachhouse in rent_list:
        comment = eachhouse.find_element_by_css_selector("div._17djt7om")
        comment = comment.text
        price = eachhouse.find_element_by_css_selector("div._59f9ic")
        price = price.text[4:]
        fangxin = eachhouse.find_element_by_tag_name('span')
        fangxin = fangxin.text
        evaluate = eachhouse.find_element_by_css_selector("div._1hc6xcl")
        evaluate = evaluate.text
        print("评论"+evaluate+"，价格"+price,fangxin,comment+"\n")
