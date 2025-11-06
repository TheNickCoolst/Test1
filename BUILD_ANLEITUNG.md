# MAX ANIM BURN - Build-Anleitung

## 📦 Fertige Ausführbare Datei

### Linux/Unix
Die Datei `max_anim_burn` ist eine ausführbare Linux-Datei (ELF 64-bit).

**Verwendung:**
```bash
./max_anim_burn
```

Falls Berechtigungsfehler auftreten:
```bash
chmod +x max_anim_burn
./max_anim_burn
```

---

## 🪟 Windows .exe erstellen

Da die aktuelle Build-Umgebung Linux ist, wurde eine Linux-Executable erstellt.
Für eine **Windows .exe** gibt es folgende Möglichkeiten:

### Methode 1: PyInstaller auf Windows ausführen (Empfohlen)

1. **Python auf Windows installieren**
   - Download: https://www.python.org/downloads/
   - Bei Installation "Add Python to PATH" aktivieren

2. **PyInstaller installieren**
   ```cmd
   pip install pyinstaller
   ```

3. **Dependencies installieren**
   ```cmd
   pip install numpy matplotlib pygame moderngl moderngl-window pyrr pillow psutil
   ```

4. **Executable erstellen**
   ```cmd
   pyinstaller --onefile --name max_anim_burn max_anim_burn.py
   ```

5. **Fertig!**
   - Die .exe befindet sich in: `dist\max_anim_burn.exe`

### Methode 2: Mit Icon und erweiterten Optionen

```cmd
pyinstaller --onefile ^
            --name max_anim_burn ^
            --console ^
            --hidden-import numpy ^
            --hidden-import matplotlib ^
            --hidden-import pygame ^
            max_anim_burn.py
```

Optional: Icon hinzufügen
```cmd
pyinstaller --onefile --icon=myicon.ico --name max_anim_burn max_anim_burn.py
```

### Methode 3: Cross-Compilation mit Wine (Fortgeschritten)

Für Linux-Nutzer, die Windows .exe erstellen möchten:

```bash
# Wine und Python für Windows installieren
sudo apt-get install wine wine64
wget https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
wine python-3.11.0-amd64.exe

# PyInstaller in Wine installieren
wine pip install pyinstaller

# Build
wine pyinstaller --onefile max_anim_burn.py
```

---

## 🔄 Rebuild (Neu kompilieren)

Falls Sie das Programm ändern und neu kompilieren möchten:

### Linux:
```bash
pyinstaller max_anim_burn.spec
```

### Windows:
```cmd
pyinstaller max_anim_burn.spec
```

Die `.spec` Datei enthält alle Build-Konfigurationen.

---

## 📋 Systemanforderungen

### Für die Ausführung:
- **CPU:** Multi-Core empfohlen (wird alle Cores auslasten!)
- **RAM:** Mindestens 8 GB (Programm allokiert mehrere GB)
- **GPU:** Dedizierte GPU empfohlen (für Partikel-Rendering)
- **Speicher:** Mehrere GB freier Speicherplatz (für temporäre Test-Dateien)

### Für den Build:
- **Python:** 3.8 oder höher
- **PyInstaller:** 6.0 oder höher
- **Speicher:** ~500 MB für PyInstaller und Dependencies

---

## ⚠️ WICHTIGE HINWEISE

**WARNUNG: Dieses Programm ist ein STRESS-TEST-Tool!**

- ✅ NUR in Sandbox/VM-Umgebungen verwenden
- ❌ NICHT auf Produktionssystemen ausführen
- ❌ NICHT auf Laptops (Überhitzungsgefahr)
- ⚠️ Kann System zum Absturz bringen
- ⚠️ Maximale CPU/GPU/RAM/Disk-Auslastung

Das Programm:
- Belastet ALLE CPU-Cores auf 100%
- Rendert 500.000 Partikel in 4K-Auflösung
- Allokiert mehrere GB RAM
- Erstellt/löscht kontinuierlich Test-Dateien (je 100 MB)
- Generiert hochauflösende Fraktal-Animationen

---

## 📝 Technische Details

### Build-Informationen:
- **Kompiliert mit:** PyInstaller 6.16.0
- **Python-Version:** 3.11
- **Typ:** Standalone-Executable (alle Dependencies eingebettet)
- **Größe:** ~8 MB (Linux) / ~12-15 MB (Windows typisch)

### Eingebettete Bibliotheken:
- NumPy (numerische Berechnungen)
- Matplotlib (Fraktal-Visualisierung)
- Pygame (Partikel-System & GPU-Rendering)
- ModernGL (OpenGL-Wrapper)
- PSUtil (System-Monitoring)
- Pillow (Bildverarbeitung)

---

## 🐛 Troubleshooting

### "Permission denied" (Linux)
```bash
chmod +x max_anim_burn
```

### Fehlende Dependencies beim Ausführen
Falls die Executable Dependencies vermisst:
```bash
# Rebuild mit hidden-imports
pyinstaller --onefile \
            --hidden-import numpy.core._multiarray_umath \
            --hidden-import pygame \
            max_anim_burn.py
```

### Windows Antivirus blockiert die .exe
PyInstaller-Executables werden manchmal fälschlicherweise als Malware erkannt.
- Whitelist-Ausnahme hinzufügen
- Oder: Python-Script direkt ausführen (`python max_anim_burn.py`)

---

## 📄 Lizenz & Haftung

Dieses Tool ist ausschließlich für Testzwecke gedacht.
Der Autor übernimmt keine Haftung für Hardware-Schäden oder System-Ausfälle.

**Verwendung auf eigene Gefahr!**
