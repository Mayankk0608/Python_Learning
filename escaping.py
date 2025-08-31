# for backslash 
a = "\\watshi no namye wa hatake kakashi desu\\"
print(a)

# for single quote
text = "my name is kakashi."
escaped_text = repr(text)
print("")
print(escaped_text)

# for new line 
text2 = "This is a \nnew line."
encoded_text2_1 = text2.encode('unicode_escape')
decoded_text2 = encoded_text2_1.decode('unicode_escape')
print("")
# print(encoded_text2_1)
print(decoded_text2)

# for bold
import html
text3 = "This is a <b>bold</b> text."
escaped_text3_2 = html.escape(text3)
print("")
print(escaped_text3_2)

# for special char
from urllib.parse import quote, unquote
text4 = "This is a string with spaces and & symbols."
encoded_text4_3 = quote(text4)
decoded_text4_1 = unquote(encoded_text4_3)
print("")
print(encoded_text4_3)
print(decoded_text4_1)

# import sqlite3
# username = "mayank"
# connection = sqlite3.connect('example.db')
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
# print(cursor.execute)

# sql escaping 
import json
data = {"key": "This is a \"quoted\" word."}
json_string = json.dumps(data)
print("")
print(json_string)

# for add backslash after every word 
import re
text5 = "This is a string with special characters: .*+?"
escaped_text5_4 = re.escape(text5)
print("")
print(escaped_text5_4)