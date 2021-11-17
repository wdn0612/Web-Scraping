from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import constants

### DATA ###
property_listings = []
property_features = []
property_types = []
property_urls = []

### METHODS ###

def getPageUrl(page, element, value):
    return page + element + value


def getPropertyPage(main_page_url, driver):
    driver.get(main_page_url)
    time.sleep(10)
    description_div = driver.find_element_by_id(constants.PROPERTYGURU.description_div)
    next_page_class = driver.find_element_by_class_name(constants.PROPERTYGURU.next_pagination)
    next_page = get_next_page(next_page_class)
    # else:
    #     description_div = driver.find_element_by_class_name('_19sj7')
    return description_div, next_page


def getListings(description_div):
    listings = description_div.find_elements_by_class_name(constants.PROPERTYGURU.listing_identifier)
    for x in listings:
        property_listings.append(x.text)
        property_urls.append(x.find_element_by_tag_name('a').get_attribute('href'))


def getFeatures(description_div):
    features = description_div.find_elements_by_class_name(constants.PROPERTYGURU.feature_identifier)
    for x in features:
        feature = str(x.text)
        # Property without availability
        if (feature.startswith('S$')) and (len(feature.split('\n')) < 2):
            feature= feature + '\nNot Applicable'
        property_features.append(feature)


def getTypes(description_div):
    types = description_div.find_elements_by_class_name(constants.PROPERTYGURU.property_type_identifier)
    for x in types:
        property_types.append(x.text)


def getListingsInfo(description_div):
    getListings(description_div)
    getFeatures(description_div)
    getTypes(description_div)

def get_next_page(page):
    try:
        next_page_element = page.find_element_by_tag_name('a')
        next_page = next_page_element.get_attribute('href')
        print ('+'*20,
               '\nFound next page')
        return next_page
    except:
        print ('-'*20,
               '\nReached the last page')
        return None


def scrape(**kwargs):
    chrome_options = Options()
    #chrome_options.headless = True
    page_url = constants.PROPERTYGURU.main_url
    for k, v in kwargs.items():
        if k == 'mrt':
            for value in v:
                page_url = getPageUrl(page_url, constants.PROPERTYGURU.mrt_ep, value)
        if k == 'bedrooms':
            for value in v:
                page_url = getPageUrl(page_url, constants.PROPERTYGURU.bedroom_ep, value)
        if k == 'bathrooms':
            for value in v:
                page_url = getPageUrl(page_url, constants.PROPERTYGURU.bathroom_ep, value)
        if k == 'max_rent':
            page_url = getPageUrl(page_url, constants.PROPERTYGURU.max_price_ep, value)
        if k == 'min_rent':
            page_url = getPageUrl(page_url, constants.PROPERTYGURU.min_price_ep, value)
        if k == 'build_year':
            page_url = getPageUrl(page_url, constants.PROPERTYGURU.built_year_ep, value)

    while True:
        driver = webdriver.Chrome(constants.CHROMEDRIVER.chromeExecutable, options=chrome_options)
        print(f'===== Scraping from {page_url} =====')
        descriptions, next_page = getPropertyPage(page_url, driver)
        getListingsInfo(descriptions)
        driver.close()
        if next_page is None:
            break
        page_url = next_page
    driver.quit()
    return property_listings, property_features, property_types, property_urls


if __name__ == "__main__":
    ### 99 Co ###
    # descriptions = getPropertyPage("https://www.99.co/singapore/rent?query_ids=sg-mrt-queenstown", "99co")
    # ninetynine_listings = descriptions.find_elements_by_class_name("_1zvu5")
    # furnishments = descriptions.find_elements_by_class_name("QYieC")
    # for i in range(len(ninetynine_listings)):
    #     print ('='*20)
    #     print (ninetynine_listings[i].text)
    #     print (furnishments[i].text)

    print("----- Quitting Property GURU program... -----")
