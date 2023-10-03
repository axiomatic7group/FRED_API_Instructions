import requests
import pandas as pd

api_key= '### Enter your API key here ###'

FRED_Categories = pd.DataFrame({"name":['Money, Banking, & Finance','Population, Employment, & Labor Markets', 'National Accounts', 'Production & Business Activity', 'Prices', 'International Data', 'U.S. Regional Data', 'Academic Data'],
                                "id":[32991, 10, 32992, 1, 32455, 32263, 3008, 33060]})

get_category = lambda FRED_Category_ID, APIKey: requests.get('https://api.stlouisfed.org/fred/category/children?category_id='+str(FRED_Category_ID) +'&api_key='+ APIKey + '&file_type=json').json()['categories']
get_series = lambda FRED_Category_ID, APIKey: requests.get('https://api.stlouisfed.org/fred/category/series?category_id='+str(FRED_Category_ID) +'&api_key='+ APIKey + '&file_type=json').json()['seriess']
get_observations = lambda FRED_Series_ID, APIKey: requests.get('https://api.stlouisfed.org/fred/series/observations?series_id='+str(FRED_Series_ID) +'&api_key='+ APIKey + '&file_type=json').json()['observations']
get_scategories = lambda FRED_Series_ID, APIKey: requests.get('https://api.stlouisfed.org/fred/series/categories?series_id='+str(FRED_Series_ID) +'&api_key='+ APIKey + '&file_type=json').json()['categories']


children = pd.DataFrame(get_category(FRED_Categories['id'][1], api_key))
categories = pd.DataFrame(get_category(children['id'][0], api_key))
series = pd.DataFrame(get_series( categories['id'][0], api_key))
observations = pd.DataFrame(get_observations(series['id'][0] ,api_key))
observations.index = observations['date']
observations = observations.drop(columns='date')

print(series['title'][0])
print(observations)
print(observations.columns)

