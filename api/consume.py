#did this to see how api's are consumed in python(i will use dart though)
 
import requests
#from django.http.request import HttpRequest
response = requests.get(url="http://127.0.0.1:8000/api/")
print(response.json())
