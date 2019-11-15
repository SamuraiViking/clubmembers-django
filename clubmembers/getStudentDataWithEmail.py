import requests
  
# api-endpoint 

def getStudentDataWithEmail(email):
    URL = "https://www.stolaf.edu/directory/search"
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {
        'format':'json',
        'email': email
    }
    
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    
    # extracting data in json format 
    student_data = r.json()

    # getting display_name and photo from json 
    display_name = student_data['results'][0]['displayName']
    photo = student_data['results'][0]['photo']

    # returning json to create ClubMember Model
    student_data = {
        "email": email,
        "display_name": display_name,
        "photo": photo
    }

    return student_data