#!/bin/sh

# Prepping
cd Alpine
#--------
mkdir -p /tmp/alpine
chmod -R 1777 /tmp/alpine
mpoints=""

sudo mount -t proc none proc && mpoints="${mpoints}proc "
sudo mount -t sysfs none sys && mpoints="${mpoints}sys "
sudo mount -t devtmpfs none dev && mpoints="${mpoints}dev "
sudo mount -t devpts none dev/pts
sudo mount -B /tmp/alpine tmp && mpoints="${mpoints}tmp "

if [ -L /dev/shm ] && [ -d /run/shm ]; then
	mkdir -p run/shm
	sudo mount -B /run/shm run/shm
	sudo mount --make-private run/shm
    mpoints="${mpoints}run/shm "
fi

# Chroot
sudo chroot . /bin/sh -ic "su -"

# Cleanup and logging
cd ..
#----
echo "===========ALPINE	:$(date)============" >>.umount
for point in $mpoints
    do sudo umount -R Alpine/$point 2>>.umount
done
echo "Umount done." >>.umount

echo
