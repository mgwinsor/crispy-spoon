import os
import requests

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')

def main():
    pixela_endpoint = "https://pixe.la/v1/users"

    user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }

    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response)
    # print(response.text)

    graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

    headers = {
        'X-USER-TOKEN': TOKEN
    }
    graph_config = {
        'id': 'graph1',
        'name': 'Engineering Hours',
        'unit': 'Hours',
        'type': 'float',
        'color': 'ajisai',
    }
    # response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    # print(response)
    # print(response.text)

    today = datetime.now()

    pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
    add_pixel = {
        'date': today.strftime('%Y%m%d'),
        'quantity': '0.5',
    }
    response = requests.post(url=pixel_endpoint, headers=headers, json=add_pixel)
    print(response)
    print(response.text)

if __name__ == "__main__":
    main()
