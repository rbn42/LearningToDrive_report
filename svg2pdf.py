import sys
import os.path
for path in sys.argv[1:]:
    path, ext = os.path.splitext(path)
    dst = path + '.pdf'
#    if os.path.exists(dst):
#        os.remove(dst)
    cmd = 'inkscape -D -z --file=%s.svg --export-pdf=%s.pdf --export-latex'
    cmd = cmd % (path, path)
    print(cmd)
    os.system(cmd)
