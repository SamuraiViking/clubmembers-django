# importing the requests library 
import requests 
  
# api-endpoint 

URL = "https://www.stolaf.edu/directory/search"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {
    'format':'json',
    'email':'nelson67@stolaf.edu'
} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json()

print(data)