# ui_get_info displays system information in a formatted menu and waits for user input before returning to the System Info menu.
ui_get_info(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== System Info ===${COLOR_RESET}\n"
    get_system_info
    echo
    read -p "Press [Enter] to return to System Info menu..."
}

# ui_get_specs displays hardware information in a formatted menu and waits for user input before returning to the System Info menu.
ui_get_specs(){
    clear
    echo -e "${BOLD}${COLOR_MENU}=== HARDWARE INFO ===${COLOR_RESET}\n"
    get_hardware_info
    echo
    read -p "Press [Enter] to return to System Info menu..."
}