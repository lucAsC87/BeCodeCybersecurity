# get_average_cpu_stats collects and displays average CPU usage statistics across all CPUs, formatting each metric and highlighting those that exceed predefined thresholds.
get_average_cpu_stats() {
    local print_statements=""

    # Check if 'mpstat' command is available (part of 'sysstat' package)
    if ! command -v mpstat &>/dev/null; then
        echo -e "${COLOR_ABOVE_THRESHOLD}mpstat not found. Please install the sysstat package.${COLOR_RESET}"
        return  # Exit function if mpstat is missing
    fi

    # Run mpstat to collect 1 sample over 1 second
    # Extract the line that starts with "Average:" and refers to all CPUs (the "all" row)
    local cpu_stats
    cpu_stats=$(mpstat 1 1 | awk '/^Average:/ && $2 == "all" {print}')

    # Read each field from the output into individual variables
    read -r _ _ usr nice sys iowait irq soft steal guest gnice idle <<<"$cpu_stats"

    # Calculate total CPU usage as 100 - idle
    total=$(awk -v idle="$idle" 'BEGIN { printf "%.2f", 100 - idle }')

    # Append formatted metric evaluations using thresholds and messages for each CPU stat
    print_statements+="${BOLD}$(print_metric "Total (%)" "$total" $DEFAULT_CPU_TOTAL_THRESHOLD "over" "CPU usage is high; may be overloaded" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "usr (%)" "$usr" $DEFAULT_CPU_USR_THRESHOLD "over" "Too much user-space processing" "CPU" "")\n"
    print_statements+="$(print_metric "nice (%)" "$nice" $DEFAULT_CPU_NICE_THRESHOLD "over" "Too many low-priority background jobs" "CPU" "")\n"
    print_statements+="$(print_metric "sys (%)" "$sys" $DEFAULT_CPU_SYS_THRESHOLD "over" "Excessive system/kernel activity" "CPU" "")\n"
    print_statements+="$(print_metric "iowait (%)" "$iowait" $DEFAULT_CPU_IOWAIT_THRESHOLD "over" "Waiting too long on disk or I/O" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "irq (%)" "$irq" $DEFAULT_CPU_IRQ_THRESHOLD "over" "Too many hardware interrupts" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "soft (%)" "$soft" $DEFAULT_CPU_SOFT_THRESHOLD "over" "Too many software interrupts" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "steal (%)" "$steal" $DEFAULT_CPU_STEAL_THRESHOLD "over" "Other VMs are stealing CPU time" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "guest (%)" "$guest" $DEFAULT_CPU_GUEST_THRESHOLD "over" "Unusual guest CPU usage" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "gnice (%)" "$gnice" $DEFAULT_CPU_GNICE_THRESHOLD "over" "Unusual guest nice usage" "CPU" "WARNING")\n"
    print_statements+="$(print_metric "idle (%)" "$idle" $DEFAULT_CPU_IDLE_THRESHOLD "under" "Low idle means CPU is heavily loaded" "CPU")\n"

    # Print all results with formatting and color (assumed handled in print_metric)
    echo -e "$print_statements"
}


# get_all_cpu_stats collects and displays CPU usage statistics for each individual CPU core using mpstat, formatting and highlighting metrics that exceed predefined thresholds.
get_all_cpu_stats() {
    # Check if the 'mpstat' command is available
    if ! command -v mpstat &>/dev/null; then
        echo -e "${COLOR_ABOVE_THRESHOLD}mpstat not found. Please install the sysstat package.${COLOR_RESET}"
        return  # Exit early if 'mpstat' is not installed
    fi

    local print_statements=""

    # Collect CPU stats for all cores (excluding the 'all' and header rows)
    # The loop reads one line at a time and parses it into variables
    while IFS= read -r line; do
        # Parse values from mpstat output into named variables
        read -r cpu_id usr nice sys iowait irq soft steal guest gnice idle <<<"$line"

        # Calculate total CPU usage for this core
        total=$(awk -v i="$idle" 'BEGIN { printf "%.2f", 100 - i }')

        # Start assembling the output for this CPU core
        print_statements+="${BOLD}Core $cpu_id:\n"

        # Append metrics with alerting and formatting via print_metric
        print_statements+="${BOLD}$(print_metric "Total (%)" "$total" $DEFAULT_CPU_TOTAL_THRESHOLD "over" "High usage on Core $cpu_id" "CPU" "WARNING")  "
        print_statements+="$(print_metric "usr (%)" "$usr" $DEFAULT_CPU_USR_THRESHOLD "over" "High usr on Core $cpu_id" "CPU")  "
        print_statements+="$(print_metric "nice (%)" "$nice" $DEFAULT_CPU_NICE_THRESHOLD "over" "High nice on Core $cpu_id" "CPU")  "
        print_statements+="$(print_metric "sys (%)" "$sys" $DEFAULT_CPU_SYS_THRESHOLD "over" "High sys on Core $cpu_id" "CPU")  "
        print_statements+="$(print_metric "iowait (%)" "$iowait" $DEFAULT_CPU_IOWAIT_THRESHOLD "over" "High iowait on Core $cpu_id" "CPU" "WARNING")  "
        print_statements+="$(print_metric "irq (%)" "$irq" $DEFAULT_CPU_IRQ_THRESHOLD "over" "High irq on Core $cpu_id" "CPU" "WARNING")  "
        print_statements+="$(print_metric "soft (%)" "$soft" $DEFAULT_CPU_SOFT_THRESHOLD "over" "High soft on Core $cpu_id" "CPU" "WARNING")  "
        print_statements+="$(print_metric "steal (%)" "$steal" $DEFAULT_CPU_STEAL_THRESHOLD "over" "High steal on Core $cpu_id" "CPU" "WARNING")  "
        print_statements+="$(print_metric "guest (%)" "$guest" $DEFAULT_CPU_GUEST_THRESHOLD "over" "Unusual guest usage" "CPU" "WARNING")  "
        print_statements+="$(print_metric "gnice (%)" "$gnice" $DEFAULT_CPU_GNICE_THRESHOLD "over" "Unusual gnice usage" "CPU" "WARNING")  "
        print_statements+="$(print_metric "idle (%)" "$idle" $DEFAULT_CPU_IDLE_THRESHOLD "under" "Low idle on Core $cpu_id" "CPU")\n"

    # Use process substitution to feed mpstat output directly to the while loop
    done < <(
        mpstat -P ALL 1 1 | awk '/^Average:/ && $2 != "all" && $2 != "CPU" {
            print $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12
        }'
    )

    # Display the collected and formatted output
    echo -e "$print_statements"
}
