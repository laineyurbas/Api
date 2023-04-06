import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
submissions_list =[]
for sID in r.json()[:20]:
    print(sID)
    url1 = f"https://hacker-news.firebaseio.com/v0/item/{sID}.json"
    curr_r = requests.get(url1)
    json_obj = curr_r.json()
    print(f"Title: {json_obj['title']}\nComments:{json_obj.get('descendants','none')}")

    a_dict = {'title': title, 'link':link, 'comments':comments}

    submissions_list.append(a_dict)

from operator import itemgetter

submissions_list = sorted(submissions_list, key=itemgetter('comments',reverse=True))

for x in submissions_list:
    print(f"Title: {x['title']}")
    print(f"Link: {x['link']}")
    print(f"Comments: {x['comments']}")


"""

outfile = open('hn.json', 'w')
json.dump(r.json(), outfile, indent=4)

submissionIDsList = r.json()

url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)
outfile = open('hn2.json','w')

json.dump(r.json(),outfile, indent=4)
"""