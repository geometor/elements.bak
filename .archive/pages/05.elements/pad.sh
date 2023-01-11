#!/usr/bin/env bash
for file in $(find -name "*.png")
do
  echo $file
  mv $file .$file
  convert -background none -gravity center .$file -resize 600x400 -extent 700x500 $file
done

