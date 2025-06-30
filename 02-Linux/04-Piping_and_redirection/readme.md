# Linux : Piping and Redirection

- Type of Challenge: `Learning` 
- Duration: `1/2 day`
- Aim - `Learning and application`
- Challenge type : `solo`

## Pipe

A pipe is a means of transmitting data from one process to another. It is one of the methods of inter-process communication ("Inter Process Communication": IPC).
A pipe has the following characteristics:
- The communication is unidirectional: we write at one end and read at the other (hence the name tube). This
implies that at least two descriptors are needed to manipulate a tube.
- The communication is done in FIFO (First In First Out) mode, first written, first read. Some primitives
like lseek(), or any other direct access to a data, have no sense for a tube.

What is read leaves the tube permanently and cannot be reread. In the same way, what is written is definitively written
written and cannot be removed.
- The transmission is done in continuous byte flow mode. The consecutive sending of the two sequences "abcd" and
efg" is similar to "abcdefg" and can be read as a whole or in pieces like "ab", "cde" and "fg" for example.
"fg" for example.
- To work, a tube must have at least one reader and one writer. There can be more than one.
- A tube has a finite capacity, and there is a producer/consumer type synchronization between readers and writers: a reader can sometimes and writers: a reader can sometimes wait for something to be written before reading, and a writer can wait for something to be can wait until there is space in the tube before writing.

Example
````sh
$ ls | grep "MyFile"
```` 
In this example, we send the result of the ls command to the grep command which will search for the word "MyFile" in this sequence of characters.

````sh
┌──(root💀Mitnick)-[/mnt/e/lab]
└─# ll
total 0
-rw-r--r-- 1 root root 0 May  2 20:24 Config.env
-rw-r--r-- 1 root root 0 May  2 20:23 Credentials
-rw-r--r-- 1 root root 0 May  2 20:23 MyFile
-rw-r--r-- 1 root root 0 May  2 20:23 Password

┌──(root💀Mitnick)-[/mnt/e/lab]
└─# ll | grep "MyFile"
-rw-r--r-- 1 root root 0 May  2 20:23 MyFile
````
## Redirection 

Redirects are a way to send data produced by a process to a file or to retrieve
data stored in a file to a process. The standard input, standard output and standard error output
as well as the files from which data is accessed or to which data is sent are all managed by file
by file descriptors. The descriptor duplication mechanism will therefore be the mechanism used to
implement redirections in Unix.

````
ls > test.txt
````

In this example, the result of the command is redirected to the file test.txt

````
┌──(root💀Mitnick)-[/mnt/e/lab]
└─# ls > test.txt

┌──(root💀Mitnick)-[/mnt/e/lab]
└─# cat test.txt
Config.env
Credentials
MyFile
Password
test.txt
````

## Exercises

Read the following [article](https://ryanstutorials.net/linuxtutorial/piping.php) and answer the questions below. Some questions will require additional research.

1. Write the message "hello everyone" in a file called "test" by redirecting the output of the echo command.
    > Your command : echo hello everyone > test
2. Write the message "goodbye" in the same file "test" by redirecting the output of the echo command and without overwriting the content of "test" and check with the cat command
    > Your command : echo goodbye >> test
3. Make the ``ls -la`` command redirect to the ``foo`` file
    > Your command : ls -la > foo
4. Execute ``find /etc -name *conf*`` command  and redirect errors (only errors) to a file named err.txt 
    > Your command : find /etc -name *conf* 2> err.txt
5. Repeat the previous exercise, this time redirecting the errors to the linux nothingness.
    > Your command : find /etc -name *conf* 2> /dev/null
6. Now redirect the standard output and the error output of the ``find /etc -name *conf*`` command to two different files (std.out and std.err)
    > Your command : find /etc -name *conf* 2> std.err 1> std.out
7. What does the mkfifo command do?
    > No answer required
8. Create a pipe named "MyNammedPipe". Then execute the pwd command which will transmit the data in this pipe. Then use the cat command to read the contents of your "MyNammedPipe" pipe.
    > Your commands : mkfifo MyNammedPipe - pwd > MyNammedPipe - cat MyNammedPipe (in nuovo terminale)
9. With cat command, add number the lines in the file /etc/passwd with the command ``nl``
    > Your commands : cat /etc/passwd | nl
10. Using the previous nl command, the head and tail commands, display the lines of /etc/passwd between line 7 and line 12
    > Your commands : cat /etc/passwd | nl | head -n 12 | tail -n 6
