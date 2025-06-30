# get_disk_io_stats collects and displays disk I/O statistics for physical devices, highlighting metrics that exceed predefined thresholds.
#
# Uses `iostat` to gather read and write throughput (in MB/s) and utilization percentage for each detected disk device, formatting the output with alerts for high usage. Only physical disks matching standard device patterns are included.
get_disk_io_stats() {
    # Check if 'iostat' is available; if not, prompt the user and exit
    if ! command -v iostat &>/dev/null; then
        echo -e "${COLOR_ABOVE_THRESHOLD}iostat not found. Please install the sysstat package.${COLOR_RESET}"
        return
    fi

    local print_statements=""

    # Process disk I/O stats, one device per line
    while read -r dev read_mb write_mb util; do
        # Add a bold label for each device
        print_statements+="${BOLD}Device ${dev}:${COLOR_RESET}\n"

        # Append formatted metrics using print_metric (with thresholds and alerts)
        print_statements+="$(print_metric "Read (MB/s)" "$read_mb" $DEFAULT_DISK_READ_THRESHOLD "over" "High read on $dev" "DISK" "WARNING")  "
        print_statements+="$(print_metric "Write (MB/s)" "$write_mb" $DEFAULT_DISK_WRITE_THRESHOLD "over" "High write on $dev" "DISK" "WARNING")  "
        print_statements+="$(print_metric "Util (%)" "$util" $DEFAULT_DISK_TPS_THRESHOLD "over" "High utilization on $dev" "DISK" "WARNING")${COLOR_RESET}\n"
    
    # Use iostat to get extended device stats, sample over 1 second
    done < <(
        iostat -dx 1 1 | awk '
            BEGIN { found = 0 }
            /^Device/ { found = 1; next }
            # Filter for valid devices: sdX, nvmeX, vdX, hdX
            found && $1 ~ /^(sd|nvme|vd|hd)/ {
                device = $1
                rkbs = $3     # read KB/s
                wkbs = $8     # write KB/s
                util = $(NF)  # %util, usually last column

                # Convert KB/s to MB/s
                read_mb = rkbs / 1024
                write_mb = wkbs / 1024

                # Print space-separated stats for the while loop
                printf "%s %.2f %.2f %.2f\n", device, read_mb, write_mb, util
            }
        '
    )

    # Display all collected and formatted output
    echo -e "$print_statements"
}

# get_disk_usage collects and displays disk usage statistics for physical disk devices, formatting the output with thresholds and alerts for high usage.
get_disk_usage() {
    local print_statements=""

    # Loop through disk usage output line by line
    while read -r source size used avail pcent; do
        usage_val="${pcent%%%}"  # Strip trailing '%' from usage value

        # Convert sizes from KB to GB for readability
        size_gb=$(awk -v kb="$size" 'BEGIN { printf "%.2f", kb / 1024 / 1024 }')
        used_gb=$(awk -v kb="$used" 'BEGIN { printf "%.2f", kb / 1024 / 1024 }')
        avail_gb=$(awk -v kb="$avail" 'BEGIN { printf "%.2f", kb / 1024 / 1024 }')

        # Start block for each disk device
        print_statements+="${BOLD}Device ${source}:${COLOR_RESET}\n"

        # Append formatted size metrics (no threshold checking needed for raw sizes)
        print_statements+="$(print_metric "Size (GB)" "$size_gb" 0 "none" "")  "
        print_statements+="$(print_metric "Used (GB)" "$used_gb" 0 "none" "")  "
        print_statements+="$(print_metric "Avail (GB)" "$avail_gb" 0 "none" "")  "

        # Check usage percentage against threshold
        print_statements+="$(print_metric "Usage (%)" "$usage_val" $DEFAULT_DISK_THRESHOLD "over" "Disk almost full" "DISK" "INFO")${COLOR_RESET}\n"
    
    # Get disk usage info in kilobytes, ignore irrelevant devices like tmpfs or loop
    done < <(
        df --block-size=1K --output=source,size,used,avail,pcent |
        grep -E '^(/dev/sd|/dev/nvme|/dev/vd|/dev/hd)'  # Only physical disks
    )

    # Output the final formatted report
    echo -e "$print_statements"
}