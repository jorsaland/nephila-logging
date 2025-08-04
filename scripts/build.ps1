$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest


Write-Host "=== Nephila Logging ===`n"


.\env\Scripts\Activate.ps1
pip install . --force-reinstall