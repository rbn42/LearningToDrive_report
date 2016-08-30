"""
yaourt graphviz
"""
import sys
import os.path
for path in sys.argv[1:]:
    cmd = 'dot -Tsvg -O %s' % path
    print(cmd)
    os.system(cmd)
