import numpy as np
import pandas as pd
import requests
import json

base_url = ""
# test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=nose%20cover&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"
test_url= "https://developer.uspto.gov/ibd-api/v1/application/publications?searchText=animal%20diagnostic%20approaches&start=0&rows=100&largeTextSearchFlag=N&api_key=mwVGnhDAq6v0k0nupQXETJx9oZLyErl3"

api_key = "api key"

response=requests.get(test_url)
json_data = response.json()



patent_info_list = []
for data in json_data['results']:
    patent_dict={}
    # print(f'this is the json response data: {data}')
    # patent_dict['patent_number'] = data['patentNumber']
    patent_dict['application_#'] = data['patentApplicationNumber']
    patent_dict['invention_title'] = data['inventionTitle']
    patent_dict['category'] = data['inventionSubjectMatterCategory']
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
    patent_dict['abstract'] = abstract_string

    
    # claims = data['claimText']
    # patent_dict['claim_text'] = claims
    # patent_dict['description_text'] = data['descriptionText']



    patent_info_list.append(patent_dict)

# print(patent_info_list)

df=pd.DataFrame(patent_info_list)
# print(df)
df.to_csv('patent_api_demo_.csv')




# print(data['results'][0]['publicationDocumentIdentifier'])




