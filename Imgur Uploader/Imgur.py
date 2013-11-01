#
import webbrowser
import pyimgur

CLIENT_ID = "a7c30de4f98751b"
CLIENT_SECRET = "a188f1467cf86eae0d7a03e289e922235128160b"   # Needed for step 2 and 3

# Run this script once, to generate a token, then add it here.
USER_TOKEN = ""

# Uncomment this once you have a token
# im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)
im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

# The authorization URL
auth_url = im.authorization_url('pin')
webbrowser.open(auth_url)

# Get pin from user
pin = input("What is the pin? ")

# Handshake
im.exchange_pin(pin)

# This stuff will work, once you have access token

# PATH = "C:\\Users\\dufferzafar\\Pictures\\Screenshots\\Screen-01-Nov-2013-20-37-42.png"
# uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur", album=im.create_album("Screenshots", "Uploaded Screenshots."))
# print(uploaded_image.title)
# print(uploaded_image.link)
# print(uploaded_image.size)
# print(uploaded_image.type)

ac = im.refresh_access_token()

print("Save this token. You'll need it.")
print("Generated access token is : " + ac)