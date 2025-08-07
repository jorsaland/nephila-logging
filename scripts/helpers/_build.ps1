$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest


try {

    Write-Host "=== Nephila Logging ===`n"

    .\env\Scripts\Activate.ps1
    pip install . --force-reinstall
    python setup.py sdist

}


finally {

    if ($args -contains "debug") {
        Read-Host "`n=== ENTER to exit ==="
    }

}