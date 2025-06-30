# ui_get_cpu displays a real-time terminal interface showing average and per-core CPU utilization, refreshing every second until the user presses Enter to exit.
ui_get_cpu(){
    clear
    tput civis                     # Hide the cursor
    trap "tput cnorm; stty echo" EXIT  # Ensure cursor is restored when script exits

    echo -e "${BOLD}${COLOR_MENU}=== Please Wait 2 Seconds for Real-Time CPU Utilization ===${COLOR_RESET}"

    # Start real-time loop
    while true; do
        avg_cpu=$(get_average_cpu_stats)   # Get system-wide average CPU usage
        all_cpu=$(get_all_cpu_stats)       # Get CPU usage per core

        tput cup 0 0; tput ed              # Reset cursor position and clear screen from cursor down
        echo -e "${BOLD}${COLOR_MENU}=== Real-Time CPU Average Utilization ===${COLOR_RESET}\n"
        echo "$avg_cpu"
        echo
        echo -e "${COLOR_MENU}${BOLD}=== Real-Time CPU Utilization Per Core ===${COLOR_RESET}\n"
        echo "$all_cpu"

        echo -e "\nPress [Enter] to exit AVERAGE CPU monitoring."

        read -t 1 -s input && [[ -z "$input" ]] && break    # Exit if Enter pressed
    done

    tput cnorm  # Restore cursor
}


# ui_get_disk provides a real-time terminal interface displaying current disk usage and disk I/O statistics, refreshing every second until the user presses Enter to exit.
ui_get_disk(){
    clear
    tput civis                         # Hide the cursor
    trap "tput cnorm; stty echo" EXIT  # Ensure cursor is restored when script exits

    echo -e "${BOLD}${COLOR_MENU}=== Disk Usage and I/O ===${COLOR_RESET}"

    # Start real time loop
    while true; do
        disk_usage=$(get_disk_usage)        # Get filesystem disk usage
        disk_io=$(get_disk_io_stats)        # Get disk I/O stats (read/write/util)

        tput cup 0 0; tput ed               # Reset cursor position and clear screen from cursor down
        echo -e "${BOLD}${COLOR_MENU}=== Disk Usage ===${COLOR_RESET}\n"
        echo "$disk_usage"
        echo -e "\n${BOLD}${COLOR_MENU}=== Disk I/O Stats ===${COLOR_RESET}\n"
        echo "$disk_io"

        echo -e "\nPress [Enter] to exit real-time view."

        read -t 1 -s input && [[ -z "$input" ]] && break  # Exit if Enter pressed
    done

    tput cnorm  # Show cursor again
}


# ui_get_ram provides a real-time terminal interface for monitoring system memory and swap usage, updating statistics every second until the user presses Enter to exit.
ui_get_ram(){
    clear
    tput civis                         # Hide the cursor
    trap "tput cnorm; stty echo" EXIT  # Ensure cursor is restored when script exits

    echo -e "${BOLD}${COLOR_MENU}=== Please Wait 1 Second for Real-Time Memory and Swap Usage ===${COLOR_RESET}"

    # Start real time loop
    while true; do
        mem_stats=$(get_memory_stats)   # Collect RAM usage statistics
        swap_stats=$(get_swap_stats)    # Collect swap usage and activity statistics

        tput cup 0 0; tput ed           # Reset cursor position and clear screen from cursor down
        echo -e "${BOLD}${COLOR_MENU}=== Real-Time Memory Usage ===${COLOR_RESET}\n"
        echo "$mem_stats"
        echo -e "\n${BOLD}${COLOR_MENU}=== Real-Time Swap Usage ===${COLOR_RESET}\n"
        echo "$swap_stats"

        echo -e "\nPress [Enter] to exit RAM monitoring."

        read -t 1 -s input && [[ -z "$input" ]] && break  # Exit if Enter pressed
    done

    tput cnorm  # Restore cursor visibility
}
