# Monitoring 101

- Competence: `Team is able to gather information about the state of a linux machines`
- Type of Challenge: `Implementation`
- Duration: `5 days`
- Deadline: `24/06/2024`
- Type of chalenge : `Team`

## The Mission

One of the most important responsibilities a system administrator or SOC analyst have is monitoring the systems he manages. Indeed it's one thing to set them up and install software on them, but then what!? Well the next step is ensuring that the machines you provisioned as well as the services you deployed on them remain **available**, **reliable** and **secure**!
This challenge is divided in two tasks, the first one having you **research how to monitor** a Linux system as well as **what to look for** when doing so. You will have to **take note** of all your findings in a text file (EX: _markdown_) while being as **exhaustive** as possible (_what to monitor_, _how to monitor it_, _commands used_, _..._). Try to answer, but **don't limit yourself to**, the questions below to guide you through 
the research process:

- What are the main area of concern when monitoring a system? (EX: _CPU load_, _disk usage_, ...)
- How can you check what are the most memory intensive [running processes](https://www.computerhope.com/jargon/p/process.htm) ?
- What are log files? Where can you fin them on a typical Linux system ?
- How can you check who where the last connected users, what they did, when they left ?
- What are the different metrics of health and performance of a system ?
- How can you check the uptime of a machine ?
- How can you monitor the network traffic ?


> **IMPORTANT**: Take your time when researching, it's the most important part of this challenge as you'll need to be able to find out what is happening on any given system at any given time. Whether it's the percentage of system's resources currently used, what commands are being run, who is logged in, and so on...

Now create a Bash-based toolkit that helps monitor, detect, and report suspicious activity on a Linux system. The toolkit will simulate basic Host Intrusion Detection System (HIDS) capabilities using native tools and scripts.

## Complementary Resources

* [Useful monitoring commands](https://www.ubuntupit.com/most-comprehensive-list-of-linux-monitoring-tools-for-sysadmin/)
* [Linux system monitoring fundamentals](https://www.linode.com/docs/guides/linux-system-monitoring-fundamentals/)
* [Classic sysadmin viewing linux logs](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-viewing-linux-logs-from-the-command-line)
* [Security log management and logging best practice](https://www.techtarget.com/searchsecurity/tip/Security-log-management-and-logging-best-practices)
* [How to send email in linux from the command line](https://contabo.com/blog/how-to-send-email-in-linux-from-the-command-line/)
* [Cron Job: A Comprehensive Guide for Beginners](https://www.hostinger.com/tutorials/cron-job)

## Deliverables

1. A clearly articulated document for end-user to use the tool.
2. A team demo.

## Evaluation methods
- Quality of the documentation and the live demo 
- All things claimed to be implemented are working
- The team demonstrates good organisation and planning
- The team explains and justifies the various choices they made
- Tests were performed to ensure the configuration is working 
- The team demonstrate a solid knowledge of the Linux environment when answering questions during demo

## Final Words

There are plenty of tools out there but remember that collecting the metrics is only the first step towards an end goal, which is, to be able to keep track of the state of machines, troubleshoot them to understand errors and in the best cases prevent issues before they even happen!

One last thing, we cannot understate how **important**, even **crucial**, monitoring for servers, services and applications deployment.

<br>
<p align="center">
  <img src="https://c.tenor.com/FSFcij2DJkAAAAAC/watching-you-warning.gif" />
</p>

