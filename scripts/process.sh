#!/bin/bash

OUTPUT=images/montage

mkdir -p $OUTPUT

# Sprites
montage data/*/sprite.png -background transparent -crop 64x64+0+0 -geometry 64x64 $OUTPUT/sprites-front.png
montage data/*/sprite.png -background transparent -crop 64x64+64+0 -geometry 64x64 $OUTPUT/sprites-front-shiny.png
montage data/*/sprite.png -background transparent -crop 64x64+128+0 -geometry 64x64 $OUTPUT/sprites-back.png
montage data/*/sprite.png -background transparent -crop 64x64+192+0 -geometry 64x64 $OUTPUT/sprites-back-shiny.png

# Icons
montage data/*/icon.png -background transparent -crop 32x32+0+0 -geometry 32x32 $OUTPUT/icons-frame1.png
montage data/*/icon.png -background transparent -crop 32x32+0+32 -geometry 32x32 $OUTPUT/icons-frame2.png
