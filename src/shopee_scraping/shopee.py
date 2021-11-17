from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import pandas as pd

### DATA ###
items = []
original_prices = []
discounted_prices = []
discounts = []
urls =[]
delay = 3
df_columns = ["Product", "Original Price", "Discounted Price", "Discount (%)", "Product URL"]

### CONSTANTS ###
class PATH_CONSTANTS:
    chromeExecutable = 'C:\\Users\\asus\\Downloads\\chromedriver'

class IDENTIFIERS:
    productName = '//div[@class="attM6y"]'
    productOriginalPrice= '//div[@class="_2MaBXe"]'
    productDiscountedPrice = '//div[@class="Ybrg9j"]'
    productDiscount = '//div[@class="_3LRxdy"]'

### METHODS ###

def getPageUrl(page_number):

    return "https://shopee.sg/collections/371960/?order=desc&page="+str(page_number)+"&sortBy=price"

def getProductPage(main_page_url):
    driver.get(main_page_url)
    time.sleep(20)
    main_div = driver.find_elements_by_id('main')
    description_div = main_div[0].find_elements_by_class_name("_193wCc")
    description_div = description_div[0].find_element_by_class_name("_2XjODz")
    description_div = description_div.find_element_by_class_name("L4pcZ4")
    description_div = description_div.find_element_by_class_name("shopee-search-item-result")
    md_page_div = description_div.find_elements_by_xpath('.//div[@data-sqe="item"]')
    return md_page_div

def getProductUrlList(elems):
    product_urls = []
    for e in elems:
        try:
            a = e.find_element_by_tag_name("a")
            urls.append(a.get_attribute("href"))
            product_urls.append(a.get_attribute("href"))
        except:
            continue
    return product_urls

def printProductInfo(url):
    printProductName(url)
    printProductOriginalPrice(url)
    printProductDiscountedPrice(url)
    printProductDiscount(url)

def printProductName(url):
    printProductComponent(url, IDENTIFIERS.productName, "Product Name", items)

def printProductOriginalPrice(url):
    printProductComponent(url, IDENTIFIERS.productOriginalPrice, "Original Price", original_prices)

def printProductDiscountedPrice(url):
    printProductComponent(url, IDENTIFIERS.productDiscountedPrice,"Discounted Price", discounted_prices)

def printProductDiscount(url):
    printProductComponent(url, IDENTIFIERS.productDiscount, "Discount", discounts)

def printProductComponent(url, elem_identifier, component, component_list):
    try:
        element = driver.find_element_by_xpath(elem_identifier)
        print(element.text)
        component_list.append(element.text)
    except:
        print("%s not found at : %s"%(component, url))
        if component == "Discount":
            component_list.append("0")
        else:
            component_list.append("NIL")

def getProductsInformation(product_urls):
    for url in product_urls:
        print ("====="*10)
        try:
            driver.get(url)
            time.sleep(delay)
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'main')))
            printProductInfo(url)
        except TimeoutException:
            print ("Loading took too much time!")

def getProductDf(*args):
    df = pd.DataFrame(columns=df_columns)
    for i in range(len(df.columns)):
        col = df.columns[i]
        df[col] = args[i]
    df['Discount (%)']=df['Discount (%)'].str.split("%", expand=True)[0]
    df['Discount (%)']=df['Discount (%)'].astype(int)
    df.sort_values(by='Discount (%)', ascending=False, inplace=True)
    print (df)
    return df

def exportDf(df):
    df.to_csv(".//ShopeeDiscountProducts.csv", index=False)



### MAIN ###

if __name__=="__main__":
    for i in range(5):
        print ("----- Processing Page %d -----"%(i))
        page_url = getPageUrl(i)
        driver = webdriver.Chrome(PATH_CONSTANTS.chromeExecutable)
        product_list = getProductUrlList(getProductPage(page_url))
        getProductsInformation(product_list)

    df = getProductDf(items, original_prices, discounted_prices, discounts, urls)
    exportDf(df)
    print ("----- Quitting program... -----")
    driver.close()
    driver.quit()


