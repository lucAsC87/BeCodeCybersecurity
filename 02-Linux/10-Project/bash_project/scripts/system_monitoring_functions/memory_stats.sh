# get_memory_stats collects and displays system RAM usage statistics, including total, used, free memory, and usage percentage, with threshold-based warnings for low free memory or high usage.
get_memory_stats() {
    # Ensure the 'free' command is available
    if ! command -v free &>/dev/null; then
        echo -e "${COLOR_ABOVE_THRESHOLD}free not found. Please install procps or equivalent.${COLOR_RESET}"
        return
    fi

    local print_statements=""

    # Extract memory stats in MB using 'free -m'
    # Fields: total, used, free, shared, buff/cache, available
    read -r _ total used free shared buff_cache available <<< \
        $(free -m | awk '/^Mem:/ {print $1, $2, $3, $4, $5, $6}')

    # Calculate RAM usage percentage
    local mem_usage_pct=$(awk -v u=$used -v t=$total 'BEGIN { printf "%.2f", (u / t) * 100 }')

    # Format and append memory statistics using print_metric (with or without thresholds)
    print_statements+="$(print_metric "Total RAM (MB)" "$total" 0 "none" "")\n"
    print_statements+="$(print_metric "Used RAM (MB)" "$used" 0 "none" "")\n"
    print_statements+="$(print_metric "Free RAM (MB)" "$free" $DEFAULT_MEM_LIMIT "under" "Low free memory; consider closing apps" "RAM" "")\n"
    print_statements+="$(print_metric "RAM Usage (%)" "$mem_usage_pct" $DEFAULT_MEM_THRESHOLD "over" "High RAM usage" "RAM" "WARNING")\n"

    # Output all collected RAM stats
    echo -e "$print_statements"
}


# get_swap_stats collects and displays formatted system swap usage statistics, including total, used, and free swap, swap usage percentage, and swap-in/out rates, with threshold-based warnings.
get_swap_stats(){
    # Ensure the 'free' command is available
    if ! command -v free &>/dev/null; then
        echo -e "${COLOR_ABOVE_THRESHOLD}free not found. Please install procps or equivalent.${COLOR_RESET}"
        return
    fi

    local print_statements=""

    # Extract swap stats in MB: total, used, and free
    read -r _ swap_total swap_used swap_free <<< \
        $(free -m | awk '/^Swap:/ {print $1, $2, $3, $4}')

    # Get swap-in (si) and swap-out (so) values in KB/s using vmstat (2 samples, 1s interval)
    read -r si so <<< $(vmstat 1 2 | tail -1 | awk '{print $7, $8}')

    # Calculate swap usage percentage, handling division-by-zero
    local swap_usage_pct=$(awk -v u=$swap_used -v t=$swap_total 'BEGIN { if (t==0) print 0; else printf "%.2f", (u / t) * 100 }')

    # Format and append swap-related metrics using print_metric
    print_statements+="$(print_metric "Total Swap (MB)" "$swap_total" 0 "none" "")\n"
    print_statements+="$(print_metric "Used Swap (MB)" "$swap_used" 0 "none" "")\n"
    print_statements+="$(print_metric "Free Swap (MB)" "$swap_free" $DEFAULT_SWAP_FREE "none" "Low swap space left" "SWAP")\n"
    print_statements+="$(print_metric "Swap Usage (%)" "$swap_usage_pct" $DEFAULT_SWAP_PCT "over" "High swap usage; system may be swapping" "SWAP" "WARNING")\n"
    print_statements+="$(print_metric "Swap In (KB/s)" "$si" $DEFAULT_SWAP_SI_THRESHOLD "over" "System is reading from swap — RAM pressure" "SWAP" "WARNING")\n"
    print_statements+="$(print_metric "Swap Out (KB/s)" "$so" $DEFAULT_SWAP_SO_THRESHOLD "over" "System is writing to swap — RAM may be full" "SWAP" "WARNING")\n"

    # Display the full formatted output
    echo -e "$print_statements"
}