#不保证正确性,
#最终还是以emacs内部输出为准,
#这个脚本的用处是,emacs输出会堵塞较长时间,
#用这个脚本另开进程绕开堵塞
rm part1.html part1.tex part1.pdf
emacs -Q -nw part1.org --eval """
(progn 
(load-file \"./export.el\")
(org-html-export-to-html)
(org-latex-export-to-latex)
(princ \"end\"))
""" --kill 
xelatex -interaction nonstopmode part1.tex 
