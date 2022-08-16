import requests, os
from PIL import Image
from io import BytesIO

def wal_down(query):
    url = f"https://wallhaven.cc/api/v1/search?q={query}"
    res = requests.get(url) 
    json_data = res.json()
    
    all_url = []
    for data in json_data['data']:
        all_url.append(data['path'])
    
    name = ''
    for img_url in all_url:
        user_res = input("View Wallpaper/ Next Wallpaper(y/n): ")
        if(user_res == 'y'):
            print('Using URL: ', img_url)
            name = 'wallhaven_wallpaper' + os.path.splitext(img_url)[1]
            img_res = requests.get(img_url)
            img = Image.open(BytesIO(img_res.content))
            img.show()
            down = input("Download this wallpaper: ")
            if(down == 'y'):
                down_wallpaper(img_url, name)
        else:
            break


def down_wallpaper(url, filename):
    print(f'Downloading {url}... with filename {filename}')
    res = requests.get(url)
    username = os.getlogin()
    down_path = f'/home/{username}/Downloads/{filename}'
    print(down_path)
    open(down_path, 'wb').write(res.content)


query = input('Enter your wallpaper style: ')
wal_down(f'{query}')

