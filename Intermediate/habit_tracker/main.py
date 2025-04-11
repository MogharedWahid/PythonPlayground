from datetime import datetime
import requests

# -------------------- USER CONFIGURATION --------------------
USERNAME = "moghared"
TOKEN = "qwe1qwe2qwe3qwe4"

# -------------------- ENDPOINTS --------------------
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH1_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# -------------------- HEADERS --------------------
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# -------------------- USER CREATION (run once) --------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment the lines below to create a user (only once)
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# -------------------- GRAPH CREATION (run once) --------------------
graph_params = {
    "id": GRAPH_ID,
    "name": "Moghared Python Graph",
    "unit": "Hr",
    "type": "float",
    "color": "shibafu"  # green
}

# Uncomment the lines below to create a graph (only once)
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=HEADERS)
# print(response.text)

# -------------------- ADD TODAY'S DATA --------------------
today = datetime.now().strftime("%Y%m%d")
quantity = input("How many hours did you practice Python today? ")

pixel_params = {
    "date": today,
    "quantity": quantity
}

response = requests.post(url=GRAPH1_ENDPOINT, json=pixel_params, headers=HEADERS)

# -------------------- RESPONSE --------------------
print(response.text)
