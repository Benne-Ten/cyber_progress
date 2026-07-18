import requests
import argparse

def requete(url: str):
    try:
        response = requests.get(url, timeout=5)
        print(f"Status Code : {response.status_code}")
        
        if response.status_code == 200:
            lignes = response.text.splitlines()
            for ligne in lignes[:5]:
                print(ligne)
        elif response.status_code == 404:
            print("Page not found")
    
    except requests.exceptions.Timeout:
        print("Timeout!")
    except requests.exceptions.ConnectionError:
        print("Connection error!")
    except Exception as e:
        print(f"Error: {e}")

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
requete(args.url)
