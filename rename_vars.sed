# you must use sed -E for backrefs like \1 to work
# cmd: sed -i -Ef <this_file> <target_file>
s/\$(\w+)/${\1}/g
