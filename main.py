import io
from newick import load


def print_descendants(node, depth):
    print '  ' * depth + str(node.name) + ' : ' + str(node.length)
    if len(node.descendants) > 0:
        for desc in node.descendants:
            print_descendants(desc, depth + 1)


with io.open('trees.txt', encoding='utf8') as fp:
    trees = load(fp)
    print trees

    for tree in trees:
        depth_index = 0
        print 'Tree\n'
        print_descendants(tree, 0)
        print '\n\n'
