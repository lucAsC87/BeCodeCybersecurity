#!/bin/bash

export LC_ALL=C

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Derive the root project directory based on a known path pattern
PROJECT_DIR="$(echo "$SCRIPT_DIR" | sed -E 's|(.*\/Cyber2).*|\1|')"

# Source shared configuration (should define things like $LOG_DIR, $LOG_FILE, $COLOR_*)
source "$PROJECT_DIR/config.sh"

# Ensure log directories and files exist
mkdir -p "$LOG_DIR"
touch "$LOG_FILE"
touch "$RECENT_LOG_FILE"

# Define menu options for each section of the tool
main_menu=("System Info" "IDS" "Hardware Management" "Process Management" "Network Management" "User Management" "EXIT")
hardware_menu=("CPU" "DISK" "RAM" "back")
network_menu=("TRAFFIC" "CHECK SUPICIOUS PORT ACTIVITY" "back")
user_menu=("LOGS" "back")
ids_menu=("ONE TIME" "REAL TIME" "RECENT WARNINGS" "back")
system_info_menu=("INFO" "SPECS" "back")
process_menu=("DEMANDING PROCESSES" "PROCESS TREE" "LOAD AVERAGE" "back")

# is_menu returns success if the given menu item corresponds to a submenu category, or failure if it is an endpoint action.
is_menu() {
  case "$1" in
    "Hardware Management"|"Network Management"|"User Management"|"IDS"|"System Info"|"Process Management")
      return 0  # True: it's a submenu
      ;;
    *) return 1 ;;  # False: it's an endpoint
  esac
}

# navigate_menu displays a menu, allows navigation with arrow keys, highlights the current selection, and returns the index of the selected item when Enter is pressed.
navigate_menu() {
  local -n menu_items=$1   # Pass menu by name (reference)
  local prompt=$2          # Prompt title for the menu
  local selected=0         # Default selected index

  while true; do
    clear
    echo -e "${BOLD}${COLOR_MENU}=== $prompt ===${COLOR_RESET}"

    for i in "${!menu_items[@]}"; do
      local item="${menu_items[$i]}"
      local color

      # Choose color based on item type
      if [[ "$item" == "back" || "$item" == "EXIT" ]]; then
        color=$COLOR_BACK
      elif is_menu "$item"; then
        color=$COLOR_MENU
      else
        color=$COLOR_ENDPOINT
      fi

      # Highlight selected item
      if [[ $i -eq $selected ]]; then
        echo -e "> ${COLOR_SELECTED}${item}${COLOR_RESET}"
      else
        echo -e "  ${color}${item}${COLOR_RESET}"
      fi
    done

    # Read user input (arrow keys)
    read -rsn1 key
    if [[ $key == $'\x1b' ]]; then
      read -rsn2 -t 0.1 key  # Handle arrow keys
    fi

    case "$key" in
      "[A") ((selected--)); ((selected < 0)) && selected=$((${#menu_items[@]} - 1)) ;;  # Up
      "[B") ((selected++)); ((selected >= ${#menu_items[@]})) && selected=0 ;;         # Down
      "") return $selected ;;  # Enter key: return index
    esac
  done
}

# handle_submenu displays a submenu, processes user selection, and invokes the corresponding UI function for the chosen action.
handle_submenu() {
  local -n submenu=$1  # Menu passed by name
  local title=$2       # Title for the submenu

  while true; do
    navigate_menu submenu "$title"
    choice=$?
    selected="${submenu[$choice]}"

    # Go back to the previous menu
    if [[ "$selected" == "back" ]]; then
      return
    fi

    # Call the correct function depending on selected submenu and item
    case "$title" in
      "System Info")
        case "$selected" in
          "INFO") ui_get_info ;;
          "SPECS") ui_get_specs ;;
        esac
        ;;

      "IDS")
        case "$selected" in
          "ONE TIME") ui_get_one_time ;;
          "REAL TIME") ui_get_real_time ;;
          "RECENT WARNINGS") ui_get_recent_warnings ;;
        esac
        ;;

      "Hardware Management")
        case "$selected" in
          "CPU") ui_get_cpu ;;
          "DISK") ui_get_disk ;;
          "RAM") ui_get_ram ;;
        esac
        ;;

      "Process Management")
        case "$selected" in
          "DEMANDING PROCESSES") ui_get_demanding_process ;;
          "PROCESS TREE") ui_get_process_tree ;;
          "LOAD AVERAGE") ui_get_load_average ;;
        esac
        ;;

      "Network Management")
        case "$selected" in
          "TRAFFIC") ui_get_traffic ;;
          "CHECK SUPICIOUS PORT ACTIVITY") ui_get_supicious_port ;;
        esac
        ;;

      "User Management")
        case "$selected" in
          "LOGS") ui_get_logs ;;
        esac
        ;;
    esac
  done
}

# main launches the interactive menu system and routes user selections to the appropriate submenu or exits the script.
main() {
  while true; do
    navigate_menu main_menu "Main Menu"
    choice=$?
    selected="${main_menu[$choice]}"

    # Route to appropriate submenu or exit
    case "$selected" in
      "Hardware Management") handle_submenu hardware_menu "Hardware Management" ;;
      "Network Management") handle_submenu network_menu "Network Management" ;;
      "User Management") handle_submenu user_menu "User Management" ;;
      "IDS") handle_submenu ids_menu "IDS" ;;
      "System Info") handle_submenu system_info_menu "System Info" ;;
      "Process Management") handle_submenu process_menu "Process Management" ;;
      "EXIT")
        clear
        echo "Exiting..."
        exit 0 ;;
    esac
  done
}

# Start the program
main
