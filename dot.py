"""
yaourt graphviz

另一个办法
http://orgmode.org/worg/org-contrib/babel/languages/ob-doc-dot.html
emacs中可以执行dot,并且似乎可以通过table数据动态生成,图片和table因此就互相匹配了

这种办法的问题是,所有代码都inline的方式嵌入在了org文件中,
让人感觉很混乱.
matplotlib什么的还是放在独立脚本中,手动生成图片后再引入org比较好.
"""
import sys
import os.path
for path in sys.argv[1:]:
    cmd = 'dot -Tsvg -O %s' % path
    print(cmd)
    os.system(cmd)
