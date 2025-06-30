# show_process_tree displays a detailed ASCII process tree for the user "age" if the 'pstree' command is available, or prints an installation warning if not.
show_process_tree() {
    # Check if 'pstree' is available
    if command -v pstree &>/dev/null; then
        # Show a detailed process tree with ASCII lines (-A), command names (-C), and full command lines (-l)
        pstree -lAC age
    else
        # Warn user if 'pstree' is missing
        echo "pstree not found. Please install the psmisc package."
    fi
    echo  # Add a blank line for spacing
}


# show_load extracts and displays the system's 1, 5, and 15-minute load averages, highlighting values that exceed a predefined threshold.
show_load() {
    print_statements=""

    # Extract load averages using 'uptime'
    # Format: "load average: 1.23, 0.87, 0.65"
    load_vals=$(uptime | awk -F 'load average: ' '{ print $2 }' | sed 's/^ *//')

    # Split values into 1-minute, 5-minute, and 15-minute load averages
    IFS=', ' read -r load1 load5 load15 <<< "$load_vals"

    # Print each load value with threshold comparison
    print_statements+="$(print_metric "1min : " "$load1" "$DEFAULT_LOAD_AVERAGE" "over" "Load average is too high" "PROCESS")\n"
    print_statements+="$(print_metric "5min : " "$load5" "$DEFAULT_LOAD_AVERAGE" "over" "Load average is too high" "PROCESS")\n"
    print_statements+="$(print_metric "15min: " "$load15" "$DEFAULT_LOAD_AVERAGE" "over" "Load average is too high" "PROCESS")\n"

    # Output the formatted load data
    echo -e "$print_statements"
}


# get_top_processes_cpu prints a formatted report of the top 20 CPU-consuming processes, highlighting those exceeding a defined CPU usage threshold.
get_top_processes_cpu() {
    process_tree_cpu=""

    # Get top 20 processes sorted by %CPU usage
    while IFS= read -r line; do
        read -r user pid cpu path <<<"$line"

        # Normalize CPU usage relative to the default load threshold
        normalized_cpu=$(awk -v c="$cpu" -v d="$DEFAULT_LOAD_AVERAGE" 'BEGIN { printf "%.2f", c / d }')

        # Append formatted metric with warning if needed
        process_tree_cpu+="$(print_metric "${user} (%)" "$normalized_cpu" $DEFAULT_PROCESS_CPU_THRESHOLD "over" "Process ${path} is using a lot of compute power" "PROCESS" "WARNING")  PID: $pid  $path\n"
    
    # Use 'ps' to fetch the top 20 CPU-consuming processes, skipping the header
    done < <(ps aux --sort=-%cpu | grep -v "[p]s aux" | head -16 | tail -15 | awk '{
        cmd=""; 
        for(i=11;i<=NF;i++) cmd=cmd $i (i==NF ? "" : " ");
        printf "%s %s %s %s\n", $1, $2, $3, $11
    }')

    # Print the CPU-intensive process report
    echo -e "$process_tree_cpu"
}


# get_top_processes_mem prints a formatted report of the top 20 memory-consuming processes, highlighting those exceeding a memory usage threshold.
get_top_processes_mem(){
    process_tree_mem=""

    # Get top 20 processes sorted by %MEM usage
    while IFS= read -r line; do
        read -r user pid mem path <<<"$line"

        # Append memory usage with formatting and warning if above threshold
        process_tree_mem+="$(print_metric "${user} (%)" "$mem" $DEFAULT_PROCESS_MEM_THRESHOLD "over" "Process ${path} is using a lot of memory" "PROCESS" ""WARNING)  PID: $pid  $path\n"
    
    # Use 'ps' to fetch the top 20 memory-consuming processes, skipping the header
    done < <(ps aux --sort=-%mem | grep -v "[p]s aux" | head -16 | tail -15 | awk '{
        cmd="";
        for(i=11;i<=NF;i++) cmd=cmd $i (i==NF ? "" : " ");
        printf "%s %s %s %s\n", $1, $2, $4, $11
    }')

    # Print the memory-intensive process report
    echo -e "$process_tree_mem"
}