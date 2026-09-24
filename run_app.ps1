Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host " STARTING PRIVACY ENGINEERING & TECHNICAL GRC PORTFOLIO WEB APP" -ForegroundColor Green
Write-Host " Empirical Live Audit | RoPA | DPIA | Vendor DPA | Privacy Policy" -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Cyan
Write-Host ""
Set-Location "C:\Users\acer\Privacy_Engineering_Master_Portfolio"
Write-Host "Launching Streamlit server on http://localhost:8501 ..." -ForegroundColor Yellow
python -m streamlit run app.py
