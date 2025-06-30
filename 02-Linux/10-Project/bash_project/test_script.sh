#!/bin/bash

if ! command -v stress-ng >/dev/null 2>&1; then
  sudo apt-get install -y stress-ng
fi

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Derive the root project directory based on a known path pattern
PROJECT_DIR="$(echo "$SCRIPT_DIR" | sed -E 's|(.*\/Cyber2).*|\1|')"

source "$PROJECT_DIR/config.sh"

while true; do
	# Set the path to your test scripts directory
	TEST_DIR="$PROJECT_DIR/tests"

	# Find all executable test scripts in the directory (modify pattern as needed)
	TESTS=($(find "$TEST_DIR" -maxdepth 1 -type f -executable -name 'test_*' | sort))

	if [[ ${#TESTS[@]} -eq 0 ]]; then
  		echo "No test scripts found in $TEST_DIR."
  		exit 1
	fi

	echo "Available tests:"
	for i in "${!TESTS[@]}"; do
  	TEST_NAME=$(basename "${TESTS[$i]}")
  	echo "$((i+1))) $TEST_NAME"
	done

	echo
	read -p "Select a test to run [1-${#TESTS[@]}]: " choice

	if [[ "$choice" =~ ^[1-9][0-9]*$ ]] && (( choice >= 1 && choice <= ${#TESTS[@]} )); then
    	echo "Running ${TESTS[$((choice-1))]}..."
    	"${TESTS[$((choice-1))]}"
    	echo
    	read -p "Press Enter to return to the menu..."
  	elif [[ "$choice" -eq $(( ${#TESTS[@]} + 1 )) ]]; then
    	echo "Exiting."
    	exit 0
  	else
    	echo "Invalid selection."
  	fi

  echo
done
