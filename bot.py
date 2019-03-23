from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os
os.open("sentiment.csv")
s= set(map(name,date,image,content))
for i in range(4):
	url = 'https://aqueous-badlands-62703.herokuapp.com/research/new' # Set destination URL here
	post_fields = {'name': s.name[i]}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)