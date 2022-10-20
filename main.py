import requests
from datetime import datetime

today = datetime.now()
TODAY = today.strftime("%Y%m%d")


USER = "drdiedrich19"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_params = {
    "id": "test",
    "name": "Test Graph",
    "unit": "days",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixels_endpoint = f"{graph_endpoint}/test"

pixels_params = {
    "date": TODAY,
    "quantity": "4",
}
# pixel_post = requests.post(url=pixels_endpoint, json=pixels_params, headers=headers)
# print(pixel_post.text)

pixel_endpoint = f"{pixels_endpoint}/{TODAY}"
pixel_params = {
    "quantity": "1"
}
# pixel_update = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_update.text)

pixel_delete = requests.delete(url=pixel_endpoint, headers=headers)
print(pixel_delete.text)