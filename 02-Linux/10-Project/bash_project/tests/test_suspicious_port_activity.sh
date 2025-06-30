#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "You need root privileges to execute the script."
  exec sudo "$0" "$@"
fi

nc -lvp 54321 &
LISTENER_PID=$!

sleep 2

nc 127.0.0.1 54321

kill $LISTENER_PID
