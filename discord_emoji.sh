#!/bin/sh

# Configuration:
authfile=auth

###############################################################################

# Pre-tests:
[ -f ${authfile} ] || {
	echo "error: user authtoken doesn't exist. exiting."; 
	exit 1;
}

auth=$(cat ${authfile})

set -- /tmp/discord.*
if [ -d $1 ] # /tmp/discord.* matches any directory?
then 
	temp=$1
	echo "info: using ${temp}"
else 
	temp=$(mktemp -dt discord.XXXX)
fi


# Function definitions:
request()
{
	local url="${1}" out="${2}" err="${3}" status=$4

	local response=$(curl -w "%{http_code}" -s -H "Authorization: ${auth}" \
		${url} -o ${out})
	
	[ "${response}" = "200" ] || {
		printf "error: ${err} [server: ${response}]\n";
		[ -n "${status}" ] && exit ${status};
	}
}


getguilds()
{		
	request "https://discordapp.com/api/users/@me/guilds" \
		${temp}/guilds.json "failed to pull guilds." 2
	
	jq -r ".[]|.id" ${temp}/guilds.json |
	tee ${temp}/guilds
}


guildmoji() 
{ 
	local guild="$1"
	mkdir -p "${guild}"
	
	if [ -e ${guild}/emoji.json ]
	then echo "info: emoji.json already exists for guild ${guild}"
	else 
		request "https://discordapp.com/api/guilds/${guild}/emojis" \
			"${guild}"/emoji.json "failed to pull emojis from guild ${guild}." 3
	fi
}


getmoji()
{
	local guild="$1" emojid="$2" emojnm="${3}" 
	local animated="$4"
	[ ${animated} = 'true' ] && ext='gif' || ext='png'
	
	if [ -e "${guild}/${emojnm}.${ext}" ]
	then echo "file exists: ${guild}/${emojnm}.${ext}"
	else
		echo "GET https://cdn.discordapp.com/emojis/${emojid}" 
		echo "FILE ${guild}/${emojnm}.${ext}"
		request "https://cdn.discordapp.com/emojis/${emojid}" \
			"${guild}/${emojnm}.${ext}"
	fi
}

# Main:

[ -p ${temp}/id.pipe ]    || mkfifo ${temp}/id.pipe
[ -p ${temp}/emoji.pipe ] || mkfifo ${temp}/emoji.pipe

{ cat ${temp}/guilds 2>/dev/null || getguilds; } > ${temp}/id.pipe&
while read -r id
do
	guildmoji $id
	mx=$(jq ".|length" $id/emoji.json)
	echo "==========fetching ${mx} custom emojis from guild ${id}=========="
	
	jq -r '.[]|"\(.id):\(.name):\(.animated)"' $id/emoji.json \
		> ${temp}/emoji.pipe&
	while IFS=: read -r eid enm anm
	do getmoji $id $eid "${enm}" $anm
	done <${temp}/emoji.pipe
done <${temp}/id.pipe
