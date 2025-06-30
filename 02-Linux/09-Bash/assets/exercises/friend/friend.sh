#!/bin/bash

while true; do
	if [ $# -eq 0 ]; then
		echo "Good morning $USER!"
		sleep 1
		read -p "How can I help you today? Math? Do you want to know what time it is? The weather? Or do you want to hear a joke? " option
	else
		option=$1
		shift
	fi
	
	case "$option" in
		time) 
			echo "Sure! Today it's "; date
			break
			;;
		math)
			if [ $# -eq 0 ]; then
				read -p "Ok, write down your operation please: " operation
			else
				operation=$1
				shift
			fi
			echo "$operation" | bc
			break
			;;
		weather)
			if [ $# -eq 0 ]; then
				read -p "Sure! For which city? " city
			else
				city=$1
				shift
			fi
			echo "Here's the weather forecast!"; curl wttr.in/$city
			break
			;;
		joke)
			if [ -f jokes.txt ]; then
				joke=$(shuf -n 1 jokes.txt)
				echo "$joke"
			fi
			break
			;;
		*)
			echo "Sorry, I don't understand."
			if [ "$#" -gt 0 ]; then
				exit 1
			fi
			;;
	esac
done
