import requests, html2text

word = str(input())
r = requests.get('https://www.dizionario-latino.com/dizionario-latino-italiano.php?parola='+word)

line = []
for c in r.text:
    if c!='\n':
        line.append(c)
    else:
        if '<span class="italiano">' in "".join(line):
            print(html2text.html2text("".join(line)).replace('*', ''), end="")
        line = []
