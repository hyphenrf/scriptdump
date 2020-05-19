#!/bin/sh

[ -n "$1" ] || {
	echo "Please enter a C program to run.";
	exit 1;
}

# Do getopts here, defining functions -f and changing includes -I and being
# interactive in general, option -p can print the program and take confirmation
# before running it.
# Additionally there should be a way to pass flags to the compiler.

PROGRAM="${1}"

set -- /tmp/QUICKRUN*
if [ -d $1 ]; then
	cd $1
else
	cd $(mktemp -d -t QUICKRUN.XXXX)
fi

if  [ -f "${PROGRAM}" ]
then tmp="${PROGRAM}"
else
	tmp=$(mktemp -p $(pwd) --suffix=.c)
	cat <<. >${tmp}
#include <stdio.h>

void main(int argc, char *argv[]) {
	$(echo ${PROGRAM})
}
.
fi

gcc -o ${tmp%.c} -x c ${tmp};

[ $? -ne 0 ] && echo "Did not run." || { 
	${tmp%.c};
	rm -f $(pwd)/*;
};


cd -> /dev/null
