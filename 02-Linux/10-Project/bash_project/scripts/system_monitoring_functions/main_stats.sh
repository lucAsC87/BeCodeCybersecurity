# Function to get real-time system stats for display
get_realtime_stats() {
    # Get CPU usage
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | sed 's/%us,//' | sed 's/,//' || echo "N/A")
    
    # Get memory usage
    local mem_info=$(free | grep Mem)
    local mem_total=$(echo $mem_info | awk '{print $2}')
    local mem_used=$(echo $mem_info | awk '{print $3}')
    local mem_percent=$(echo "scale=1; $mem_used * 100 / $mem_total" | bc 2>/dev/null || echo "N/A")
    
    # Get swap usage
    local swap_info=$(free | grep Swap)
    local swap_total=$(echo $swap_info | awk '{print $2}')
    local swap_used=$(echo $swap_info | awk '{print $3}')
    local swap_percent="0"
    if [[ $swap_total -gt 0 ]]; then
        swap_percent=$(echo "scale=1; $swap_used * 100 / $swap_total" | bc 2>/dev/null || echo "0")
    fi
    
    # Get disk usage for root partition
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "CPU: ${cpu_usage}% | RAM: ${mem_percent}% | SWAP: ${swap_percent}% | DISK: ${disk_usage}%"
}
