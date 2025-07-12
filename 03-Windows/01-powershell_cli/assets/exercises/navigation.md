# Powershell Navigation

Now we will learn how to move around in the filesystem with `Set-Location`, `Get-Location`, `Get-ChildItem` ...

- Print your current location on the screen
  Get-Location
- Print the content of your current directory
  Get-ChildItem
- Print the content of your root (`C:` _if you're running windows_, `/` _for linux_)
  Set Location / + Get-ChildItem
- Go into your home folder (_C:\Users\Username or /home/Username_)
  Set Location /home/lucasc87
- Print the content of your home
  Get-ChildItem
- Those commands are pretty long to type, do you know any shorter way to do it?
  pwd, ls, cd
