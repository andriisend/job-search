import requests
import json 

#I plan to add to add a dropdown menu here 
user_input=input("Please choose a search criteria: Agency Subelements, Occupational Series, Pay Plans, Postal Codes  ")
if "ge" in user_input:
    user_input="agencysubelements"
    request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
    response = requests.get(request_url)
    data = json.loads(response.text)
    agency_input = input("Please input your desired agency code: ")
    for n in (data['CodeList'][0]['ValidValue']):
      if str(agency_input) in str(n['Code']):
        print(str(n['Code'][0:2] + ': ' + str(n['Value'])))
elif "ccu" in user_input:
    user_input="OccupationalSeries"
    print("Occupational Series")
    request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
    response = requests.get(request_url)
    data = json.loads(response.text)
    #agency_input = input("Please input your desired agency code: ")
    for n in (data['CodeList'][0]['ValidValue']):
      #if str(agency_input) in str(n['Code']):
      print(n['Value'])
elif "ay" in user_input:
    user_input="payplans"
    print("Pay Plans")
    request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
    response = requests.get(request_url)
    data = json.loads(response.text)
    for n in (data['CodeList'][0]['ValidValue']): 
        print(n['Value'])
elif "ost" in user_input:
    user_input="postalcodes"
    print("Postal Codes")
    request_url = f"https://data.usajobs.gov/api/codelist/{user_input}"
    response = requests.get(request_url)
    data = json.loads(response.text)
    city_search = input("Please input the city: ")
    for n in (data['CodeList'][0]['ValidValue']):
      if str(city_search) in n['City']:
        print(n['City'] + ': ' + n['Code']) 