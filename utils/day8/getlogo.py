import requests

response = requests.get(url='https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0626%2F1e68c929j00rwv9k6000wc000hs00b4g.jpg&thumbnail=660x2147483647&quality=80&type=jpg')

print(response.content)
with open('tp1.png','wb') as f:
    f.write(response.content)