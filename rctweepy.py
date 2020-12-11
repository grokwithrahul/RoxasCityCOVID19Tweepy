import tweepy
from datetime import datetime
import re
# import image_to_text if already have screenshots and tweet directly
# import image_to_text


def v1():
    # # V 1.0.0 code
    # # start

    # # GET DATA FROM https://covid19stats.ph/stats/by-location/roxas-city-capiz
    # # start "Get Data"
    # r = requests.get('https://covid19stats.ph/stats/by-location/roxas-city-capiz')
    # soup = BeautifulSoup(r.text, 'html.parser')
    # now = datetime.now()

    # def header():
    #     header = soup.find('h2', class_= 'h4 m-0')
    #     date_of_drop = soup.find('p', class_= 'as-of d-block p-0 m-0')
    #     clean = date_of_drop.text.replace('\n', '')
    #     date_ = re.sub(' +', ' ', clean.strip())
    #     return "{}\n{}\n".format(header.text, date_)
        
    # def confirmed_cases():
    #     find_confirmed_cases = soup.find('div', class_ ="text-3-dark-10 kv-store p-3 bg-white bb-3 h-100")
    #     return find_confirmed_cases.text


    # def recoveries():
    #     find_recoveries = soup.find('div', class_ ="text-6-dark-10 kv-store p-3 bg-white bb-6 h-100")
    #     return find_recoveries.text

    # def deaths():
    #     find_deaths = soup.find('div', class_="text-1-dark-10 kv-store p-3 bg-white bb-1 h-100")
    #     return find_deaths.text

    # end "Get Data"
    # end V1.0.0
    pass


def tweet(data):
    now = datetime.now()
    key_list = []
    with open('twitterkeys.txt', 'r') as keys:
        i = 1
        for key in keys:
            key_list.append(key.strip())
            i += 1

    key_name = ['API_key', 'API_secret_key', 'Access_token', 'Access_token_secret']
    key_dict = {}
    for k,v in zip(key_name, key_list):
        key_dict[k] = v

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(key_dict['API_key'], 
        key_dict['API_secret_key'])
    auth.set_access_token(key_dict['Access_token'], 
        key_dict['Access_token_secret'])

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)


    # date_cases_capiz
    # total_cases
    # active cases
    # recovered
    # died

    tweet1 = api.update_status("""[1/3]
    \nRoxas City Update\n\nCases for CAPIZ:
    {}:
    - {} 
    - {}
    - {}
    - {}
        """.format(' '.join(data['date_cases_capiz']), 
            ' '.join(data['total_cases'][0:5]),
            ' '.join(data['active_cases']),
            ' '.join(data['recovered']),
            ' '.join(data['died']),
                ))



    # date roxas lab
    # individuals tested
    # samples tested

    tweet2 = api.update_status("""[2/3]
    \nRoxas City Diagnostic and Laboratory Center:\n\n{}:
    - Total {}
    - {}
    - {}
    - {}
    @rxstwitte_rbot
        """.format(
            ' '.join(data['date_roxas_lab']),
            ' '.join(data['individuals_tested'][0:6]),
            ' '.join(data['samples_tested'][0:4]),
            ' '.join(data['samples_tested'][4:9]),
            ' '.join(data['samples_tested'][9:13])
                ), in_reply_to_status_id=tweet1.id)


    # facilities
    # bed occupancy

    tweet3 = api.update_status("""[3/3]
            \nHospital Beds of 5 City Hospitals:\n
            \n{}:
            - Occupied {}
            - Vacant {}\n\n
            \nHospitals:
            - CDH, CEH, RMPH, St. Anthony, The Health Centrum
            @rxstwitte_rbot
            """.format(' '.join(data['date_facilities']),''.join(data['bed_occupancy'][0]),''.join(data['bed_occupancy'][1])), in_reply_to_status_id=tweet2.id)


    tweet4 = api.update_status("""Date of runtime: {}
            @rxstwitte_rbot
            """.format(now.strftime("%Y-%m-%d")), in_reply_to_status_id=tweet3.id)


def main():
    # use this directly if already have the data and screenshots
    # data_dict = image_to_text.pytess()
    # tweet(data_dict)
    pass

if __name__ == "__main__":
    main()
