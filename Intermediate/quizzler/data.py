import requests

parameters = {
    "amount" : 10,
    "type"   : "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

question_data = data['results']
# print(question_data)