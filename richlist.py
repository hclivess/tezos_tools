import requests
import json

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

page = 0
request = True #init
addresses = []

while request:
    api_url = "http://api.tzscan.io/v1/accounts?p={}".format(page)



    request_raw = requests.get(api_url, headers=hdr)
    request = json.loads(request_raw.text)

    print(request)
    for entry in request:
        print(entry)
        addresses.append(entry['hash'])
    page += 1


print(addresses)



#address_balance = {}
addresses_balance = []

for address in addresses:
    api_url = "http://api.tzscan.io/v1/account/{}".format(address)
    request_raw = requests.get(api_url, headers=hdr)
    request = json.loads(request_raw.text)
    #address_balance[address] = float(request['balance'])/1000000
    addresses_balance.append((address,float(request['balance'])/1000000))

print(addresses_balance)
sorted = (sorted(addresses_balance, key=lambda list: list[1]))

with open("rich.txt","w") as richlist:
    for entry in sorted:
        richlist.write("{},{}\n".format(entry[0],entry[1]))
