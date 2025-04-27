import requests

result = None

url = 'https://example.com'

response = requests.get(url)

result = response.text
