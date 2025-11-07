@echo off
chcp 65001 >nul
color 0C
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     MAX ANIM BURN - KRASSER AUTO-INSTALLER                    ║
echo ║     Installiert ALLES automatisch!                            ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo ⚠️  ACHTUNG: Dieses Skript installiert automatisch:
echo    - Python 3.11 (falls nicht vorhanden)
echo    - Alle benötigten Python-Bibliotheken
echo    - System-Updates für pip
echo.
timeout /t 3 >nul

echo.
echo ═══════════════════════════════════════════════════════════════
echo [SCHRITT 1/5] SYSTEM-CHECK
echo ═══════════════════════════════════════════════════════════════
echo.

:: Admin-Rechte prüfen
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ❌ FEHLER: Keine Administrator-Rechte!
    echo.
    echo    Bitte als Administrator ausführen:
    echo    Rechtsklick auf install.bat ^> "Als Administrator ausführen"
    echo.
    pause
    exit /b 1
)
echo ✓ Administrator-Rechte: OK

:: Prüfe ob Python installiert ist
echo.
echo [*] Prüfe Python-Installation...
python --version >nul 2>&1
if %errorLevel% equ 0 (
    echo ✓ Python ist bereits installiert:
    python --version
    set PYTHON_INSTALLED=1
) else (
    echo ❌ Python ist NICHT installiert
    set PYTHON_INSTALLED=0
)

echo.
echo ═══════════════════════════════════════════════════════════════
echo [SCHRITT 2/5] PYTHON-INSTALLATION
echo ═══════════════════════════════════════════════════════════════
echo.

if %PYTHON_INSTALLED% equ 0 (
    echo [*] Lade Python 3.11 herunter...
    echo     Download-URL: https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
    echo.

    :: Python Installer herunterladen
    powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -OutFile '%TEMP%\python_installer.exe'}"

    if exist "%TEMP%\python_installer.exe" (
        echo ✓ Download abgeschlossen!
        echo.
        echo [*] Installiere Python 3.11...
        echo     (Dies kann einige Minuten dauern)

        :: Python silent installieren mit allen Optionen
        "%TEMP%\python_installer.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_pip=1 Include_launcher=1

        :: Warte auf Installation
        timeout /t 30 >nul

        :: Lösche Installer
        del "%TEMP%\python_installer.exe"

        echo ✓ Python 3.11 wurde installiert!
        echo.
        echo [*] Aktualisiere PATH-Umgebungsvariable...

        :: PATH neu laden
        call refreshenv >nul 2>&1

        :: Alternativ: Direkt Python-Pfad setzen
        set PATH=%PATH%;C:\Program Files\Python311;C:\Program Files\Python311\Scripts

        echo ✓ PATH aktualisiert!
    ) else (
        echo ❌ FEHLER: Python-Download fehlgeschlagen!
        echo.
        echo    Bitte installiere Python manuell von:
        echo    https://www.python.org/downloads/
        echo.
        pause
        exit /b 1
    )
) else (
    echo ✓ Python-Installation wird übersprungen (bereits vorhanden)
)

echo.
echo ═══════════════════════════════════════════════════════════════
echo [SCHRITT 3/5] PIP UPDATE
echo ═══════════════════════════════════════════════════════════════
echo.

echo [*] Aktualisiere pip auf neueste Version...
python -m pip install --upgrade pip --quiet
echo ✓ pip wurde aktualisiert!

echo.
echo [*] Installiere wheel und setuptools...
python -m pip install --upgrade wheel setuptools --quiet
echo ✓ Build-Tools installiert!

echo.
echo ═══════════════════════════════════════════════════════════════
echo [SCHRITT 4/5] DEPENDENCIES INSTALLATION
echo ═══════════════════════════════════════════════════════════════
echo.

echo [*] Installiere alle benötigten Bibliotheken...
echo.

:: Prüfe ob requirements.txt existiert
if exist requirements.txt (
    echo ✓ requirements.txt gefunden!
    echo.
    echo [*] Installiere aus requirements.txt:
    type requirements.txt
    echo.
    python -m pip install -r requirements.txt --upgrade
) else (
    echo ⚠️  requirements.txt nicht gefunden, installiere manuell...
    echo.
    python -m pip install numpy matplotlib pygame moderngl moderngl-window pyrr pillow psutil --upgrade
)

echo.
echo ✓ Alle Bibliotheken wurden installiert!

echo.
echo ═══════════════════════════════════════════════════════════════
echo [SCHRITT 5/5] SYSTEM-INFO
echo ═══════════════════════════════════════════════════════════════
echo.

echo [*] Installierte Versionen:
echo.
python --version
echo.
python -m pip list | findstr /C:"numpy" /C:"matplotlib" /C:"pygame" /C:"moderngl" /C:"psutil"

echo.
echo ═══════════════════════════════════════════════════════════════
echo.
echo    🔥🔥🔥 INSTALLATION ABGESCHLOSSEN! 🔥🔥🔥
echo.
echo    Alles bereit für MAX ANIM BURN!
echo.
echo    Starte das Programm mit:
echo    python max_anim_burn.py
echo.
echo    ODER direkt jetzt starten? (Drücke eine Taste)
echo.
echo ═══════════════════════════════════════════════════════════════
echo.
pause

cls
echo.
echo 🚀 STARTE MAX ANIM BURN...
echo.
timeout /t 2 >nul

python max_anim_burn.py

pause
