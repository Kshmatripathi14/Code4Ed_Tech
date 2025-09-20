# PowerShell script to setup & run project
if (-Not (Test-Path "./venv")) { python -m venv venv }
& .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install fastapi uvicorn sqlmodel pdfplumber python-docx spacy sentence-transformers streamlit
python -m spacy download en_core_web_sm
Start-Process powershell -ArgumentList "uvicorn backend.main:app --reload --port 8000"
streamlit run .\frontend\app_streamlit.py
