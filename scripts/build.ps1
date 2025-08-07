$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest


Push-Location (Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent)
try {
    Write-Host "-- Build Logging package --"
    Start-Process -FilePath "powershell.exe" -ArgumentList (@("-File", ".\scripts\helpers\_build.ps1") + $args)
}
finally {
    Pop-Location
}