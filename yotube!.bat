@echo off

REM Change this to the path of your PowerShell executable
set POWERSHELL="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

REM Change this to the path of your ascii-art-launcher.ps1 script
set PS_SCRIPT="Youtube.ps1"

%POWERSHELL% -NoExit -Command "& {Start-Process '%POWERSHELL%' -ArgumentList '-NoExit -File ""%PS_SCRIPT%""' -Verb RunAs}";
