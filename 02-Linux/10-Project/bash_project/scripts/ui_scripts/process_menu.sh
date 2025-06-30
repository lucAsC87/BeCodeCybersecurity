# ui_get_demanding_process displays a real-time, continuously updating list of the top CPU- and memory-consuming processes until the user presses Enter to exit.
ui_get_demanding_process(){
    clear
    tput civis                 # Hide the cursor
    trap "tput cnorm; stty echo" EXIT # Ensure cursor is restored when script exits
    
    echo -e "${BOLD}${COLOR_MENU}=== Top CPU-consuming Processes ===${COLOR_RESET}\n"
    
    # Start real time loop
    while true; do
        top_cpu_process=$(get_top_processes_cpu)    # Get top CPU-consuming processes info
        top_mem_process=$(get_top_processes_mem)    # Get top memory-consuming processes info

        tput cup 0 0; tput ed   # Reset cursor position and clear screen from cursor down
        
        echo -e "${BOLD}${COLOR_MENU}=== Top CPU-consuming Processes ===${COLOR_RESET}\n"
        echo "$top_cpu_process"
        echo  
        echo -e "${BOLD}${COLOR_MENU}=== Top Memory-consuming Processes ===${COLOR_RESET}\n"
        echo "$top_mem_process"       
        echo -e "\nPress [Enter] to exit DEMANDING PROCESS monitoring." 
        
        read -t 1 -s input && [[ -z "$input" ]] && break    # Exit if Enter pressed
    done
    
    tput cnorm                  # Restore cursor visibility
}

# ui_get_process_tree displays the system's process tree and waits for user input before returning to the process management menu.
ui_get_process_tree(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== Process Tree ===${COLOR_RESET}\n"
    show_process_tree
    read -p "Press [Enter] to return to Process Management menu..."
}

# ui_get_load_average clears the terminal, displays system load averages for 1, 5, and 15 minutes, and waits for user input before returning to the menu.
ui_get_load_average(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== Load Average Over 1min, 5min and 15min ===${COLOR_RESET}\n"
    show_load
    read -p "Press [Enter] to return to Process Management menu..."
}
