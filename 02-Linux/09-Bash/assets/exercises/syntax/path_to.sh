#!/bin/bash
echo "Enter a folder or a file to open:"
read path
if [ -f "$path" ]; then
	if file --mime-type "$path" | grep -q "text/"; then
		cat "$path"
	else
		echo "$path is not a text file."
	fi
elif [ -d "$path" ]; then
	ls "$path"
else
	echo "$path doesn't exist or is neither a folder or file"
fi
