import re
valid_urls = re.compile('(https?|ftp|file)?://[a-z0-9+&@#/%?=~_|!:,.;]+.[a-z+&@#/%=~_|]', re.IGNORECASE)    
print(valid_urls)


if (valid_urls.match("https://aa.")):
    print("matcheoo")
else:
    print("no matcheo")