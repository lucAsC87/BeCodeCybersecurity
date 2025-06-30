#!/bin/bash

CORES=$(nproc)
echo "Stressing CPU with $CORES workers for 10 seconds..."
stress-ng --cpu "$CORES" --timeout 10s
echo "CPU stress test finished."
