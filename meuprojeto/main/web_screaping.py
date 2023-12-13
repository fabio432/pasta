import requests

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://www.google.com"
token = "YOUR_TOKEN"
proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
proxies = {
    "http": proxyModeUrl,
    "https": proxyModeUrl,
}
response = requests.request("GET", url, proxies=proxies, verify=False)
print(response.text)
