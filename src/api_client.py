import requests

def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try: 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data= response.json()
        return data
    except requests.RequestException as error:
        return {'error': str(error)}