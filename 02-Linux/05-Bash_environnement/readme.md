# Bash environnement

- Type of Challenge: `Learning` 
- Duration: `1 day`
- Aim - `Learning and application`
- Challenge type : `solo`

> Connect to the virtual machine 10.12.0.xx with the following credentials:
> 
> * **ip** : 10.12.0.xx
> * **user** : Name
> * **password** : name

## Environment variables

Environment variables are a way to influence the behavior of software on your system. For example, the environment variable "LANG" determines the language that the software uses to communicate with the user.

Variables are made up of names that are assigned values. For example, a French user's system should have the value "fr_FR.UTF-8" assigned to the "LANG" variable.

The meaning of an environment variable and the type of value that can be assigned to it are determined by the application that uses it. There are a small number of well-known environment variables, whose meaning and type of value are well determined, and which are used by many applications.

To see the environment variables in bash, you can simply run the ``env`` command :

````bash
student@student:~$ env
XDG_SESSION_ID=85
TERM=xterm-256color
SHELL=/bin/bash
...
HOME=/home/student
LANGUAGE=en_US:en
LOGNAME=student
````
You can also use ``printenv`` command.


The value of the variable can also be retrieved by using the "$" sign in front of its name, as in the following example:

````sh
student@student:~$ echo $LANGUAGE
en_US:en
````

### Assigning a value to a variable

You can assign a value to a variable using the ``=`` operator. 

Example : 
````sh 
student@student:~$ MYVAR='MyValue'
````

But by creating a variable in this way, it will be available to you only. This means that it will not be available to all sub-processes active on the session. 

For example, let's create a MYNAME variable and assign it the value "Mitnick". 

````sh
MYNAME='Mitnick'
````

Although we have created a variable, it is not yet an environment variable, it is a shell variable.

This means that the scope of your variable remains local to your shell, and subprocesses will not be able to use your variable. Why? Because your variable is not part of your environment. In order for your variable to be accessible to sub-processes, we need to export your variable toyour environment.

To do this you must do it like this:

````sh
export MYNAME='Mitnick'
````

You can verify this statement, create a variable without ``export`` and echo the variable.

````sh
student@student:~$ TEST='test'
student@student:~$ echo $TEST
test
````
Well, now start a new sub-process by running a new bash.

````sh
student@student:~$ bash
````

Echo the ``$TEST`` variable again

````sh
student@student:~$ echo $TEST

student@student:~$ 
````

Repeat the operation, but this time export your variable.

````sh
student@student:~$ export TEST="test"
student@student:~$ echo $TEST
test
student@student:~$ bash
student@student:~$ echo $TEST
test
````
### Export or not ?

We have just seen the difference between variable definitions with and without export. But when to use export and when not to export?

We use environment variables (with export ) when we want to export the variables and make them available for the following commands or processes. Normally we use it to share the environment with a child process.

- Setting up the environment of the child process or shell
- Set a variable that a bash script run from the parent shell would use
- Setting environment variables for terminal multiplexers such as screen or tmux
- Setting up the build environment for build scripts and build tools

We use shell variables (without export ) when we want the variables to be available only in the parent shell and we don't want to pollute the child process environment:

- Loop counter variables
- Temporary variables

### Exercises 

1. On your student machine what is the value of the FLAG environment variable ?
> FLAG : No FLAG environment variable

2. Currently if you notice your machine, the variable you have created will be deleted. What should you do to make your variable persistent? (With a Bash shell).
> Commands : Just use export before declaring the variable (ex. export $FLAG="flag")


## History

In the terminal, have you ever tapped on the up or down arrows to return to a command you had previously used? 

![history](https://www.commitstrip.com/wp-content/uploads/2017/02/Strip-La-flemme-de-retaper-650-finalenglsih-1.gif)

Well, this is made possible by a file humbly named 'History'. This is located in your user file /home/user/. In the virtual machine, it is the file ``/home/student/.bash_history``

````sh
student@student:~$ ls -la
total 144
drwxr-xr-x 5 student student  4096 May  3 22:43 .
drwxr-xr-x 4 root    root     4096 May  1 17:39 ..
-rw------- 1 student student   863 May  2 08:30 .bash_history
-rw-r--r-- 1 student student   220 May  1 17:39 .bash_logout
-rw-r--r-- 1 student student  4003 May  3 22:43 .bashrc
drwx------ 2 student student  4096 May  1 17:40 .cache
-rw-r--r-- 1 root    root      209 May  1 23:12 employee.txt
drwxrwxr-x 2 student student  4096 May  1 21:25 findme
````

As you can see, the . in front of the file indicates that it is a hidden file.

> ⚠️ Depending on the shell used, the file name may change. You will often find it under .history 


````sh
student@student:~$ cat .bash_history 
sudo -l
dh
ls
cd /var
ls
cd /www
cd www
ls
cd html
ls
````

If we inspect the file, we can see all the history of our previously typed commands. There is also a command that displays the same thing: ``history``.
 
```sh
student@student:~$ history
    1  sudo -l
    2  dh
    3  ls
    4  cd /var
    5  ls
    6  cd /www
    7  cd www
    8  ls
```

When it is executed, history returns all the commands and their entry number (first column). We can use this number to re-run commands without having to type them again. For example, if you want to re-execute command number 42, you just have to enter :

````
student@student:~$ !42
````

The keyboard shortcut Ctrl+R allows you to enter the search mode in the history. The prompt looks like this:

```sh
(reverse-i-search):
```

You just have to enter the first characters of the command you want to search for so that the prompt offers you the most recent commands corresponding to your keystrokes, then Enter when you have found the right command.

> ⚠️ While this file can be useful for us users, it is also useful for hackers. Sometimes the history can 
> contain important information such as credentials that could help them escalate privileges.
>
> ⚠️ Also, when a machine has been compromised, it can be interesting for the analyst to check if the hacker has left some traces in the history.


### Exercises :

1. **From a hacker's perspective**, look for information that might be useful to you in the ``.history`` file. 
> Your answer: username and ip address for ssh connections; location of sensitive files (like the .ovpn one); git repos address; possible packets with vulnerabilities
2. **From an analyst's perspective**, look for information that might be useful to you in the ``.history`` file. 
> Your answer: look for suspicious commands used

## Custom aliases 
Linux users often need to use one command over and over again. Typing or copying the same command again and again reduces your productivity and distracts you from what you are actually doing.

You can save yourself some time by creating aliases for your most used commands. Aliases are like custom shortcuts used to represent a command (or set of commands) executed with or without custom options. Chances are you are already using aliases on your Linux system.

You can see a list of defined aliases on your profile by simply executing alias command.

````sh
student@student:~$ alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'

````

Here you can see the default aliases defined for your user in Ubuntu 16

Test it : 
````sh
student@student:~$ ll
total 148
drwxr-xr-x 5 student student  4096 May  3 23:36 ./
drwxr-xr-x 4 root    root     4096 May  1 17:39 ../
-rw------- 1 student student   863 May  2 08:30 .bash_history
-rw-r--r-- 1 student student   220 May  1 17:39 .bash_logout
-rw-r--r-- 1 student student  4003 May  3 22:43 .bashrc
drwx------ 2 student student  4096 May  1 17:40 .cache/
-rw-r--r-- 1 root    root      209 May  1 23:12 employee.txt
drwxrwxr-x 2 student student  4096 May  1 21:25 findme/
-rw-rw-r-- 1 student student  2330 May  3 23:40 .history
````

Is equivalent to running:

````sh
ls -alF
````

You can create an alias with a single character that will be equivalent to a command of your choice.

### How to Create Aliases in Linux

Creating aliases is relatively easy and quick process. You can create two types of aliases – temporary ones and permanent. We will review both types.

* **Creating Temporary Aliases** : What you need to do is type the word alias then use the name you wish to use to execute a command followed by "=" sign and quote the command you wish to alias.

    ````
    $ alias shortName="your custom command here"
    ````
* **To keep aliases between sessions**, you can save them in your user's shell configuration profile file. This can be:
    - Bash : ~/.bashrc
    - ZSH : ~/.zshrc
    - Fish : ~/.config/fish/config.fish

The syntax you should use is practically the same as creating a temporary alias. The only difference comes from the fact that you will be saving it in a file this time. So for example, in bash, you can open .bashrc file with your favorite editor like this:

````
nano ~/.bashrc
````

Find a place in the file, where you want to keep the aliases. For example, you can add them in the end of the file. For organizations purposes you can leave a comment before your aliases something like this:

````
#My custom aliases
alias home="ssh -i ~/.ssh/mykep.pem tecmint@192.168.0.100"
alias ll="ls -alF"
````

Save the file. The file will be automatically loaded in your next session. If you want to use the newly defined alias in the current session, issue the following command:

````
source ~/.bashrc
````

Well! Now it's time to optimize your workspace and create your own aliases!
