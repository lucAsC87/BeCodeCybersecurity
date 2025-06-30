# monitor_all runs a sequence of system and network monitoring functions, discarding their outputs.
monitor_all(){
    show_traffic "$IFACE" >/dev/null
    check_suspicious >/dev/null
    get_average_cpu_stats >/dev/null
    get_disk_io_stats >/dev/null
    get_memory_stats >/dev/null
    get_swap_stats >/dev/null
    get_top_processes_cpu >/dev/null
    get_top_processes_mem >/dev/null
    show_load >/dev/null
}