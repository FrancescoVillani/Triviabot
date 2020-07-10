from googleapiclient.discovery import build
from pprint import pprint

API_key = "AIzaSyBbmlLp4Yxrx_2sE3ebdx9mCt1fL1YrRS4"
CSE_id = "017297845227077967885:8bnf4eoxf-4"

def search(search_term):
    service = build("customsearch", "v1", developerKey=API_key)
    res = service.cse().list(q=search_term, cx=CSE_id, num=10).execute()
    return res['items']

results = search('how old is grandpa pig')
pprint(results[0])