#!/bin/bash

# Check if log files exist
if [ ! -f "$LOG_HISTORY_FILE" ]; then
    echo -e "${RED}Error: History log file not found${NC}"
    exit 1
fi

# Clear the screen
clear

# Print fancy header
echo -e "\n${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         Log Analysis in Progress         ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}\n"

# Process history log silently
total_entries=$(wc -l < "$LOG_HISTORY_FILE")
error_count=$(grep -ci "error" "$LOG_HISTORY_FILE")
grep -i "error" "$LOG_HISTORY_FILE" | tail -n 5 > "$LOG_DIR/history_report.txt"

# Process system error logs silently
sudo journalctl -p err --no-pager | tail -n 5 > "$LOG_DIR/system_error_report.txt"

# Get login history
sudo last -n 10 | grep -Ev '^(reboot|shutdown|wtmp|btmp|$)' > "$LOG_DIR/login_history.txt"
total_logins=$(wc -l < "$LOG_DIR/login_history.txt")
unique_users=$(awk '{print $1}' "$LOG_DIR/login_history.txt" | sort -u | wc -l)

# Create backups (overwrite existing ones)
cp -p "$LOG_HISTORY_FILE" "$LOG_DIR/history.backup"
sudo journalctl -p err -n 100 > "$LOG_DIR/system_errors.backup"

# Display beautiful summary
echo -e "\n${GREEN}┌─────────────────────────────────┐${NC}"
echo -e "${GREEN}│       Analysis Summary           │${NC}"
echo -e "${GREEN}└─────────────────────────────────┘${NC}"

echo -e "\n${BLUE} Log Statistics${NC}"
echo -e "   ${YELLOW}•${NC} Total Log Entries: $total_entries"
echo -e "   ${YELLOW}•${NC} Total Error Events: $error_count"

echo -e "\n${BLUE} Login History${NC}"
echo -e "   ${YELLOW}•${NC} Total Logins: $total_logins"
echo -e "   ${YELLOW}•${NC} Unique Users: $unique_users"
echo -e "   ${YELLOW}•${NC} Last 10 Logins:"
sudo last -n 10

echo -e "\n${BLUE} Report Details${NC}"
echo -e "   ${YELLOW}•${NC} Full error analysis saved to reports"
echo -e "   ${YELLOW}•${NC} System logs backed up successfully"
echo -e "   ${YELLOW}•${NC} Historical data preserved"

echo -e "\n${GREEN} Analysis completed successfully! ${NC}"
echo -e "\n${BLUE} Reports Location:${NC} $LOG_DIR/"
echo -e "${YELLOW}Generated Reports:${NC}"
echo -e "   history_report.txt"
echo -e "   system_error_report.txt"
echo -e "   login_history.txt"
echo -e "   history.backup"
echo -e "   system_errors.backup"
