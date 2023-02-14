def create(binary_number: str, width: str, path: str, number: str):
    content = [f'<rect x="{x}" y="0" width="1" height="90%" fill="#000000" />' for x, i in enumerate(binary_number) if int(i)]

    meta_head = f'<svg version="1.1"\nbaseProfile="full"\nwidth="{width}"\nheight="80"\nxmlns="http://www.w3.org/2000/svg">\n\n' + \
    '<!-- fill background -->\n<rect width="100%" height="100%" fill="white" />\n\n' + \
    '<!-- fill jancode -->\n'
    meta_tail =  "\n\n</svg>"
    data = meta_head + "\n".join(content) + meta_tail

    with open(f"{path}/{number}.svg", "w") as f:
        f.write(data)
