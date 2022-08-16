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
    i=1
    for img_url in all_url:
        print('Using URL: ', img_url)
        name = f'{i}' + os.path.splitext(img_url)[1]
        print('File name will be: ', name)
        #urllib.request.urlretrieve(f'{url}', name)
        img_res = requests.get(img_url)
        img = Image.open(BytesIO(img_res.content))
        img.show()
        i+=1


#all_url = wal_down('cyberpunk')
#print('Available Url are: ')
#for url in all_url:
    #print(url)
    #img = Image.open(BytesIO(url))
    #img.show()
    #path = urllib.parse.urlparse(url).path
    #print(os.path.splitext(path)[0], " ", os.path.splitext(path)[1])


query = input('Enter your wallpaper style: ')
wal_down(f'{query}')

