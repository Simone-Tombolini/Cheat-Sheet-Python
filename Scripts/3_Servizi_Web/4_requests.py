import requests

#il codice è molto semplice, non necessita di commenti
r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.status_code == requests.codes.ok)
print(r.json())
print(r.raw)

r = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(r)
r = requests.delete('https://httpbin.org/delete')
print(r)
r = requests.head('https://httpbin.org/get')
print(r)
r = requests.options('https://httpbin.org/get')
print(r)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)

#get cookie diretta, sconsigliato
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

#getsione dei cookie con l'oggetto di sessione
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
