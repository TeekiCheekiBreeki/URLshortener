import requests

#account info
username ="o_sk88l8f0s"
password = "Jebemtimater1!"

#we get the access token (if you read bitly api documentation, you see that
# we need access token in order to make api calls)

#firstly we need to get authentication response, then if response is OK, we get the token

auth_response = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth = (username, password))

if auth_response.status_code == 200:
    access_token = auth_response.content.decode()
    print("[!] Got access token: ", access_token)

else:
    print("[!] Cannot get access token, exiting..")
    exit()

# We used requests.post() to make a POST request to bitly endpoint and get our access token

