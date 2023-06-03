import requests

url = "https://checkout.sandbox.bka.sh/v1.2.0-beta/checkout/payment/create"

headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)