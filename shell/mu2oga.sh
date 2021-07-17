#!/bin/sh

for i in *.{flac,m4a}
do 

album="$(ffprobe -v quiet -show_format -print_format json "$i" \
        |jq .format.tags.album)"
song="$(echo $i |rev |cut -d '.' -f 2- |rev)"

if [ -d "${album}" ]
then true
else mkdir "${album}"
fi

#ffmpeg -v quiet -i "$i" -c:a libvorbis -q:a 3 "${album}/${song}.oga"
ffmpeg -v quiet -i "$i" -c libvorbis "${album}/${song}.oga"

done
