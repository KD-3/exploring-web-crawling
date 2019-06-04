import json

with open('tweerData.json') as json_data:
	jsonData = json.load(json_data)
	for i in jsonData:
		print(i['shares'])