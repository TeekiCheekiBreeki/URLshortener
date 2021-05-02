import requests

#api key
api_key = "cd30c7e21d07ede6c3303ff73d2c9fae4db92"

# We read url we want to shorten
url = input("Enter your URL here: ")

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

# We make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # IF everything is OK, we get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)