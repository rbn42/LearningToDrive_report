#!/bin/bash
export ORGFILE=./report.org

#pdf暂且弄不了中文,所以还是输出html吧
rm ./report.pdf
pandoc \
    -o ./report.pdf \
    --latex-engine=xelatex \
    $ORGFILE

    #--template=./pm-template.latex \
    #-V mainfont=Hei \

rm ./report.html
pandoc -s -o ./report.html $ORGFILE
