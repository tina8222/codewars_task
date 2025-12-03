
def create_frame(picture):
    max_len = max(len(line) for line in picture)
    border = "*" * (max_len + 4)
    framed = [border]

    for line in picture:
        padding = " " * (max_len - len(line))  
        framed_line = "* " + line + padding + " *"
        framed.append(framed_line)

    framed.append(border)

    return "\n".join(framed)

elephant= [
"  Create a frame!mewww ",
"           __     __   ",
"          /  \~~~/  \  ",
"    ,----(     ..    ) ",
"   /      \__     __/  ",
"  /|         (\  |)    ",
" ^  \  /___\  /\ |     ",
"    |__|   |__|-..     ",
]

print(create_frame(elephant))


