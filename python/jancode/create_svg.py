def create(binary_number: str, width: str, path: str, number: str):
    x = y = 0
    content = list()

    for i in binary_number:
        if(int(i)):
            content.append(f'<rect x="{x}" y="{y}" width="1" height="90%" fill="#000000" />')
        x += 1

    meta_head = f'<svg version="1.1"\nbaseProfile="full"\nwidth="{width}"\nheight="80"\nxmlns="http://www.w3.org/2000/svg">\n\n' + \
    '<!-- fill background -->\n<rect width="100%" height="100%" fill="white" />\n\n' + \
    '<!-- fill jancode -->\n'
    meta_tail =  "\n\n</svg>"
    data = meta_head + "\n".join(content) + meta_tail

    with open(f"{path}/{number}.svg", "w") as f:
        f.write(data)
