import requests, atoma, datetime

response = requests.get("https://www.xkcd.com/atom.xml")
feed = atoma.parse_atom_bytes(response.content)

since_update = datetime.datetime.now(tz=datetime.timezone.utc) - feed.updated
print(since_update.total_seconds())

"""
for post in feed.entries:
    title = post.title.value
    url = post.links[0].href
    num = ""
    for char in url:
        if char.isnumeric():
            num += (char)
    num = int(num)
    print(num)
"""