# Processes

- Type of Challenge: `Learning` 
- Duration: `1 day`
- Aim - `Learning and application`
- Challenge type : `solo`


## Program VS Process
A process is a program that executes and that also has its ordinal counter, its registers and its variables; this is the subtlety between program and process. The difference between a process and a program is thin: the process has the program but also the current state of this one in the memory of the computer. The program is ultimately the set of files that, when executed, become the process.

## What is a PID ?
A PID (that is, a process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system. A process is a running (i.e., executing) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

[What is PID? in Linux?](https://www.scaler.com/topics/what-is-pid-in-linux/)

## Commands

### ps
the "ps" command allows you to display the active processes and resources used at a time t, by user, by PID .

````sh
student@student:~$ ps
  PID TTY          TIME CMD
14711 pts/0    00:00:00 bash
14730 pts/0    00:00:00 ps
````

The "-x" option allows you to view all active processes of the current user
````sh
student@student:~$ ps -x
  PID TTY      STAT   TIME COMMAND
14621 ?        Ss     0:00 /lib/systemd/systemd --user
14622 ?        S      0:00 (sd-pam)
14710 ?        S      0:00 sshd: student@pts/0
14711 pts/0    Ss     0:00 -bash
14738 pts/0    R+     0:00 ps -x

````

The "-ax" option allows to display all the processes of the machine of all the users
````sh
student@student:~$ ps -ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:02 /sbin/init
    2 ?        S      0:00 [kthreadd]
    3 ?        S      0:00 [ksoftirqd/0]
    5 ?        S<     0:00 [kworker/0:0H]
    7 ?        S      0:00 [rcu_sched]
    8 ?        S      0:00 [rcu_bh]
    9 ?        S      0:00 [migration/0]
   10 ?        S      0:00 [watchdog/0]
   11 ?        S      0:00 [kdevtmpfs]
   12 ?        S<     0:00 [netns]
   13 ?        S<     0:00 [perf]
   14 ?        S      0:00 [khungtaskd]
   .           .
   .           .
   .           .
14619 ?        Ss     0:00 sshd: student [priv]
14621 ?        Ss     0:00 /lib/systemd/systemd --user
14622 ?        S      0:00 (sd-pam)
14624 ?        S      0:00 [kworker/0:1]
14710 ?        S      0:00 sshd: student@pts/0
14711 pts/0    Ss     0:00 -bash
14739 pts/0    R+     0:00 ps -ax

````

The "-aux" option allows to display the users associated to each process
````sh
student@student:~$ ps -aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3  38128  6112 ?        Ss   May03   0:02 /sbin/init
root         2  0.0  0.0      0     0 ?        S    May03   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    May03   0:00 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S<   May03   0:00 [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    May03   0:00 [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    May03   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    May03   0:00 [migration/0]
root        10  0.0  0.0      0     0 ?        S    May03   0:00 [watchdog/0]
root        11  0.0  0.0      0     0 ?        S    May03   0:00 [kdevtmpfs]
root        12  0.0  0.0      0     0 ?        S<   May03   0:00 [netns]
root        13  0.0  0.0      0     0 ?        S<   May03   0:00 [perf]
root        14  0.0  0.0      0     0 ?        S    May03   0:00 [khungtaskd]
root        15  0.0  0.0      0     0 ?        S<   May03   0:00 [writeback]
root        16  0.0  0.0      0     0 ?        SN   May03   0:00 [ksmd]
.           .   .     .       .     .           .       .        .
root     14573  0.0  0.0      0     0 ?        S    23:06   0:00 [kworker/u2:1]
root     14619  0.0  0.4  92832  6656 ?        Ss   23:14   0:00 sshd: student [priv]
student  14621  0.0  0.3  45316  4760 ?        Ss   23:14   0:00 /lib/systemd/systemd --user
student  14622  0.0  0.1  61580  2228 ?        S    23:14   0:00 (sd-pam)
student  14710  0.0  0.2  92832  3356 ?        S    23:14   0:00 sshd: student@pts/0
student  14711  0.0  0.3  21288  5120 pts/0    Ss   23:14   0:00 -bash
root     14740  0.0  0.0      0     0 ?        R    23:18   0:00 [kworker/u2:2]
student  14742  0.0  0.2  36080  3312 pts/0    R+   23:19   0:00 ps -aux

```` 

The "-u username" option displays every process associated with user

````sh
student@student:~$ ps -u student
  PID TTY          TIME CMD
14621 ?        00:00:00 systemd
14622 ?        00:00:00 (sd-pam)
14710 ?        00:00:00 sshd
14711 pts/0    00:00:00 bash
14744 pts/0    00:00:00 ps
````

### kill

The "kill" command can be used to kill any command, including commands running in the background. The "kill" command, more precisely, sends a signal to the designated processes. The default action for a process is to die on receiving certain signals. To send a signal to a process you must be the owner of the process; "kill" cannot be used to kill another user's process unless you are the super user (the "root" user).

````
student@student:~$ kill 14711 
````

### wait 

The "wait" command allows you to suspend the execution of a shell script until the process, whose PID is specified as an argument, finishes. If no PID is specified, in this case we will wait until all processes launched in the background have finished. 

````sh
student@student:~$ cat /usr/man1/* > file &
student@student:~$ find / -print > file2 &
student@student:~$ wait
student@student:~$ echo "cat and find are finished ..."
````

### bg and & 
Each operating system may handle processes differently, but in the case of Linux, processes are usually associated with a terminal. This means that it must be open for the process to run normally, but this action can lead to situations such as:

- The open terminal may contain a lot of output data or error/diagnostic messages, which makes it difficult not only to read the data, but also to manage it.
- If we were to close the terminal, the process and its sub-processes would end up directly affecting the task at hand.

In this type of scenario, it is essential to run the necessary processes in the background. A background process is the process that will be executed in a hidden way. For its operation, the user's intervention is not necessary. Thus, the terminal is closed. The main process will continue to execute its task. Background processes apply to tasks that may take time, such as scripts, downloaded files, etc., for which we can not wait for the action to be completed without doing anything.If the goal is to completely separate a process from the terminal, we must use the following syntax: 

````
app /dev/null & 
````

you can use the sleep command to test. This command will pause for 10 seconds which will block the shell

````
student@student:~$ sleep 10
````

Now test the following command: 
````
student@student:~$ sleep 10 &
````

### jobs
Finding jobs that are running or suspended in background
Type the following jobs command:
````
jobs -l
````
The output of the jobs -l command shows the following job running in the background:
````
[4]+  6138 Stopped                 ping becode.org
````

Type the following commands:
````
sleep 20 &
````
Then :
````
jobs -l
````

### fg
The fg command, short for the foreground, is a command that moves a background process on your current Linux shell to the foreground. This contrasts the bg command, short for background, that sends a process running in the foreground to the background in the current shell.

Before you start using fg command, you need to start couple of jobs on your system for demonstration purpose. Type the following commands to start jobs:

````
student@student:~$ program1 &
````
Type enter and then : 

````
student@student:~$ program2 &
````

Create a file :
````
nano test
````
Close it.

look for the id of the job.
````
student@student:/$ jobs -l
[4]- 15837 Running                 program1 &
[5]+ 15838 Running                 program2 &
````
and return to one of the previous jobs.
````
fg 4
````


### Exercises :

1. List all running processes in Linux.
> Your answer : ps aux

2. How do you find the PID of a process by its name?
> Your answer : pgrep + PROCESS' NAME

3. Terminate a process with a specific PID.
> Your answer : kill + PID

4. Change the priority of a running process.
> Your answer : fg + PROCESS' NUMBER

5. How can you continuously monitor the resource usage of a specific process?
> Your answer : top -p + PID
