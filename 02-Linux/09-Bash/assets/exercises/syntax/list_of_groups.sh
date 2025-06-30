#!/bin/bash
list=($(groups $USER))
for group in "${list[@]:2}"; do
	echo "$USER is part of the group $group"
done
