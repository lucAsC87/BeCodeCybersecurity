# get_system_info displays key system information including user, host, OS, kernel, uptime, shell, terminal, CPU model, and memory usage with color-coded labels.
get_system_info(){

    # Print the current username
    echo -e "${COLOR_TEXT}User: ${COLOR_SELECTED}$USER${COLOR_RESET}"

    # Print the system hostname
    echo -e "${COLOR_TEXT}Host: ${COLOR_SELECTED}$(hostname)${COLOR_RESET}"

    # Print the OS name (tries lsb_release first, falls back to /etc/os-release)
    echo -e "${COLOR_TEXT}OS: ${COLOR_SELECTED}$(lsb_release -ds 2>/dev/null || grep PRETTY_NAME /etc/os-release | cut -d= -f2- | tr -d '\"')${COLOR_RESET}"

    # Print the running kernel version
    echo -e "${COLOR_TEXT}Kernel: ${COLOR_SELECTED}$(uname -r)${COLOR_RESET}"

    # Print how long the system has been up
    echo -e "${COLOR_TEXT}Uptime: ${COLOR_SELECTED}$(uptime -p)${COLOR_RESET}"

    # Print the current user's shell
    echo -e "${COLOR_TEXT}Shell: ${COLOR_SELECTED}$SHELL${COLOR_RESET}"

    # Print the terminal type being used
    echo -e "${COLOR_TEXT}Terminal: ${COLOR_SELECTED}$TERM${COLOR_RESET}"

}


# get_hardware_info displays detailed hardware information including CPU model, core count, architecture, memory usage, GPU details, and disk device information with color-coded labels.
get_hardware_info(){

    # Print the CPU model name
    echo -e "${COLOR_TEXT}CPU: ${COLOR_SELECTED}$(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | sed 's/^ //')${COLOR_RESET}"

    # Print the total number of CPU cores
    echo -e "${COLOR_TEXT}Cores: ${COLOR_SELECTED}$(nproc)${COLOR_RESET}"

    # Print the system architecture (e.g. x86_64, arm64)
    echo -e "${COLOR_TEXT}Architecture: ${COLOR_SELECTED}$(uname -m)${COLOR_RESET}"

    # Print current memory usage (used / total in human-readable format)
    echo -e "${COLOR_TEXT}Memory: ${COLOR_SELECTED}$(free -h | awk '/^Mem:/ {print $3 " / " $2}')${COLOR_RESET}"

    # Print GPU info (VGA/3D/2D controllers from lspci)
    echo -e "${COLOR_TEXT}GPU: ${COLOR_SELECTED}$(lspci | grep -i 'vga\|3d\|2d' | cut -d: -f3 | sed 's/^ //')${COLOR_RESET}"

    # Print block devices (disks only) with name, size, and model
    echo -e -n "${COLOR_TEXT}Disk(s): ${COLOR_RESET}"
    echo -e "Name       Size       Model"

    lsblk -d -o NAME,SIZE,MODEL,TYPE -P | while read -r line; do
        eval "$line"
        if [[ "$TYPE" == "disk" ]]; then
            printf "         ${COLOR_SELECTED}%-10s %-10s %-s${COLOR_RESET}\n" "$NAME" "$SIZE" "$MODEL"
        fi
    done
}
