# Exercise Powershell CLI - Trial of might

Now that you gathered some basic understanding of the Powershell CLI, here is an exercise to test your might! It's been put together by the guys at [UnderTheWire](https://underthewire.tech/) (_very similar to OverTheWire_). You will have to tackle a series of exercise called Century that is aimed at testing the fundamentals of Powershell know-hows.

- Go to the webpage of the [Century game](https://underthewire.tech/century) and follow the instructions there
- **complete a maximum amount of levels** and **take note of the passwords** for each one of them
- First level:  ```century1@century.underthewire.tech``` 
- Password: ```century1```
- Encrypt the collected passwords with [GPG](https://medium.com/meetcyber/gpg-encryption-a-comprehensive-guide-to-securing-data-transfers-b66e784d7889), upload them on Github (link to be provided later) with a minimalist readme and send me your public key. 

1 - century1
2 - $PSVersionTable --> 10.0.14393.7870
3 - invoke-webrequest443
4 - (Get-ChildItem -File).Count --> 123
5 - 15768
6 - $env:userdomain --> underthewire3347
7 - (Get-ChildItem | ? { $_.PSIsContainer }).Count --> 197
8 - Get-ChildItem -File -Recurse / Get-Content .\Readme.txt --> 7points
9 - (Get-Content .\unique.txt | Select-Object -Unique).Count --> 696
10 - (Get-Content .\Word_File.txt) -split "\s+" | Select-Object -Index 160 --> pierid
11 - ((Get-WmiObject -Class Win32_Service -Filter "Name='wuauserv'").Description -split "\s+")[9,7] --> windowsupdates110
12 - Get-ChildItem -File -Recurse -Force | Where-Object { $_.Attributes -match "Hidden" } - secret_sauce
13 - Get-ADDomainController -Filter *i_authenticate_things / Get-ADComputer UTW -Properties Description | Select-Object Name, Description --> i_authenticate_things
14 - ((Get-Content .\countmywords) -split "\s+").Count --> 755
15 - ((Get-Content .\countpolos) -split "\s+" | Where-Object { $_ -eq "polo" }).Count - 153


