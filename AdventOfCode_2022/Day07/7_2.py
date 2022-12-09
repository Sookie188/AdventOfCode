from anytree import Node, RenderTree, PreOrderIter


def get_strings(filename):
    with open(filename, "r") as fp:
        tmp = fp.readlines()
    return [str(i.rstrip()) for i in tmp]


def get_dir_size(dir):
    size = 0
    return size


input = get_strings("AdventOfCode_2022/Day07/input.txt")

root = Node('root', parent=None, size=0, directory=True)
current = root

for line in input[1:]:
    if '$ ls' in line:
        pass
    elif '$ cd' in line:
        target_dir_name = line.split(' ')[2]
        if target_dir_name == '..':
            if current.parent == None:
                current = root
            else:
                current = current.parent
        else:
            for child in current.children:
                if target_dir_name == child.name:
                    current = child
                    break
    elif 'dir ' in line:
        directory_name = line.split(' ')[1]
        Node(directory_name, parent=current, size=0, directory=True)
    else:
        file_size, file_name = line.split(' ')
        Node(file_name, parent=current, size=file_size, directory=False)


# for pre, fill, node in RenderTree(root):
#     print("%s%s - %s" % (pre, node.name, node.size))

# total_size
total_size = 0

for node in PreOrderIter(root):
    total_size += int(node.size)

free_space = 70000000 - total_size
to_delete = 30000000 - free_space

directory_sizes = []

for node in PreOrderIter(root):
    if node.directory:
        children = node.descendants
        size_tmp = 0
        for child in children:
            size_tmp += int(child.size)
        things = [node.name, size_tmp]
        directory_sizes.append(things)

# fancy sorting thingies
directory_sizes.sort(key=lambda x: x[1])

target = ''
target_size = 0
for directory in directory_sizes:
    directory_name = directory[0]
    directory_size = int(directory[1])
    if directory_size >= int(to_delete):
        target_size = directory_size
        target = directory_name
        break

print('target_size: ', target_size)
