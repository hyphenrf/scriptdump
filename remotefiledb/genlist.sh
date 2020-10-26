#!/bin/sh
LC_ALL=C
repopath="/sol"

# Generate package list from repo Local -- replace with any repo you want to
# know the file listings of all its packages
# output is 2 header lines followed by a list in the form of:
# <pkgname>\s+- <description>
echo "Generating package list, please wait..."
eopkg -N la Local |grep -v dbginfo |cut -d" " -f1 |sed 1,2d > /tmp/package-list.txt
# additional packages that don't follow standard placement in Shannon (just for
# testing purposes)
cat <<... >>/tmp/package-list.txt
alsa-firmware
alsa-lib
alsa-plugins
alsa-tools
alsa-utils
...

# Move into appropriate directory: scripts work in subshell -- using cd is fine
cd "${repopath}"
# Find all eopkgs in the remote repo. This makes later execution time at least
# 50% faster. Probably quadratic -> linear improvement and greatly simplifies
# processpkg script.
find ./ -name "*.eopkg" \! -name "*.delta.eopkg" |sort -rn > /tmp/package-eopkgs.txt

# Make tempdir
mkdir -vp /tmp/lists

# Start processing -- can use GNU parallel on this kind of data
while read i; do ./processpkg $i /tmp/package-eopkgs.txt; done < /tmp/package-list.txt
