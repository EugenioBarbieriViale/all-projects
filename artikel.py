import requests, html2text

articles = ["der","die","das"]
word = str(input())

for i in articles:
    url = "https://der-artikel.de/"+i+'/'+word.title()+".html"
    r = requests.get(url)
    if (r.status_code==200):
        break

if r.status_code==404:
    print("Word not found")

content = html2text.html2text(r.text)
line = []
for c in content:
    if c!='\n':
        line.append(c)
    else:
        if '#' in "".join(line):
            ans = html2text.html2text("".join(line))
            break
        line = []
e = (ans.replace('#',''))
print(e.replace('_',''), end='')
