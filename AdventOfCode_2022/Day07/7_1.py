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


for pre, fill, node in RenderTree(root):
    print("%s%s - %s" % (pre, node.name, node.size))

size = 0
for node in PreOrderIter(root):
    if node.directory:
        children = node.descendants
        size_tmp = 0
        for child in children:
            size_tmp += int(child.size)
        if size_tmp <= 100000:
            size += size_tmp

print(size)
