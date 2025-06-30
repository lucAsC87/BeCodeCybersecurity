# ui_get_one_time runs a one-time network monitoring session, displays detected warnings, and appends them to the main log file before returning to the IDS menu.
ui_get_one_time(){
    LOG_FILE="$LOG_DIR/temp_logs.log"
    touch "$LOG_FILE"                      # Create temporary log file
    clear                                 # Clear terminal screen
    tput civis                            # Hide the cursor
    trap "tput cnorm; stty echo" EXIT    # Ensure cursor is restored when script exits

    echo -e "${BOLD}${COLOR_MENU}=== Choose Network Interface ===${COLOR_RESET}\n"
    IFACE=$(choose_interface)             # Let user pick network interface to monitor

    clear
    echo -e "${BOLD}${COLOR_MENU}=== Please Wait a Few Seconds to View the Warnings ===${COLOR_RESET}"
    monitor_all                          # Run monitoring; write warnings to LOG_FILE

    clear
    echo -e "${BOLD}${COLOR_MENU}=== WARNINGS!!!! ===${COLOR_RESET}\n"
    cat "$LOG_FILE"                      # Display collected warnings to user

    cat "$LOG_FILE" >> "$LOG_DIR/all_system_logs.log"  # Append warnings to main log file

    WARNING_COUNT=$(wc -l < "$LOG_FILE")  # Count number of warnings found
    rm "$LOG_FILE"                        # Remove temporary log file
    LOG_FILE="$LOG_DIR/all_system_logs.log"  # Reset log file variable to main log

    echo
    echo -e "Found $WARNING_COUNT warnings."
    read -p "Press [Enter] to return to IDS menu..."  # Wait for user input before exiting
}


# ui_get_real_time provides a real-time interactive display of network monitoring warnings, updating continuously until the user exits.
ui_get_real_time(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== Choose Network Interface ===${COLOR_RESET}"
    IFACE=$(choose_interface)            # Let user pick network interface to monitor

    clear
    echo -e "${BOLD}${COLOR_MENU}=== Please Wait a Few Seconds to View the Warnings ===${COLOR_RESET}"

    WARNING_COUNT=0                     # Initialize total warnings count

    # Start real time loop
    while true; do
        LOG_FILE="$LOG_DIR/temp_logs.log"
        touch $LOG_FILE                 # Create temporary log file
        monitor_all                    # Run monitoring; write warnings to LOG_FILE

        tput cup 0 0; tput ed          # Reset cursor and clear screen for live update
        echo -e "${BOLD}${COLOR_MENU}=== WARNINGS!!!! ===${COLOR_RESET}\n"
        cat $LOG_FILE                  # Show current warnings

        cat $LOG_FILE >> "$LOG_DIR/all_system_logs.log"  # Append warnings to main log file

        COUNT=$(wc -l < "$LOG_FILE")  # Count warnings in this batch
        (( WARNING_COUNT += COUNT ))   # Accumulate total warnings

        echo -e "\nFound $WARNING_COUNT warnings since the start of real time monitoring (view \"$LOG_DIR/all_system_logs.log\" to see them all)"
        echo
        echo -e "Press [Enter] to return to IDS menu..."

        rm $LOG_FILE                  # Remove temp log file for next iteration

        # Exit loop if user presses Enter key
        read -t 1 -s input && [[ -z "$input" ]] && break
    done

    LOG_FILE="$LOG_DIR/all_system_logs.log"  # Reset log file variable
    tput cnorm                            # Restore cursor visibility
}

# ui_get_recent_warnings displays the contents of the recent warnings log file and waits for user input before returning to the IDS menu.
ui_get_recent_warnings(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== RECENT WARNINGS ===${COLOR_RESET}\n"
    cat "$RECENT_LOG_FILE"               # Output the contents of recent warnings log
    echo
    read -p "Press [Enter] to return to IDS menu..."  # Wait for user confirmation before returning
}