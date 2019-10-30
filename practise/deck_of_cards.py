import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count": "6"}

headers = {
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "79c0bfa5-09fc-4dd5-94b7-b7a2ff6e90ee,b7d24f60-9fdb-4659-8c7f-edccb741bf38",
    'Host': "deckofcardsapi.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "__cfduid=d3ffc81ad2976e6e9fc24ae99dc60c8ba1572466014",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
deck = response.json()
print(type(deck))
deck_id = deck['deck_id']
print(deck_id)
