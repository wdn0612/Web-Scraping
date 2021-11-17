
### Property Guru Constants ###

results_path = './/generated_results//rent_compilation_results.csv'

class CHROMEDRIVER:
    chromeExecutable = 'C:\\Users\\asus\\Downloads\\chromedriver'

class PROPERTYGURU:
    main_url = "https://www.propertyguru.com.sg/property-for-rent?market=residential&listing_type=rent"
    listing_identifier = 'header-container'
    feature_identifier = 'listing-features'
    property_type_identifier = 'listing-property-type'

    # ENDPOINTS #
    mrt_ep = "&MRT_STATIONS[]="
    bedroom_ep = "&beds%5B%5D="
    bathroom_ep = "&baths[]="
    max_price_ep = '&maxprice='
    min_price_ep = '&minprice='
    built_year_ep = ''

    description_div = 'listings-container'
    next_pagination = 'pagination-next'