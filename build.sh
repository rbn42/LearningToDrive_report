#!/bin/bash
export ORGFILE=./report.org

#pdf暂且弄不了中文,所以还是输出html吧
rm ./report.pdf
pandoc \
    -s -o ./report.pdf \
    --latex-engine=xelatex \
    $ORGFILE

    #--template=./pm-template.latex \
    #-V mainfont=Hei \

rm ./report.tex
pandoc \
    -s -o ./report.tex \
    --latex-engine=xelatex \
    $ORGFILE


rm ./report.html
pandoc -s -o ./report.html $ORGFILE
