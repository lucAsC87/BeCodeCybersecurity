# Powershell Environment Variables

In any programming language you can store data within variables. However they only exist as long as the program is executed, but what if you wanted to share information between two applications not running at the same time.

Then you could use environment variables, which are variables stored at the OS level. You can access them from anywhere.

- Open a Powershell Terminal
- Type `echo $env:computername`. It should show your computer name
- Create a variable by typing `$env:test = "hello powershell"`
- Check the variable you just created the same way you did with the computer name
- Now we will add something to this variable by typing `$env:test += " Becode"`
- Check the variable
- There is one really important environment variable : `$env:path`. This variable store the location where windows looks for files that are not in your current folder. For example, if you call VSCode from the powershell terminal, it opens it even if the executable isn't present in the current folder. That's because the path to the vscode's executable is stored in `$env:path`. Now download an executable software ([rufus](https://github.com/pbatard/rufus/releases/download/v3.13/rufus-3.13p.exe) for example) and copy it on your desktop. If you try from a command line to launch it, it will fail with a command not found (if you are not in the same folder).
- Try to happen the $env:path to add the path to rufus' executable (It should be something like this if you copied it on your desktop : `C:\Users\Username\Desktop`)  
  $env:path += "C:\Users\vboxuser\Desktop"
- Try to call rufus from anywhere
- I would like you to have a look at [the recognized environment variables available on windows](https://docs.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables).
- Write a small script reporting your computer specs and convert it in a csv file. You might have some trouble executing your script once saved. Why? How can you change it in a secure way?  
   $sys_array = "computername", "number_of_processors", "os", "processor_architecture", "username"; foreach ($var in $sys_array) { echo "$var,$($env[$var])" } | Out-File "sys-spec.csv"
   It cannot be executed due to the Windows Execution Policy, a security feature that prevents the execution of unhautorized   scripts. By default it's set on Restricted.
  With the command Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned it's possible to allow the execution of all the locally created script just for the current user and demands an attendible author for the ones downloaded from the Internet. Otherwise, Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass make the script executable only for the current powershell session.
  
> **WARNING**: This exercise will **only work on windows** since it's specific to the way windows manages environment variables.
