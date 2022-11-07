
import requests
endpoint='http://localhost:8000/api/product/'
# endpoint='https://httpbin.org/status/200/'


get_response= requests.get (endpoint)

print(get_response.json())

