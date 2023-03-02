import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input("Please give a url")  # προσδιορισμός του url
response = requests.get(url)

#with requests.get(url, headers=headers) as response:  # το αντικείμενο response
#    html = response.text
#    more(html)


print(response.headers,"\n")
print("The web server's name is:", response.headers["Server"], "\n")
#for key in response.headers:
 #   if key == "Set-Cookie" or key == "set-cookie":
  #      print("This site uses cookies,\n ",response.headers[key],"\n")
if response.cookies:
    print("This site uses cookies, ")
for c in response.cookies:
    print(c.name, c.value, "\n")