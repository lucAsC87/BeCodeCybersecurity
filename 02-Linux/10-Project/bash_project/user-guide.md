# User Guide: System Monitoring Demo Script  
_A Component of the HIDS Project_

---

## 1. Overview

`demo_script.sh` is an interactive, terminal-based tool that provides both **real-time** and **snapshot** views of your Linux system's performance. It helps monitor critical resources such as:

- CPU utilization  
- Disk I/O and usage  
- RAM and swap  
- Running processes  
- System load averages
- Network traffic
- Suspicious port activity
- System Logs
- User Logins

This script is designed as a core building block for a Host-based Intrusion Detection System (HIDS), allowing users to detect unusual system activity, resource bottlenecks, or other security-relevant anomalies.

---

## 2. Contributors

This project is a collaborative effort:

- [Harold Defree](https://github.com/GSGSDgggdzez)
- [Jérémie Loriaux](https://github.com/JeremieLoriaux)
- [Luca Cavallo](https://github.com/lucAsC87)
- [Daiane Roveda](https://github.com/DaianeR02)

---

## 3. System Requirements

- **Tested OS:** Kali Linux/Ubuntu  
- **Compatibility:** May work on other Debian-based distributions.

---

## 4. Getting Started

### 4.1 Clone the Repository

```bash
git clone https://github.com/GSGSDgggdzez/Cyber2
```
This will create a Cyber2 directory containing all project files.

### 4.2 Navigate to the Script Directory

```bash
cd Cyber2/demo/
```
### 4.3 Install Required Packages

Ensure the following packages are installed. While most are pre-installed on Linux Debian-based distributions, missing tools will trigger warnings during script execution.

| Package      | Purpose            | Install Command                 |
|--------------|--------------------|---------------------------------|
| `sysstat`    | `mpstat`, `iostat` | `sudo apt install sysstat -y`   |
| `psmisc`     | `pstree`           | `sudo apt install psmisc -y`    |
| `lsb-release`| `lsb_release`      | `sudo apt install lsb-release -y`|
| `pciutils`   | `lspci`            | `sudo apt install pciutils -y`  |
| `netcat`     | `nc`               | `sudo apt install netcat`       |
| `stress-ng`  | `stress-ng`        | `sudo apt install stress-ng`    |
| `iproute2`   | `ss`               | (usually pre-installed)         |
| `util-linux` | `lsblk`            | (usually pre-installed)         |
| `coreutils`  | `nproc`            | (usually pre-installed)         |
| `procps`     | `free`, `ps`       | (usually pre-installed)         |
| `wget`       | `wget`             | (usually pre-installed)         |

### 4.4 Make the Script Executable

```bash
chmod +x demo_script.sh
```
### 4.5 Run the Script

```bash
./demo_script.sh
```
This will launch the interactive menu interface.

## 5. Menu Navigation

- ↑ / ↓: Move between menu items

- Enter: Select highlighted option

- back: Return to the previous menu

- EXIT: Exit the program

- Press [Enter]: Used to stop real-time monitoring or return to menus

## 6. Main Menu Options

- System Info: Display OS and hardware specs

- IDS (Intrusion Detection System): Simulated threat response

- Hardware Management: Monitor CPU, Disk, RAM

- Process Management: Analyze processes and system load

- Network Management: Monitor suspicious ports and traffic

- User Management: View user-related logs and user logins

- EXIT: Close the program

## 7. Detailed Features
### 7.1 System Info

INFO

- Logged-in user

- Hostname

- OS and kernel version

- Uptime

- Shell and terminal type

SPECS

- CPU model and core count

- Architecture

- GPU

- Memory specs

- Disk details (names, sizes, models)

## 7.2 Hardware Management
#### 7.2.1 CPU Monitoring

Average CPU utilization

- Real-time overall CPU metrics:

- usr, nice, sys, iowait, irq, soft, steal, guest, gnice, idle

- Alerts shown for abnormal values

- Updates every 2 seconds

CPU core utilization

- Per-core breakdown of the above metrics

- Individual core alerts

- Updates every 2 seconds

- Press Enter to exit

#### 7.2.2 DISK Monitoring

Disk Usage

- Real-time stats: Size, Used, Available, Usage %

- Alerts when usage exceeds thresholds

Disk I/O Stats

- Read MB/s, Write MB/s, Util %

- High activity alerts

- Updates every second

- Press Enter to exit

#### 7.2.3 RAM Monitoring

Memory Stats
- Total, Used, Free RAM

- RAM usage (%) with alerts

Swap Usage

- Total, Used, Free

- Swap In/Out in KB/s

- Alerts for high swap usage or low physical RAM

- Press Enter to exit

## 7.3 Process Management

DEMANDING PROCESSES

- Real-time top consumers: Fields: PID, PPID, CMD, %MEM, %CPU

- Updates every second

- Press Enter to exit

PROCESS TREE

- Snapshot of parent-child process hierarchy (first 20 lines)

- Helps identify suspicious process spawns

- Press Enter to return

LOAD AVERAGE

- System load over 1, 5, and 15 minutes

- Includes explanations for interpretation

- Press Enter to return

## 7.4 Network Management 

TRAFFIC:

- Real-time display of network traffic per interface

- Uses tools like ifstat, nload, or parses /proc/net/dev

- Shows RX/TX bytes and speed (KB/s or MB/s)

- Helps detect unusual traffic spikes

- Updates every second

- Press Enter to exit

CHECK SUSPICIOUS PORT ACTIVITY

- Shows currently open ports and associated services

- Uses ss -tuln or netstat -tulnp to list TCP/UDP ports

- Helpful for identifying exposed services and potential vulnerabilities

- Static snapshot view

- Press Enter to return

## 7.5 User Management

LOGS
Displays:
- Monitors /var/log/auth.log and other log files for login and authentication attempts

- Looks for failed login patterns or sudo misuse

- Can be extended to parse .bash_history or /var/log/syslog

- Useful for detecting brute-force or suspicious user activity

- Press Enter to return

## 7.6 IDS (Intrusion Detection System)

ONE TIME: 

- Monitors all previously mentioned categories for alerts

- Outputs the found alerts to the terminal

- Press Enter to return

REAL TIME: 

- Continuously monitors all previously mentioned categories for alerts

- Outputs the currently active alerts to the terminal

- Press Enter to return

# 8. Logging

- A logs/ folder is created inside the project root

- Contains all_system_logs.log (contains all the alerts) and recent_system_logs.log (containes the most recent unique alerts)

- All scripts write to these files when they encounter an alert

- Main outputs typically output directly to the terminal

# 9. Demo Menu Breakdown

This document outlines the menu structure and functionality of the HIDS demo.

---

## Main Menu

* **System Info**
    * **INFO**: Basic system info
    * **SPECS**: Hardware specifications

* **IDS**: Placeholder for intrusion prevention
    * **ONE TIME**: monitors all categories once
    * **REAL TIME**: monitors all categories until stopped

* **Hardware Management**
    * **CPU**: average and per core CPU usage
    * **DISK**: Disk usage and I/O
    * **RAM**: Memory and swap usage

* **Process Management**
    * **DEMANDING PROCESSES**: Top CPU/memory processes
    * **PROCESS TREE**: Tree of running processes
    * **LOAD AVERAGE**: System load averages

* **Network Management**
    * **TRAFFIC**: Network traffic monitoring
    * **CHECK SUSPICIOUS PORT ACTIVITY**: Monitors suspicous port activity
* **User Management**
    * **LOGS**: View log activity and user logins

* **EXIT**

# 10. Troubleshooting

Problem	Solution

- Command not found	Check section 4.3 to install required packages

- Colors or layout look broken	Use a terminal that supports ANSI codes (e.g., GNOME Terminal, XFCE4 Terminal)

- Real-time views freeze	Ensure the terminal is responsive; press Enter again

- Unexpected behavior in unfinished features	Scripts under development (e.g., User or Network modules) may not behave consistently

---

# 11. Testing

To ensure that everything runs properly, you can use `test_script.sh`

### 11.1 Make the Script Executable
```bash
chmod +x test_script.sh
```
### 11.2 Run the Script
```bash
./test_script.sh
```
This will launch the test menu interface. From there, you can choose which test you want to run with Enter. Press ctrl+c to terminate the script. 

---

