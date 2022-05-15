# status code checker
import requests
import json
import time
SLEEP = 0  # Time in seconds the script should wait between requests
url_list = []
url_statuscodes = []
url_statuscodes.append(["url", "status_code"])  # set the file header for output


def get_status_code(url):
    try:
        r = requests.head(url, verify=False, timeout=5) # it is faster to only request the header
        return (r.status_code)
    except:
        return -1
# Url checks from file Input
# use one url per line that should be checked


with open("urls.json") as f:
    reader = json.load(f)
    for row in reader:
        url = "localhost:4547/cms/{row}/Model/zsqls/manage_main".format(row=row)
        url_list.append(url)
# Loop over full list
for url in url_list:
    print(url)
    check = [url, get_status_code(url)]
    time.sleep(SLEEP)
    url_statuscodes.append(check)
# Save file
with open("urls_withStatusCode.txt", "w") as f:
    # writer = json.writer(f)
    # writer.writerows(url_statuscodes)
    f.write(('').join(url_statuscodes))
