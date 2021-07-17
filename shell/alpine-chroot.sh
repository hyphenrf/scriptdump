#!/bin/sh
distro=Alpine

# Prepping
cd "${distro}"
#--------
mkdir -p /tmp/"${distro}"
chmod -R 1777 /tmp/"${distro}"

mount -t proc none proc && mpoints="proc ${mpoints}"
mount -t sysfs none sys && mpoints="sys ${mpoints}"
mount -t devtmpfs /dev dev && mpoints="dev ${mpoints}"
mount -t devpts /dev/pts dev/pts && mpoints="dev/pts ${mpoints}"
mount -t tmpfs /tmp/survey tmp && mpoints="tmp ${mpoints}"

if [ -L /dev/shm ] && [ -d /run/shm ]; then
	mkdir -p run/shm
	mount -o bind -o private /run/shm run/shm
    mpoints="run/shm ${mpoints}"
fi

# Chroot
chroot . /bin/sh -ic "su -"

# Cleanup and logging
cd ..
#----
echo "===========${distro}	:$(date)============" >>.umount
# echo points: ${mpoints} >>.umount
for point in ${mpoints}
do 
	umount "${distro}/${point}" 2>>.umount
done
echo "Umount done." >>.umount

echo
