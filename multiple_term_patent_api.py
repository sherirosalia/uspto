from re import search
import numpy as np
import pandas as pd
import requests
import json
# import urllib.parse
from requests.utils import requote_uri



base_url = ""
# test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=nose%20cover&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"
# test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=remote%20diagnostic%20approaches&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"

api_key = "api key"

# response=requests.get(test_url)
# json_data = response.json()

# search_terms = ['medical diagnostics system', 'medical diagnostics', 'veterinary', 'medical assessment','computer assisted diagnosis', 'veterinary medicine', 'animal pain detection', 'medical diagnosis model','medical diagnostic method','diagnostic data processing','diagnostic data','pain detection' ]
# search_terms = ['medical', 'veterinary', 'data', 'mitotic', 'model', 'disease', 'diagnostic', 'diagnostics', 'relevant', 'human', 'interest', 'research,' 'detection', 'field', 'pain', 'learning', 'results', 'problem', 'clinical', 'population']
# test_url= f'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={search_term}&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}'
search_terms=['extreme heat','self priming','ceramic coating','high celcius','extreme heat','high celcius', 'thermal barrier coating', 'abrasion resistance coating', '1700 Celcius ceramic coating', 'high temperature self priming ceramic coating', 'high-temperature coating composistion' ]
number_of_urls_checked=0
patent_info_list = []
for search_term in search_terms:
    # print(search_term)

    # print(urllib.parse.quote("http://www.sample.com/"))
    test_urls=requote_uri(f'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={search_term}&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}')

    # test_url= urllib.parse.quote(f'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={search_term}&start=0&rows=100&largeTextSearchFlag=N&api_key={api_key}')
       
    # print(test_urls)

    request=requests.get(test_urls) 
    json_data = request.json()
    
    # print(json_data)
    number_of_urls_checked+=1
    
    for data in json_data['results']:

            patent_dict={}
            # print(f'this is the json response data: {data}')
            # patent_dict['patent_number'] = data['patentNumber']
            patent_dict['application_#'] = data['patentApplicationNumber']
            patent_dict['invention_title'] = data['inventionTitle']
            patent_dict['category'] = data['inventionSubjectMatterCategory']
            patent_dict['search_term']=search_term
            patent_dict['filing_date'] = data['filingDate']
            # patent_dict['grant_date'] = data['grantDate']
            patent_dict['assignee'] = data['assigneeEntityName']
            patent_dict['assignee_location'] = data['assigneePostalAddressText'] 
            patent_dict['inventors'] = data['inventorNameArrayText']
            patent_dict['file_url'] = data['filelocationURI'] 
            # patent_dict['archive_url'] = data['archiveURI']
            # convert abstract from list to string
            for abstract_list in data['abstractText']:
                abstract_string = ''.join(abstract_list)
                print(f'abstract string: {abstract_string}')
            patent_dict['abstract'] = abstract_string
            


            
#             # claims = data['claimText']
#             # patent_dict['claim_text'] = claims
#             # patent_dict['description_text'] = data['descriptionText']
            patent_info_list.append(patent_dict)

        

    print(f'this is loop number {number_of_urls_checked} and search term: {search_term}')

df=pd.DataFrame(patent_info_list)
# print(df)
df.to_csv('henkel.csv', index=False)

 