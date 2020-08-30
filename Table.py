# Imports the unofficial Notion API
from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="1e428df2815e00f2cc7bc6edeb32bf187b4f5feb6629f0281c1b25e1196a2b8fe7b746633e50caf041cc22e95af1360545b294c2a0073145d13d8108a7a73a96349ef71cf249ee2c605bf1cefbb3")

# Replace this URL with the URL of the page you want to edit
miku_database = client.get_collection_view("https://www.notion.so/0ebd3315de5446589185448132251bcd?v=6bec01f0809041b99bf3b49a02a6edfc")

# Creates a list of entrys from the table along with title and additional child blocks. 

print ("Miku's table from Notion")

for row in miku_database.collection.get_rows(search="Miku's Table"):	
	 print("Name: '{}'			|			Type: '{}'			|			Date: '{}".format(row.name, row.Type, row.Date_Added))
