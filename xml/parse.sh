#!/usr/bin/bash

source ~/.bashrc

function get_title_case() {
  printf "%s" "$1" | sed 's/.*/\L&/; s/[a-z]*/\u&/g'
  
}
function create_article() {
  folder=$1
  mkdir -p $folder
  title=$2
  content=$3
  id=$4
  summary=$5
  category=$6

  cat <<- EOF > $folder/article.md
---
title:  $( echo ${title,,} | sed 's/./\u&/' | sed 's/\.$//' )
subtitle: 
author:
routes:
  aliases:
    - /$id
collection:
  name: elements
  showCount: true
  showMenu: true
content:
  items: '@self.children'
child_type: article
figure:
  image:
  alt:
  title:
  caption:
taxonomy:
  tag:
  category:
    - $category
---

$summary

===

$content
EOF
}

b=1
for xf in $(fdfind .xml ); do
  echo $xf

  cnt1=$(xmlstarlet sel -t -v "count(//div1)"  $xf)
  for (( n = 1; n <= $cnt1; n++ )); do

    div1h="$(xmlstarlet sel -t -v "//div1[$n]/head" $xf)"
    div1folder="$(printf "%02d" $b).$(slugify "$div1h")"
    div1id="$(xmlstarlet sel -t -v "//div1[$n]/@id" $xf )" 
    # div1content="$(xmlstarlet sel -t -c "//div1[$n]" $xf | sed "s/div./div/g" | sed "s/head/h1/g")"

    create_article "$div1folder" "$div1h" "" "$div1id"

    echo $div1h

    cnt2=$(xmlstarlet sel -t -v "count(//div1[$n]/div2)"  $xf)
    for (( i = 1; i <= $cnt2; i++ )); do

      div2h="$(xmlstarlet sel -t -v "//div1[$n]/div2[$i]/head" $xf)"
      div2folder="$div1folder/$(printf "%02d" $i).$(slugify "$div2h")"
      div2id="$(xmlstarlet sel -t -v "//div1[$n]/div2[$i]/@id" $xf )" 
      # div2content="$(xmlstarlet sel -t -c "//div1[$n]/div2[$i]" $xf | sed "s/div./div/g" | sed "s/head/h1/g")"

      create_article "$div2folder" "$div2h" "" "$div2id"

      echo " -" $div2h

      cnt3=$(xmlstarlet sel -t -v "count(//div1[$n]/div2[$i]/div3)"  $xf)
      for (( j = 1; j <= $cnt3; j++ )); do
        # xmlstarlet sel -t -o "   - " -v "//div1[$n]/div2[$i]/div3[$j]/head" -n $xf
        div3h="$(xmlstarlet sel -t -v "//div1[$n]/div2[$i]/div3[$j]/head" $xf)"
        div3folder="$div2folder/$(printf "%02d" $j).$(slugify "$div3h")"
        div3id="$(xmlstarlet sel -t -v "//div1[$n]/div2[$i]/div3[$j]/@id" $xf )"
        # div3cat="$(xmlstarlet sel -t -v "//div1[$n]/div2[$i]/div3[$j]/@type" $xf )"
        div3summary="$(xmlstarlet sel -t -c "//div1[$n]/div2[$i]/div3[$j]/div4[@type='Enunc']/*" $xf )"
        if [[ !$div3summary ]]; then
          div3summary="$(xmlstarlet sel -t -c "//div1[$n]/div2[$i]/div3[$j]/p[1]" $xf )"
        fi

        div3content="$(xmlstarlet sel -t -c "//div1[$n]/div2[$i]/div3[$j]/*" $xf |\
          sed "s/div./div/g" |\
          sed "s/head/h1/g" |\
          sed "s/note/blockquote/g" |\
          sed "s/<figure\/>//g" |\
          sed "s/<hi rend=/<span class=/g" |\
          sed "s/<\/hi/<\/span/g" |\
          sed "s/<ref target=\"/<a href=\"\//g" |\
          sed "s/ targOrder=\"U\"//g" |\
          sed "s/<\/ref/<\/a/g" |\
          sed "s/<\/p>/<\/p>\n/g" |\
          sed "s/<p>/\n<p>/g" |\
          sed "s/type=/class=/g" |\
          sed "s/ org=\"uniform\"//g" |\
          sed "s/ sample=\"complete\"//g" |\
          sed "s/emph/em/g" )"

        create_article "$div3folder" "$div3h" "$div3content" "$div3id" "$div3summary"

        echo "   -" $div3h

        # cnt4=$(xmlstarlet sel -t -v "count(//div1[$n]/div2[$i]/div3[$j]/p)"  $xf)
        # for (( k = 1; k <= $cnt4; k++ )); do
          # xmlstarlet sel -t -o "     " -v "//div1[$n]/div2[$i]/div3[$j]/p[$k]" -n $xf
        # done

        # cnt4=$(xmlstarlet sel -t -v "count(//div1[$n]/div2[$i]/div3[$j]/div4)"  $xf)
        # for (( k = 1; k <= $cnt4; k++ )); do
          # xmlstarlet sel -t -o "     - " -v "//div1[$n]/div2[$i]/div3[$j]/div4[$k]" -n $xf
        # done
      done
    done
  done
  echo
  ((b++))
done
