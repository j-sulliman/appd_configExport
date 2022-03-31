


def appdLogin(url="https://apjsales2.saas.appdynamics.com//controller/auth?action=login?output=json"):
  import requests

  url = url

  payload={}
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <UPDATE ME>'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)


def getRequest(url='https://apjsales2.saas.appdynamics.com//controller/rest/applications?output=json'):
  import requests
  import json

  url = url

  payload={}
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <UPDATE ME>'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  if "output=json" in url:
    data = json.loads(response.text)
  else:
    data = response.text

  return data


def postRequest(postData, url='https://apjsales2.saas.appdynamics.com//controller/rest/applications?output=json'):
  import requests
  import json

  url = url
  print(url)
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <UPDATE ME>'
  }

  response = requests.request("POST", url, headers=headers, data=postData)
  if "output=json" in url:
    data = json.loads(response.text)
  else:
    data = response.text
  print(response.status_code)

  return data

applications = getRequest(url ='https://vistaentertainment-non-prod.saas.appdynamics.com//controller/rest/applications?output=json')

for app in applications:
  transactionRules = getRequest(url="https://vistaentertainment-non-prod.saas.appdynamics.com//controller/transactiondetection/{}/custom".format(app['id']))
  f = open("./TransactionRules/{}_TransactionDetectionRules.xml".format(app["name"]), "w")
  f.write(transactionRules)
  f.close()



'''
import os 

dir_list = os.listdir('./TransactionRules')
#cwd = os.getcwd()
#print(cwd)
os.chdir('./TransactionRules')
 
 
for rule in dir_list:
  # Open the XML file.
  with open('{}'.format(rule)) as xml:
    # Give the object representing the XML file to requests.post.
    targetApp = input("Source App [{}] | Enter Target Application name:".format(rule))
    postRequest(xml, 
      url="https://apjsales2.saas.appdynamics.com//controller/transactiondetection/{}/custom".format(targetApp))
'''
