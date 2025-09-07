# Phishing Analysis

- Type of Challenge: Learning
- Challenge type : solo


## Your Mission
As a consultant, you have to analyze the 5 emails that your colleagues send you. You must determine which email appears to be phishing and write a report. Your report should include all your thoughts and print screens of all the tools you used 

### Phishing Fundamentals

First of all please do these two rooms of tryhackme :
- https://tryhackme.com/room/phishingemails1tryoe
- https://tryhackme.com/room/phishingemails2rytmuv


### Phishing Case
Your colleagues have provided you with emails in .eml format, ".eml" files are individual email files stored in Multipurpose Internet Mail Extensions (MIME) format. To scan .eml emails, you can use tools such as email clients (Outlook, Thunderbird, etc.), email viewing applications, or specialized tools such as email scanners.

Here are some general steps you can take to scan an .eml file:

- Open the .eml file in an email client or email viewing application. You can also open the .eml file with a text editor to see the source code of the email.
- Check the email headers to identify the sender, recipient, date and subject information. You may also find additional information, such as the mail servers involved in the transmission of the message.
- Check the content of the email for signs of phishing, such as suspicious links or requests for sensitive data.
- Check attachments for malicious files, such as macros or scripts.
- Use email analysis tools to extract additional information from the email, such as IP addresses of email servers or additional headers.

**In your report, you must at least answer all the questions in the list below :**

- What is the email's timestamp? 
- Who is the email from?
- What is his email address?
- What email address will receive a reply to this email? 
- What brand was this email tailored to impersonate?
- What is the originating IP? Defang the IP address. 
- What do you think will be a domain of interest? Defang the domain.
- What is the shortened URL? Defang the URL.
- Do you think this is a phishing email?

### Tools 
#### [VirusTotal](https://www.virustotal.com/gui/home/upload)

VirusTotal was founded in 2004 as a free service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. Our goal is to make the internet a safer place through collaboration between members of the antivirus industry, researchers and end users of all kinds. Fortune 500 companies, governments and leading security companies are all part of the VirusTotal community, which has grown to over 500,000 registered users.

#### [PhishTools](https://www.phishtool.com/)  
Be you a security researcher investigating a new phish-kit, a SOC analyst responding to user reported phishing, a threat intelligence analyst collecting phishing IoCs or an investigator dealing with email-born fraud.

PhishTool combines threat intelligence, OSINT, email metadata and battle tested auto-analysis pathways into one powerful phishing response platform. Making you and your organisation a formidable adversary - immune to phishing campaigns that those with lesser email security capabilities fall victim to.

#### [MX Lookup](https://mxtoolbox.com/)
This test will list MX records for a domain in priority order. The MX lookup is done directly against the domain's authoritative name server, so changes to MX Records should show up instantly. You can click Diagnostics , which will connect to the mail server, verify reverse DNS records, perform a simple Open Relay check and measure response time performance. You may also check each MX record (IP Address) against 105 DNS based blacklists 

#### [PhishTank](https://phishtank.com/?)
PhishTank is a collaborative clearing house for data and information about phishing on the Internet. Also, PhishTank provides an open API for developers and researchers to integrate anti-phishing data into their applications at no charge.

#### [Spamhaus](https://www.spamhaus.org/)
Spamhaus is the world leader in supplying realtime highly accurate threat intelligence to the Internet's major networks.

#### [Phishing incident response](https://www.incidentresponse.org/playbooks/phishing)  
The phishing incident response playbook contains all 7 steps defined by the NIST incident response process: Prepare, Detect, Analyze, Contain, Eradicate, Recover, Post-Incident Handling.
