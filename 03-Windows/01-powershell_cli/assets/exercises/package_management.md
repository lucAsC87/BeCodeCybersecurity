# Powershell Package Management

It's time to start installing softwares and keep them updated. We will see how to use Chocolatey and how to use Windows Updates.

* Instructions

- Get Windows updates
    - Install the `PSWindowsUpdate` module
    - Type `Get-WindowsUpdate` to check for updates
    - Type `Install-WindowsUpdate` to install updates
    runAs :/user:Administrator powershell
    Install-Module -Name PSWindowsUpdate
- Manage Packages
    - Install `Chocolatey`
      Install-Module -Name Chocolatey
      Set-ExecutionPolicy Bypass -Scope Process -Force; `
     [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
     iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    - Install `VLC` from `Chocolatey`
      choco install vlc -y
    - Upgrade `VLC` to the latest version (it should already be but it's your first use)
      choco upgrade vlc -y
    - Remove the `VLC` package using `Chocolatey`
      choco uninstall vlc -y
    - Could you use `Chocolatey` on already installed software? How?
      yes, using choco install [PROGRAM] --force
- Manage Windows Features
    - Get installed windows features with the command `Get-WindowsFeature`
      Avalaible only on Windows Server
    - Install a new feature such as hyper-v with `Install-WindowsFeature`
      Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart

> **WARGNING**: This exercise **will only work on Windows** since it's specific to the way windows manages packages.
