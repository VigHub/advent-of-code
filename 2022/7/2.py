class FileSystem: 
    
    def __init__(self, name, parent=None, is_file=False, size=0):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = size
        self.is_file = is_file
    
    def add_child(self, name, is_file=False, size=0):
        if name in self.children:
            return
        child = FileSystem(name, parent=self, is_file=is_file, size=size)
        self.children[name] = child
    
    def get_size(self):
        if self.is_file:
            return self.size
        size = 0
        for child in self.children.values():
            size += child.get_size()
        self.size = size
        return self.size


with open('2022/7/in.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    TOT_SPACE = 70000000
    SPACE_REQUIRED = 30000000
    filesystem = FileSystem('/', is_file=False, size=0)
    root = filesystem
    for line in lines:
        line = line.split(' ')
        if line[0] == '$':
            # command
            if line[1] == 'cd':
                if line[2] == '..':
                    filesystem = filesystem.parent
                elif line[2] == '/':
                    filesystem = root
                else:
                    filesystem = filesystem.children[line[2]]
            elif line[1] == 'ls':
                continue
            else:
                assert False
        elif line[0] == 'dir':
            # add dir to filesystem
            filesystem.add_child(line[1], is_file=False, size=0)
        else:
            size = int(line[0])
            filesystem.add_child(line[1], is_file=True, size=size)
    # trigger calculate of size
    root.get_size()
    ##
    space_available = TOT_SPACE - root.size
    space_needed_to_del = SPACE_REQUIRED - space_available
    res = TOT_SPACE
    dir_to_del = '/'
    def bfs(fs: FileSystem, tab=0):
        global res
        global dir_to_del
        print('\t'*tab, fs.name, fs.size)
        if fs.is_file:
            return
        if fs.size >= space_needed_to_del and res > fs.size:
            res = fs.size
            dir_to_del = fs.name
        for child in fs.children.values():
            bfs(child, tab+1)
    bfs(root)
    print(dir_to_del, res)


            

                    
