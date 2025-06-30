#!/bin/bash

echo "Testing disk write/read for 20 seconds..."
stress-ng --hdd 1 --hdd-bytes 50G --timeout 50s
echo "Disk stress test finished."
