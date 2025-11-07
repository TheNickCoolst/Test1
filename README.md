# 🔥🔥🔥 MAX ANIM BURN - KRASSER MODUS! 🔥🔥🔥

## EXTREME SANDBOX STRESS TEST - ULTRA EDITION

![WARNING](https://img.shields.io/badge/WARNING-EXTREME_SYSTEM_LOAD-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)

---

## ⚠️⚠️⚠️ WARNUNG ⚠️⚠️⚠️

**Dieses Programm ist EXTREM und wird dein System an seine absoluten Grenzen bringen!**

- ❌ **NICHT** auf deinem Produktiv-PC ausführen!
- ❌ **NICHT** auf einem Server ausführen!
- ✅ **NUR** in einer isolierten Sandbox/VM verwenden!
- 🚨 **Kann deinen PC zum Einfrieren/Absturz bringen!**

---

## 🎯 Was macht dieses Programm?

MAX ANIM BURN ist ein **extremer Systemstresstest**, der entwickelt wurde, um Sandbox-Umgebungen und virtuelle Maschinen an ihre absoluten Grenzen zu bringen.

### 🔥 Features - KRASSER MODUS:

#### 💻 CPU-Last (x4 Workers pro Core!)
- **Mandelbrot-Berechnung**: Hochauflösende Fraktal-Berechnungen (4000x4000, 1000 Iterationen)
- **Matrix-Operationen**: Massive 3000x3000 Matrix-Multiplikationen, Inversionen, SVD
- **Crypto-Mining-Simulation**: SHA256-Hash-Berechnungen (Proof-of-Work Simulation)

#### 🎨 GPU-Last (8K Ultra HD!)
- **8K Rendering**: 7680x4320 Auflösung (4x mehr als 4K!)
- **1 Million Partikel**: Echtzeit-Partikelsystem mit Physik-Simulation
- **Visuelle Effekte**: Gravitationseffekte, Partikel-Verbindungen, Chaos-Engine

#### 💾 RAM-Allokation (bis zu 20 GB!)
- **2 aggressive RAM-Allocators**: Je 200 MB Chunks
- **Bis zu 100 Chunks**: Maximal 20 GB RAM-Nutzung
- **Dynamische Verwaltung**: Verhindert kompletten System-Crash

#### 💽 Disk I/O (3 Worker!)
- **3 parallele Disk-Worker**: Massive I/O-Operationen
- **200 MB Dateien**: Große Test-Dateien mit Zufallsdaten
- **Kontinuierliches Löschen/Erstellen**: Extreme Festplatten-Belastung

#### 📊 Zusätzlich:
- **Fraktal-Generierung**: Julia-Set-Animationen (2000x2000, 500 Iterationen)
- **Matplotlib-Rendering**: Hochauflösende Visualisierungen

---

## 🚀 Installation - KRASSER AUTO-INSTALLER!

### Windows - Super Einfach:

**Einfach `install.bat` als Administrator ausführen!**

```batch
Rechtsklick auf install.bat → "Als Administrator ausführen"
```

Das Skript macht **ALLES automatisch**:
- ✅ Prüft ob Python installiert ist
- ✅ Lädt Python 3.11 herunter (falls nicht vorhanden)
- ✅ Installiert Python automatisch
- ✅ Aktualisiert pip
- ✅ Installiert alle Dependencies
- ✅ Startet das Programm

**Kein manuelles Setup nötig - VOLL AUTOMATISCH!**

---

### Manuelle Installation (Linux/Mac):

```bash
# Python 3.11+ installieren (falls nicht vorhanden)
# Ubuntu/Debian:
sudo apt update
sudo apt install python3.11 python3-pip

# Installation der Dependencies:
pip install -r requirements.txt

# Programm starten:
python3 max_anim_burn.py
```

---

## 📦 Dependencies

```
numpy          # Matrix-Operationen
matplotlib     # Visualisierungen
pygame         # Partikel-Rendering
moderngl       # OpenGL-Rendering
moderngl-window
pyrr           # 3D-Mathematik
pillow         # Bildverarbeitung
psutil         # System-Monitoring
```

---

## 🎮 Verwendung

### Windows (Automatisch):
```batch
install.bat
```

### Manuell:
```bash
python max_anim_burn.py
```

### Beenden:
- Drücke **ESC** im Pygame-Fenster
- Oder **STRG+C** im Terminal

**Das Programm räumt automatisch alle Test-Dateien auf!**

---

## 📊 Systemvoraussetzungen

### Minimum (für Test):
- **CPU**: 4+ Cores
- **RAM**: 8 GB
- **Disk**: 10 GB freier Speicher
- **GPU**: Beliebige (integriert reicht)
- **Python**: 3.8+

### Empfohlen (für vollen Stress):
- **CPU**: 8+ Cores (16+ Threads)
- **RAM**: 32 GB
- **Disk**: 50 GB freier Speicher (SSD!)
- **GPU**: Dedizierte Grafikkarte
- **Python**: 3.11+

### ⚠️ Für KRASSEN MODUS:
- **CPU**: 16+ Cores
- **RAM**: 64 GB
- **Disk**: NVMe SSD
- **GPU**: High-End Gaming GPU
- **System**: In einer isolierten VM/Sandbox!

---

## 🔧 Konfiguration

Im Code (`max_anim_burn.py`) kannst du die Intensität anpassen:

```python
# Zeile 70-76:
RESOLUTION = (7680, 4320)  # 8K - reduziere für weniger GPU-Last
NUM_PARTICLES = 1000000    # Partikel - reduziere für weniger Last
NUM_CPU_WORKERS = mp.cpu_count() * 4  # CPU-Worker - reduziere Multiplikator
FILE_STRESS_SIZE_MB = 200  # Datei-Größe - reduziere für weniger Disk I/O
RAM_CHUNK_SIZE_MB = 200    # RAM-Chunk-Größe - reduziere für weniger RAM
MAX_RAM_CHUNKS = 100       # Max RAM-Chunks - reduziere für weniger RAM
```

---

## 🛡️ Sicherheit

**Dieses Tool ist KEIN Virus oder Malware!**

- ✅ Vollständiger Open-Source-Code
- ✅ Klare Warnhinweise
- ✅ Nutzer muss explizit "JA" eingeben
- ✅ Automatisches Cleanup aller Test-Dateien
- ✅ Keine Netzwerk-Aktivität
- ✅ Keine Datensammlung

**Zweck**: Legitimate Systemtests für:
- Sandbox-Evaluation
- VM-Performance-Tests
- Kühlungstests
- Stabilitätstests
- Übertaktungs-Tests

---

## 📝 Was wird getestet?

1. **CPU-Stabilität**: Können alle Cores gleichzeitig 100% Last verarbeiten?
2. **RAM-Stabilität**: Funktioniert große RAM-Allokation ohne Fehler?
3. **Disk-Performance**: Wie schnell kann das System große Dateien schreiben?
4. **GPU-Performance**: Kann die GPU 8K mit 1 Mio. Partikeln rendern?
5. **Thermal-Management**: Kann das Kühlsystem die Last bewältigen?
6. **System-Stabilität**: Bleibt das System unter extremer Last stabil?

---

## 🎯 Use Cases

- 🔬 **Sandbox-Tests**: Teste wie gut eine Sandbox extreme Programme handhabt
- 🖥️ **VM-Performance**: Benchmark für virtuelle Maschinen
- ❄️ **Kühlungs-Tests**: Teste Kühlsysteme unter maximaler Last
- 🔧 **Übertaktungs-Tests**: Stabilitätstest für übertaktete Systeme
- 📊 **System-Benchmarking**: Vergleiche verschiedene Systeme
- 🎓 **Lernzwecke**: Verstehe Systemgrenzen und Ressourcenverwaltung

---

## 🤔 FAQ

**Q: Ist das Malware?**
A: Nein! Vollständig transparenter Open-Source-Code für legitime Systemtests.

**Q: Warum friert mein PC ein?**
A: Das ist der Zweck des Programms - extreme Belastung! Nutze eine VM!

**Q: Kann es meine Hardware beschädigen?**
A: Unwahrscheinlich, aber hohe Last über lange Zeit kann Verschleiß erhöhen. Überwache Temperaturen!

**Q: Warum brauche ich Admin-Rechte (Windows)?**
A: Nur für die automatische Python-Installation. Das Programm selbst braucht keine Admin-Rechte.

**Q: Kann ich es auf meinem Gaming-PC testen?**
A: Nicht empfohlen! Nutze lieber eine VM oder Sandbox.

---

## 📜 Lizenz

MIT License - Frei verwendbar für legitime Zwecke.

**Haftungsausschluss**: Der Autor übernimmt keine Verantwortung für Schäden durch unsachgemäße Verwendung. Nutze dieses Tool nur in kontrollierten Umgebungen!

---

## 🙏 Credits

Entwickelt für Sandbox-Tests und System-Benchmarking.

**Technologien**:
- Python 3.11+
- NumPy (Matrix-Operationen)
- Pygame (Rendering)
- Matplotlib (Visualisierungen)
- ModernGL (OpenGL)
- PSUtil (System-Monitoring)

---

## 🔥 VIEL ERFOLG MIT DEM STRESS-TEST! 🔥

**Vergiss nicht**: Nur in Sandbox/VM verwenden!

```
   _____ _______ _____  ______  _____ _____   _______ ______  _____ _______
  / ____|__   __|  __ \|  ____|/ ____/ ____| |__   __|  ____|/ ____|__   __|
 | (___    | |  | |__) | |__  | (___| (___      | |  | |__  | (___    | |
  \___ \   | |  |  _  /|  __|  \___ \\___ \     | |  |  __|  \___ \   | |
  ____) |  | |  | | \ \| |____ ____) |___) |    | |  | |____ ____) |  | |
 |_____/   |_|  |_|  \_\______|_____/_____/     |_|  |______|_____/   |_|

```

---

**⚠️ WICHTIGER HINWEIS: Dieses Tool ist ausschließlich für legitime Systemtests in kontrollierten Umgebungen gedacht. Missbrauch kann zu Systemschäden oder Datenverlust führen. Du wurdest gewarnt! ⚠️**
