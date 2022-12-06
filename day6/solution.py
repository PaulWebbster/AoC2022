with open("input.txt", "r") as data_input:
    a = data_input.read()


for j in [4, 14]:
    visible_characters = []
    for i, letter in enumerate(a):
        if a not in visible_characters:
            visible_characters.append(a)
        elif i >= j:
            found_marker = a[i-j:i]
            if len(set(found_marker)) == j:
                print(f"Task {1 if j == 4 else 2}: Marker is {found_marker} on position {i}")
                break
