# Powershell Permissions

Now that we can navigate and create files, we should be able to change permissions on these. We will use the commands `Get-Acl`, `Set-Acl`, `RunAs`

- Create a file
  New-Item test.txt
- Check the owner and the groups
  Get-Acl test.txt
- Change the file owner to the built-in administrator (administrator account is disabled by default, check how to enable it. Don't forget to set a strong password!)
  Start-Process powershell -Verb runAs
  $File = C:\Users\vboxusers\test.txt
  $AdminUser = "Administrator"
  $Acl = Get-Acl $File
  $Acl.SetOwner([System.Security.Principal.NTAccount]$AdminUser)
  Set-Acl $File $Acl
- Check the file's permission
- Try to print the content of the file as your normal user
- Print the content of the file using administrator account
  Get-Acl test.txt | Format-List

> **WARNING**: This exercise **will only work on Windows** system since file system permissions are not managed the same way on Windows and Linux.
