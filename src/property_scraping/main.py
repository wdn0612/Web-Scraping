import user_queries
import scrape_guru
import df_processor
import send_notification
import datetime


def scrape(user_query_dict):
    websites = user_query_dict.get('Websites')
    print(user_query_dict)
    if '1' in websites:
        data = scrape_guru.scrape(mrt=user_query_dict.get('MRT'),
                                  bedrooms=user_query_dict.get('Bedrooms'),
                                  bathrooms=user_query_dict.get('Bathrooms'),
                                  max_rent=user_query_dict.get('Maximum Price'),
                                  min_rent=user_query_dict.get('Minimum Price'))
        createDf('guru', data)


def createDf(website, data):
    dfs = []
    if website == 'guru':
        print("===== Creating Dataframe from Property Guru =====")
        dfs.append(df_processor.property_guru_processor(data))
    return df_processor.merge_dfs(dfs)


def queryUserSelections():
    return user_queries.queryUserSelections()


if __name__ == '__main__':
    print(datetime.datetime.now())
    scrape(queryUserSelections())
    #send_notification.send_notification()
    print('***** Quit program *****')
    print(datetime.datetime.now())
