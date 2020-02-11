import requests, bs4, psycopg2, os

# Actually y'know, get the page
comic_page = requests.get("https://www.explainxkcd.com/wiki/index.php/List_of_all_comics_(1-500)")

# Setup the database connection
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='allow')
cursor = conn.cursor()
insert_query = "INSERT INTO comics VALUES (%s, %s, %s)" # This formats the query for later

# Parse the page and find the table
soup = bs4.BeautifulSoup(comic_page.content, 'lxml')
table = soup.find('table')

# Loop through table rows and acquire data
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if not tds:
        continue
    url, title = [td.a.text.strip() for td in tds[:2]]
    print(title)
    num = ""
    for char in url:
        if char.isnumeric():
            num += (char)
    num = int(num)
    record = (num, title, url)
    try:
        cursor.execute(insert_query, record)
        conn.commit()
    except psycopg2.Error as e: # Handle if the database fucks up
        print(e.pgerror)
        cursor.execute("ROLLBACK")
        conn.commit()

# Close out when we're done
cursor.close()
conn.close()