# Clean reset of the experiment
Write-Host "Starting Clean Reset of Privacy Engineering Audit" -ForegroundColor Cyan

# 1. Archive legacy artifacts
Write-Host "Archiving legacy artifacts..."
if (Test-Path "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-EU-001") {
    Move-Item "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-EU-001" "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-EU-001-ARCHIVED-LEGACY" -Force
}
if (Test-Path "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-IN-001") {
    Move-Item "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-IN-001" "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-IN-001-ARCHIVED-LEGACY" -Force
}

# Ensure clean directories
New-Item -ItemType Directory -Force -Path "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-EU-001" | Out-Null
New-Item -ItemType Directory -Force -Path "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\runs\MIRO-IN-001" | Out-Null

Write-Host "Legacy artifacts archived. Ready for fresh capture."
Write-Host ""
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host "IMPORTANT: You must run the following commands manually with" -ForegroundColor Yellow
Write-Host "a REAL EU VPN active on your machine." -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Turn on your EU VPN (e.g., France)."
Write-Host "2. Run EU Captures:"
Write-Host "   python capture_miro.py --profile eu-france --action baseline --proxy direct"
Write-Host "   python capture_miro.py --profile eu-france --action accept --proxy direct"
Write-Host "   python capture_miro.py --profile eu-france --action reject --proxy direct"
Write-Host ""
Write-Host "3. Turn off your VPN (revert to India)."
Write-Host "4. Run India Captures:"
Write-Host "   python capture_miro.py --profile india --action baseline"
Write-Host "   python capture_miro.py --profile india --action accept"
Write-Host "   python capture_miro.py --profile india --action reject"
Write-Host ""
Write-Host "5. Regenerate Manifest and JSON:"
Write-Host "   python consolidate_evidence.py (Make sure to write this script to update hashes)"
