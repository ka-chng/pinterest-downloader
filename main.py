import os
import requests
from py3pin.Pinterest import Pinterest
from token import access_token

access_token = 'your_access_token'

pinterest = Pinterest(access_token=access_token)

search_query = 'trippy'
search_results = pinterest.search(scope='pins', query=search_query)

image_count = 0
output_folder = 'trippy_take_images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for pin in search_results:
    if image_count >= 50:
        break

    image_url = pin['images']['orig']['url']
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(os.path.join(output_folder, f'_{image_count}.jpg'), 'wb') as f:
            f.write(response.content)
        image_count += 1

print(f'Downloaded {image_count} images')
