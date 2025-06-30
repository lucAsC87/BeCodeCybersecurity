#!/bin/bash

echo "Starting stress-ng memhog for 20 seconds..."
stress-ng --vm 1 --vm-bytes 80% --timeout 20s
echo "Memory stress test finished."
