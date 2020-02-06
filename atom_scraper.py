import requests, atoma, datetime, os, psycopg2

response = requests.get("https://www.xkcd.com/atom.xml")
feed = atoma.parse_atom_bytes(response.content)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='allow')

since_update = datetime.datetime.now(tz=datetime.timezone.utc) - feed.updated
print(since_update.total_seconds())

cursor = conn.cursor()
print(len(feed.entries))

insert_query = "INSERT INTO comics VALUES (%s, %s, %s)"

for post in feed.entries:
    title = post.title.value
    url = post.links[0].href
    num = ""
    for char in url:
        if char.isnumeric():
            num += (char)
    num = int(num)
    record = (num, title, url)
    cursor.execute(insert_query, record)
    conn.commit()

cursor.close()
conn.close()
