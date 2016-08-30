"""
org处理svg太麻烦了,所以转成高像素png
"""
import sys
import os.path
for path in sys.argv[1:]:
    path, ext = os.path.splitext(path)
    src = path + '.svg'
    dst = path + '.png'
    cmd = 'convert  -density 500  -resize 3000x3000 "%s" "%s"' % (src, dst)
    cmd = 'convert  -density 500 "%s" "%s"' % (src, dst)
    print(cmd)
    os.system(cmd)
