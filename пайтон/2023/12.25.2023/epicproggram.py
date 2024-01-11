text = input("текст: ")
max_line_length = int(input("максимальная длина строки: "))

initial_lines = text.split(" ", maxsplit=max_line_length)

paragraphs = []
current_paragraph = ""
for line in initial_lines:
    if line:
        if not line[0].isupper():
            line = line.capitalize()
        current_paragraph += " " + line
        if line[-1] in ".!?":
            paragraphs.append(current_paragraph.strip())
            current_paragraph = ""
paragraphs.append(current_paragraph.strip())

formatted_lines = []
for paragraph in paragraphs:
    words = paragraph.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > max_line_length:
            formatted_lines.append(line.strip())
            line = ""
        line += word + " "
    if line:
        formatted_lines.append(line.strip())

for line in formatted_lines:
    if line and not line[-1] in ".!?":
        line = "    " + line

print("\n\n".join(formatted_lines))