#!/bin/bash
python ./dot.py ./images/*.digraph
python ./svg2png.py ./images/*.svg
