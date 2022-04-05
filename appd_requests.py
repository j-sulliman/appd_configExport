def appdLogin(url="https://<REPLACE ME>.saas.appdynamics.com//controller/auth?action=login?output=json"):
  import requests

  payload={}
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <REPLACE ME>'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)


def getRequest(url='https://<REPLACE ME>.saas.appdynamics.com//controller/rest/applications?output=json'):
  import requests
  import json

  url = url

  payload={}
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <REPLACE ME>'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  print("Retreving API response for {}".format(url))
  print("Received response {}".format(response.status_code))

  if "output=json" in url:
    data = json.loads(response.text)
  else:
    data = response.text

  return data


def postRequest(postData, url='https://<REPLACE ME>.saas.appdynamics.com//controller/rest/applications?output=json'):
  import requests
  import json

  url = url
  print(url)
  headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'X-CSRF-TOKEN': '{{X-CSRF-TOKEN}}',
    'Authorization': 'Basic <REPLACE ME>'
  }

  response = requests.request("POST", url, headers=headers, data=postData)
  if "output=json" in url:
    data = json.loads(response.text)
  else:
    data = response.text
  print(response.status_code)

  return data


def writeConfigToFile(fileData, directoryName, filename):
  import os
  # Check whether the specified path exists or not
  isExist = os.path.exists(directoryName)

  if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(directoryName)

  print("Writing {} configuration for app {} to file... ".format(directoryName, filename))
  f = open("./{}/{}_{}.xml".format(directoryName, app["name"], filename), "w")
  f.write(fileData)
  f.close()


# Get all applications
applications = getRequest(url ='https://<REPLACE ME>.saas.appdynamics.com//controller/rest/applications?output=json')


for app in applications:
  print("Found {} applications, retrieving configuration...".format(len(applications)))
  # Export transaction detection rules
  transactionRules = getRequest(url="https://<REPLACE ME>.saas.appdynamics.com//controller/transactiondetection/{}/custom".format(app['id']))
  writeConfigToFile(transactionRules, directoryName="TransactionRules", filename="TransactionDetectionRules")

  # Export health rules
  healthRules = getRequest(url="https://<REPLACE ME>.saas.appdynamics.com//controller/healthrules/{}".format(app['id']))
  writeConfigToFile(healthRules, directoryName="HealthRules", filename="HealthRules")

  # Export application policies
  appPolicies = getRequest(url="https://<REPLACE ME>.saas.appdynamics.com//controller/policies/{}".format(app['id']))
  writeConfigToFile(appPolicies, directoryName="ApplicationPolicies", filename="Policies")




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
      url="https://<REPLACE ME>.saas.appdynamics.com//controller/transactiondetection/{}/custom".format(targetApp))
'''
