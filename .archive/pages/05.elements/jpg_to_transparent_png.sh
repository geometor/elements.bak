#!/usr/bin/env bash

for file in $(find -name "*.jpg")
do
  echo $file
  convert $file -fuzz 4% -transparent white "${file%.jpg}.png"
  mv $file ../../archive/

done
