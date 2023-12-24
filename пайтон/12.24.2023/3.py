try:
    fd = open("html.html", encoding='utf8')
except FileNotFoundError:
    print("нет")
    exit()
text=fd.read()
fd.close()

title_start=text.find("<title>")
title_end=text.find("</title>")

title = text[title_start + 7:title_end]
if not title == "":
    print(title)

h1_start=text.find("<h1")
h1_end=text.find("</h1>")

h1 = text[h1_start + 4:h1_end]
print(h1)