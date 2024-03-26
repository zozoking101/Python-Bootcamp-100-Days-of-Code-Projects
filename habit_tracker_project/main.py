import requests
import os
import datetime as dt
import random

USERNAME = "zozoking101"
TOKEN = os.environ.get("PIXELA_PASSWORD")

# Create a user account by calling https://pixe.la/v1/users with HTTP POST
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph definition by calling https://pixe.la/v1/users/zozoking101/graphs with HTTP POST
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    'id': "commit-graph1",
    'name': "Commit Tracker Graph",
    'unit': "commit",
    'type': "int",
    'color': "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Graph at https://pixe.la/v1/users/zozoking101/graphs/commit-graph1.html
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# Post value to a pixel by calling https://pixe.la/v1/users/zozoking101/graphs/commit-graph1 with HTTP POST

today = dt.datetime.now().strftime('%Y%m%d')
yesterday = dt.datetime(year=2024, month=3, day=25).strftime('%Y%m%d')

pixel_endpoint = f'{graph_endpoint}/{graph_params["id"]}'

pixel_params = {
    "date": today,  # yesterday
    "quantity": "5",
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_response.text)

# Update value of a pixel by calling https://pixe.la/v1/users/zozoking101/graphs/commit-graph1/yyyyMMdd with HTTP PUT
update_endpoint = f'{pixel_endpoint}/{yesterday}'  # Updating yesterday's pixel value

update_params = {
    "quantity": "8",
}

# update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_response.text)

# Delete value of a pixel by calling https://pixe.la/v1/users/zozoking101/graphs/commit-graph1/yyyyMMdd with HTTP DELETE
delete_endpoint = f'{pixel_endpoint}/{yesterday}'  # Deleting yesterday's pixel value

# delete_response = requests.delete(url=delete_endpoint,  headers=headers)
# print(delete_response.text)

# I can't post multiple pixels at once for free, so I have to post them randomly repeatedly.
# Post value of a pixel by calling https://pixe.la/v1/users/zozoking101/graphs/commit-graph1/yyyyMMdd with HTTP POST

months = [_ for _ in range(4, 9)]  # (1, 4)
days = [_ for _ in range(1, 31)]  # (1, 26)
quantities = [4, 5, 7, 8, 9, 11, 12, 14, 18]

day = dt.datetime(year=2023, month=random.choice(months), day=random.choice(days)).strftime('%Y%m%d')
quantity = str(random.choice(quantities))

random_endpoint = f'{pixel_endpoint}'

random_params = {
    "date": day,
    "quantity": quantity,
}

random_response = requests.post(url=random_endpoint, json=random_params, headers=headers)
print(random_response.text)
