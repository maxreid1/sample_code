this is the new one!


import requests, json

def fetchData(url):
  while True:  
    try:
      r=requests.get(url)
      if r.status_code==200:
          data=r.json()
          return data
      else: print('Error:', r.status_code)
    except Exception as e: print(e)

url='https://api.example.com/data'
data=fetchData(url)
if data!=None: print(data)
