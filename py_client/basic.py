from webbrowser import get
import requests
endpoint='http://localhost:8000/api/'
# endpoint='https://httpbin.org/status/200/'


get_response= requests.get (endpoint,params={"abc":123},json={"name":"omar"})
# print(get_response.status_code)

# print(get_response.headers)

# print(get_response.text)
#print raaw text
print(get_response.json())
python


# print(get_response.status_code)