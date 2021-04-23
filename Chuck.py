import requests

resp = input('Would you like one?')

while resp == 'y' or resp == 'Y' or resp == 'yes' or resp == 'Yes':
    url = 'https://api.chucknorris.io/jokes/random'
    headers = {'cache-control': 'no-cache'}
    r = requests.request('GET', url, headers=headers)
    joke = r.json()
    print(joke['value'], '\n')
    resp = input('Would you like to be hit again?\n')
print('You were not worthy anyways')
