#!/usr/bin/env python3
"""
MAX ANIM BURN - Extreme Sandbox Stress Test
============================================
ACHTUNG: Dieses Programm verursacht extreme CPU-/GPU-/RAM-/Disk-Last
und kann deinen PC zum Absturz bringen!

NUR FÜR SANDBOX-TESTS VERWENDEN!

Dieses Programm testet System-Grenzen durch:
- Maximale CPU-Auslastung (alle Cores)
- Extreme GPU-Rendering-Last
- Massive RAM-Allokation
- Intensives Disk I/O (Test-Dateien)
- Unendliche HD/4K Animationen
"""

import sys
import os
import time
import random
import threading
import multiprocessing as mp
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Automatische Dependency-Installation
def install_dependencies():
    """Installiert alle benötigten Bibliotheken"""
    dependencies = [
        'numpy',
        'matplotlib',
        'pygame',
        'moderngl',
        'moderngl-window',
        'pyrr',
        'pillow',
        'psutil'
    ]

    print("Überprüfe/Installiere Dependencies...")
    import subprocess
    for dep in dependencies:
        try:
            __import__(dep.replace('-', '_'))
        except ImportError:
            print(f"  Installiere {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", dep])
    print("Dependencies bereit!\n")

install_dependencies()

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend für Performance
import matplotlib.pyplot as plt
from matplotlib import animation
import pygame
from pygame.locals import *
try:
    import moderngl
    import moderngl_window as mglw
    MODERNGL_AVAILABLE = True
except:
    MODERNGL_AVAILABLE = False
import psutil

# Konfiguration - KRASSER MODUS! 🔥
RESOLUTION = (7680, 4320)  # 8K ULTRA HD!
TEST_DIR = Path("./sandbox_stress_test")
NUM_PARTICLES = 1000000  # 1 MILLION Partikel!
NUM_CPU_WORKERS = mp.cpu_count() * 4  # VIERFACHE CPU-Core-Anzahl!
FILE_STRESS_SIZE_MB = 200  # 200 MB Test-Dateien!
RAM_CHUNK_SIZE_MB = 200  # 200 MB RAM-Chunks
MAX_RAM_CHUNKS = 100  # Bis zu 20 GB RAM!

print("""
╔════════════════════════════════════════════════════════════════╗
║     🔥🔥🔥 MAX ANIM BURN - KRASSER MODUS! 🔥🔥🔥              ║
║        EXTREME SANDBOX STRESS TEST - ULTRA EDITION            ║
╚════════════════════════════════════════════════════════════════╝

⚠️⚠️⚠️  ACHTUNG: EXTREME SYSTEM-AUSLASTUNG! ⚠️⚠️⚠️

Dieses Programm wird ALLES ZERSTÖREN:
✓ ALLE CPU-Cores auf 100% auslasten (x4 Workers pro Core!)
✓ GPU MAXIMAL belasten (8K Rendering mit 1 Mio. Partikeln!)
✓ RAM BRUTAL allokieren (bis zu 20 GB!)
✓ MASSIVE Disk I/O (200 MB Dateien, 3 Worker!)
✓ Crypto-Mining-Simulation (SHA256-Hashing!)
✓ Fraktal-Generierung und Matrix-Operationen!

⚠️⚠️⚠️  NUR FÜR SANDBOX/VM-TESTS VERWENDEN! ⚠️⚠️⚠️
🚨 DEIN PC WIRD WAHRSCHEINLICH EINFRIEREN! 🚨

System-Info:
- CPU Cores: {cores}
- RAM Total: {ram:.1f} GB
- Test-Prozesse: {workers}
- Auflösung: {res[0]}x{res[1]} (8K ULTRA HD!)
- Partikel: {particles:,}
- File Size: {filesize} MB
- Max RAM: {maxram} GB

🔥🔥🔥 KRASSER MODUS AKTIVIERT! 🔥🔥🔥

""".format(
    cores=mp.cpu_count(),
    ram=psutil.virtual_memory().total / (1024**3),
    workers=NUM_CPU_WORKERS,
    res=RESOLUTION,
    particles=NUM_PARTICLES,
    filesize=FILE_STRESS_SIZE_MB,
    maxram=RAM_CHUNK_SIZE_MB * MAX_RAM_CHUNKS / 1024
))

response = input("Fortfahren? (JA/nein): ").strip().upper()
if response != "JA":
    print("Abgebrochen.")
    sys.exit(0)

print("\n🔥 STARTE STRESS TEST IN 3 SEKUNDEN... 🔥\n")
time.sleep(3)

# Test-Verzeichnis erstellen
TEST_DIR.mkdir(exist_ok=True)
print(f"Test-Verzeichnis: {TEST_DIR.absolute()}\n")


# ═══════════════════════════════════════════════════════════════
# CPU BURN WORKERS
# ═══════════════════════════════════════════════════════════════

def cpu_burner_mandelbrot(worker_id):
    """Berechnet kontinuierlich Mandelbrot-Sets für maximale CPU-Last"""
    print(f"[CPU-Worker {worker_id}] Gestartet - Mandelbrot Berechnung")

    iteration = 0
    while True:
        # Extrem hochauflösende Mandelbrot-Berechnung
        width, height = 4000, 4000
        max_iter = 1000

        xmin, xmax = -2.5, 1.5
        ymin, ymax = -2.0, 2.0

        x = np.linspace(xmin, xmax, width)
        y = np.linspace(ymin, ymax, height)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y

        Z = np.zeros_like(C)
        M = np.zeros(C.shape)

        for i in range(max_iter):
            mask = np.abs(Z) <= 2
            Z[mask] = Z[mask]**2 + C[mask]
            M[mask] = i

        # Weitere mathematische Operationen
        result = np.fft.fft2(M)
        result = np.abs(result)
        result = np.log1p(result)

        iteration += 1
        if iteration % 5 == 0:
            print(f"[CPU-Worker {worker_id}] Iteration {iteration} - {width}x{height} Mandelbrot")


def cpu_burner_matrix(worker_id):
    """KRASSE Massive Matrix-Operationen - 3000x3000!"""
    print(f"[CPU-Worker {worker_id}] Gestartet - EXTREME Matrix Operationen")

    iteration = 0
    while True:
        size = 3000  # Noch größer!
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)

        # NOCH MEHR intensive Operationen
        C = np.dot(A, B)
        D = np.linalg.inv(C + np.eye(size) * 0.1)
        E = np.linalg.svd(A[:800, :800])  # Größere SVD
        F = np.fft.fft2(C)
        G = np.exp(A[:200, :200])
        H = np.sin(C) + np.cos(C)  # Trigonometrie
        I = np.power(A[:100, :100], 3)  # Potenzen

        iteration += 1
        if iteration % 10 == 0:
            print(f"[CPU-Worker {worker_id}] 🔥 Matrix-Op {iteration} - {size}x{size}")


# ═══════════════════════════════════════════════════════════════
# CRYPTO MINING SIMULATOR - EXTREME CPU BURN!
# ═══════════════════════════════════════════════════════════════

def cpu_burner_crypto_simulator(worker_id):
    """Simuliert Crypto-Mining mit SHA256-Hash-Berechnungen - EXTREM!"""
    print(f"[CRYPTO-Worker {worker_id}] Gestartet - Crypto Mining Simulation")

    import hashlib
    iteration = 0
    total_hashes = 0

    while True:
        # Simuliere Proof-of-Work Mining
        nonce = 0
        target = "0000"  # 4 führende Nullen

        for _ in range(100000):  # 100k Hashes pro Iteration
            data = f"Block{iteration}Nonce{nonce}Worker{worker_id}".encode()
            hash_result = hashlib.sha256(data).hexdigest()

            if hash_result.startswith(target):
                print(f"[CRYPTO-Worker {worker_id}] 💎 BLOCK GEFUNDEN! Hash: {hash_result[:16]}... (Nonce: {nonce})")

            nonce += 1
            total_hashes += 1

        iteration += 1
        if iteration % 20 == 0:
            mhash_per_sec = (100000 * 20) / 1000000
            print(f"[CRYPTO-Worker {worker_id}] 🔥 {total_hashes:,} Hashes - {mhash_per_sec:.2f} MH/s")


# ═══════════════════════════════════════════════════════════════
# DISK STRESS WORKER
# ═══════════════════════════════════════════════════════════════

def disk_stress_worker():
    """Erstellt kontinuierlich Test-Dateien und löscht sie wieder"""
    print("[DISK-Worker] Gestartet - File Stress Test")

    file_counter = 0
    active_files = []
    max_files = 50  # Maximal 50 gleichzeitige Test-Dateien

    while True:
        try:
            # Erstelle neue Test-Datei
            filename = TEST_DIR / f"stress_test_{file_counter}_{random.randint(1000,9999)}.tmp"

            # Schreibe große Daten
            data_size = FILE_STRESS_SIZE_MB * 1024 * 1024  # MB in Bytes
            with open(filename, 'wb') as f:
                # Schreibe in Chunks
                chunk_size = 1024 * 1024  # 1 MB Chunks
                for _ in range(FILE_STRESS_SIZE_MB):
                    f.write(os.urandom(chunk_size))

            active_files.append(filename)
            print(f"[DISK] Erstellt: {filename.name} ({FILE_STRESS_SIZE_MB} MB) - Total: {len(active_files)} Dateien")

            file_counter += 1

            # Lösche alte Dateien wenn Limit erreicht
            if len(active_files) > max_files:
                old_file = active_files.pop(0)
                if old_file.exists():
                    old_file.unlink()
                    print(f"[DISK] Gelöscht: {old_file.name}")

            # Random auch zwischendurch löschen
            if random.random() < 0.3 and active_files:
                delete_file = random.choice(active_files)
                active_files.remove(delete_file)
                if delete_file.exists():
                    delete_file.unlink()
                    print(f"[DISK] Random-Gelöscht: {delete_file.name}")

            time.sleep(random.uniform(0.1, 0.5))

        except Exception as e:
            print(f"[DISK] Error: {e}")
            time.sleep(1)


# ═══════════════════════════════════════════════════════════════
# RAM ALLOCATOR
# ═══════════════════════════════════════════════════════════════

def ram_allocator():
    """Allokiert kontinuierlich MASSIVE RAM-Mengen - KRASSER MODUS!"""
    print("[RAM-Worker] Gestartet - EXTREME Memory Allocation")

    memory_chunks = []
    chunk_size = RAM_CHUNK_SIZE_MB * 1024 * 1024  # Konfigurierbare Chunk-Größe
    max_chunks = MAX_RAM_CHUNKS

    while True:
        try:
            # Allokiere neuen KRASSEN Chunk
            chunk = np.random.rand(chunk_size // 8)  # 8 bytes per float64
            memory_chunks.append(chunk)

            total_mb = len(memory_chunks) * RAM_CHUNK_SIZE_MB
            total_gb = total_mb / 1024
            ram_percent = psutil.virtual_memory().percent
            print(f"[RAM] 🔥 Allokiert: {total_mb} MB ({total_gb:.2f} GB) - RAM-Nutzung: {ram_percent:.1f}%")

            # Verhindere kompletten System-Crash durch RAM-Limit
            if len(memory_chunks) >= max_chunks or ram_percent > 85:
                freed_chunk = memory_chunks.pop(0)
                del freed_chunk  # Explizit freigeben
                print(f"[RAM] Chunk freigegeben - RAM-Nutzung: {ram_percent:.1f}%")

            # Noch aggressiver - kürzere Wartezeit!
            time.sleep(0.2)

        except MemoryError:
            print("[RAM] ⚠️  MemoryError - Gebe Chunks frei")
            memory_chunks = memory_chunks[-10:]  # Behalte nur 10 neueste
            time.sleep(2)


# ═══════════════════════════════════════════════════════════════
# PYGAME PARTICLE ANIMATION
# ═══════════════════════════════════════════════════════════════

def pygame_particle_animation():
    """Extreme Partikel-Animation mit Pygame"""
    print("[PYGAME] Gestartet - Partikel-System")

    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION, DOUBLEBUF | HWSURFACE)
    pygame.display.set_caption("MAX ANIM BURN - Partikel-System")
    clock = pygame.time.Clock()

    # Partikel initialisieren
    num_particles = NUM_PARTICLES
    positions = np.random.rand(num_particles, 2) * RESOLUTION
    velocities = (np.random.rand(num_particles, 2) - 0.5) * 10
    colors = np.random.randint(0, 256, (num_particles, 3))
    sizes = np.random.randint(1, 5, num_particles)

    frame = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Partikel-Physik
        positions += velocities

        # Bounce an Rändern
        for i in range(2):
            mask = positions[:, i] < 0
            positions[mask, i] = 0
            velocities[mask, i] *= -1

            mask = positions[:, i] > RESOLUTION[i]
            positions[mask, i] = RESOLUTION[i]
            velocities[mask, i] *= -1

        # Gravitation zu Zentrum
        center = np.array(RESOLUTION) / 2
        to_center = center - positions
        distance = np.linalg.norm(to_center, axis=1, keepdims=True)
        distance = np.maximum(distance, 1)  # Verhindere Division durch 0
        gravity = to_center / distance * 0.1
        velocities += gravity

        # Füge Chaos hinzu
        velocities += (np.random.rand(num_particles, 2) - 0.5) * 0.5

        # Rendering
        screen.fill((0, 0, 0))

        # Zeichne Partikel
        for i in range(0, num_particles, 10):  # Jeder 10. für Performance
            pos = positions[i].astype(int)
            color = tuple(colors[i])
            pygame.draw.circle(screen, color, pos, sizes[i])

        # Zusätzliche visuelle Effekte
        if frame % 2 == 0:
            # Verbindungslinien zwischen nahen Partikeln
            sample_size = min(1000, num_particles)
            sample_indices = np.random.choice(num_particles, sample_size, replace=False)
            sample_pos = positions[sample_indices]

            for i in range(min(500, len(sample_pos))):
                p1 = sample_pos[i]
                distances = np.linalg.norm(sample_pos - p1, axis=1)
                nearby = np.where((distances < 100) & (distances > 0))[0]

                if len(nearby) > 0:
                    p2 = sample_pos[nearby[0]]
                    pygame.draw.line(screen, (50, 50, 100),
                                   p1.astype(int), p2.astype(int), 1)

        pygame.display.flip()

        frame += 1
        if frame % 60 == 0:
            fps = clock.get_fps()
            print(f"[PYGAME] Frame {frame} - FPS: {fps:.1f} - Partikel: {num_particles:,}")

        # KEIN Frame-Limit für maximale GPU-Last!
        # clock.tick(60)  # AUSKOMMENTIERT

    pygame.quit()


# ═══════════════════════════════════════════════════════════════
# MATPLOTLIB FRACTAL ANIMATION
# ═══════════════════════════════════════════════════════════════

def matplotlib_fractal_animation():
    """Erzeugt kontinuierlich komplexe Fraktal-Visualisierungen"""
    print("[MATPLOTLIB] Gestartet - Fraktal-Visualisierung")

    frame = 0
    while True:
        try:
            # Julia-Set Animation
            width, height = 2000, 2000
            max_iter = 500

            # Animierte Julia-Set Parameter
            c = complex(-0.7, 0.27015) + complex(np.cos(frame * 0.05), np.sin(frame * 0.05)) * 0.1

            x = np.linspace(-2, 2, width)
            y = np.linspace(-2, 2, height)
            X, Y = np.meshgrid(x, y)
            Z = X + 1j * Y

            M = np.zeros(Z.shape)

            for i in range(max_iter):
                mask = np.abs(Z) <= 2
                Z[mask] = Z[mask]**2 + c
                M[mask] = i

            # Plotte
            fig, ax = plt.subplots(figsize=(20, 20), dpi=200)
            im = ax.imshow(M, extent=[-2, 2, -2, 2], cmap='hot', interpolation='bilinear')
            ax.set_title(f'Julia Set Animation - Frame {frame}', fontsize=20)
            plt.colorbar(im)

            filename = TEST_DIR / f"fractal_frame_{frame}.png"
            plt.savefig(filename, dpi=200)
            plt.close(fig)

            print(f"[MATPLOTLIB] Frame {frame} - Julia-Set generiert: {filename.name}")

            # Lösche alte Frames
            if frame > 10:
                old_file = TEST_DIR / f"fractal_frame_{frame-10}.png"
                if old_file.exists():
                    old_file.unlink()

            frame += 1

        except Exception as e:
            print(f"[MATPLOTLIB] Error: {e}")
            time.sleep(1)


# ═══════════════════════════════════════════════════════════════
# MAIN ORCHESTRATOR
# ═══════════════════════════════════════════════════════════════

def main():
    """Startet alle Stress-Test-Komponenten parallel"""

    print("\n" + "="*70)
    print("STARTE ALLE STRESS-TEST-KOMPONENTEN")
    print("="*70 + "\n")

    processes = []
    threads = []

    try:
        # CPU Burner Prozesse (Multiprocessing für echte Parallelität)
        print(f"Starte {NUM_CPU_WORKERS} CPU-Burner-Prozesse...\n")

        # 1/3 Mandelbrot Workers
        third = NUM_CPU_WORKERS // 3
        for i in range(third):
            p = mp.Process(target=cpu_burner_mandelbrot, args=(i,))
            p.daemon = True
            p.start()
            processes.append(p)

        # 1/3 Matrix Workers
        for i in range(third, third * 2):
            p = mp.Process(target=cpu_burner_matrix, args=(i,))
            p.daemon = True
            p.start()
            processes.append(p)

        # 1/3 CRYPTO MINING SIMULATORS! 🔥
        for i in range(third * 2, NUM_CPU_WORKERS):
            p = mp.Process(target=cpu_burner_crypto_simulator, args=(i,))
            p.daemon = True
            p.start()
            processes.append(p)

        time.sleep(2)

        # MEHRERE Disk Stress Worker! 🔥
        print("\nStarte 3 KRASSE Disk-Stress-Worker...\n")
        for _ in range(3):
            t = threading.Thread(target=disk_stress_worker, daemon=True)
            t.start()
            threads.append(t)

        time.sleep(1)

        # MEHRERE RAM Allocators! 🔥
        print("Starte 2 EXTREME RAM-Allocators...\n")
        for _ in range(2):
            t = threading.Thread(target=ram_allocator, daemon=True)
            t.start()
            threads.append(t)

        time.sleep(1)

        # Matplotlib Fractal Animation (Thread)
        print("Starte Matplotlib-Fraktal-Animation...\n")
        t = threading.Thread(target=matplotlib_fractal_animation, daemon=True)
        t.start()
        threads.append(t)

        time.sleep(2)

        # Pygame Particle Animation (Main Thread für GPU)
        print("Starte Pygame-Partikel-System (Main Thread)...\n")
        print("\n" + "="*70)
        print("ALLE SYSTEME AKTIV - MAXIMALE AUSLASTUNG!")
        print("Drücke ESC im Pygame-Fenster zum Beenden")
        print("="*70 + "\n")

        # Haupt-Animation läuft im Main-Thread
        pygame_particle_animation()

    except KeyboardInterrupt:
        print("\n\n[MAIN] KeyboardInterrupt - Beende...")

    finally:
        print("\n[MAIN] Cleanup...")

        # Beende alle Prozesse
        for p in processes:
            p.terminate()

        # Warte auf Prozess-Ende
        for p in processes:
            p.join(timeout=2)

        # Cleanup Test-Dateien
        print(f"[MAIN] Räume Test-Verzeichnis auf: {TEST_DIR}")
        for file in TEST_DIR.glob("*"):
            try:
                file.unlink()
                print(f"  Gelöscht: {file.name}")
            except:
                pass

        try:
            TEST_DIR.rmdir()
            print(f"  Verzeichnis entfernt: {TEST_DIR}")
        except:
            print(f"  Verzeichnis konnte nicht entfernt werden: {TEST_DIR}")

        print("\n[MAIN] Stress-Test beendet!")
        print("="*70)


if __name__ == "__main__":
    main()
