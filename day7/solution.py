import re


def data_reader():
    with open("input.txt", "r") as input_data:
        for line in input_data:
            yield line


def calculate_dir_size(data, dirname='root', total_dir_size=None):
    dir_name = dirname
    dir_size = 0
    for line in data:
        if "$ ls" in line:
            continue
        elif line.startswith("dir"):
            continue
        elif re.match(r"(\d+) (\w+)", line) is not None:
            found = re.match(r"(\d+) (\w+)", line)
            dir_size += int(found.groups()[0])
        elif line.startswith("$ cd .."):
            break
        elif line.startswith("$ cd"):
            found = re.match(r"\$ cd (\w+)", line)
            new_dir_name = found.groups()[0]
            dir_size += calculate_dir_size(data, new_dir_name, total_dir_size)

    if dir_size <= 100000:
        total_dir_size.append(dir_size)
        print("count it")

    print(f"Directory {dir_name} has size {dir_size}")
    return dir_size


def calculate_dir_size_task2(data, dirname='root', total_dir_size=None):
    dir_name = dirname
    dir_size = 0
    for line in data:
        if "$ ls" in line:
            continue
        elif line.startswith("dir"):
            continue
        elif re.match(r"(\d+) (\w+)", line) is not None:
            found = re.match(r"(\d+) (\w+)", line)
            dir_size += int(found.groups()[0])
        elif line.startswith("$ cd .."):
            break
        elif line.startswith("$ cd"):
            found = re.match(r"\$ cd (\w+)", line)
            new_dir_name = found.groups()[0]
            dir_size += calculate_dir_size_task2(data, new_dir_name, total_dir_size)

    total_dir_size.append(dir_size)

    print(f"Directory {dir_name} has size {dir_size}")
    return dir_size


data = data_reader()
data.__next__()
total_dir_size = []
total_size = calculate_dir_size_task2(data, "root", total_dir_size)
print(f"Total size is {total_size}")
unused_size = 70000000 - total_size
print(f"Unused size is {unused_size}")
required_size = abs(unused_size-30000000)
print(f"Required size is {required_size}")


min_size_dir = total_size
for dir in total_dir_size:
    if required_size <= dir < min_size_dir:
        min_size_dir = dir


print(f"Min size is {min_size_dir}")

