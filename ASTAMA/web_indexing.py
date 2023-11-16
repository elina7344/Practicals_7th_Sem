import requests

# Define the list of URLs
list_urls = ["https://www.example.com", "https://www.example/test2"]

# Define the API endpoint URL
url = "https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch?apikey=28e2bf2d5af54a3aa06af933fd193f73"

# Iterate through the list of URLs
for y in list_urls:
    myobj = {
        "siteUrl": "https://www.example.com",
        "urlList": [str(y)]
    }

    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    x = requests.post(url, json=myobj, headers=headers)

    print("Submitting URL:", y)

    # Check the response status code
    if x.status_code == 200:
        print("Submission successful!")
    else:
        print("Submission failed. Status Code:", x.status_code)
        print("API Response:", x.text)
