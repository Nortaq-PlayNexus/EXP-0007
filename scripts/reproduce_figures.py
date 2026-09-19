#!/usr/bin/env python3
"""Reproduce all EXP-0007 figures."""
import numpy as np
import os
import sys

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))
os.environ['PYTHONPATH'] = PROJECT + ";" + os.environ.get('PYTHONPATH', '')
os.chdir(PROJECT)

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def main():
    print("Reproducing EXP-0007 figures...")
    
    from app.optics.structured_light import vortex_crystal_field
    from app.optics.deep_scan import DeepBeamScan
    from app.optics.field import ComplexField
    from app.optics.propagation import propagate_fresnel
    
    plt = None
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available — skipping figure generation")
        return 0
    
    lattice = vortex_crystal_field(shape=(256, 256), rows=6, cols=8, pixel_size=1e-6, wavelength_nm=694.3)
    E0 = ComplexField(amplitude=lattice.amplitude, phase=lattice.phase, pixel_size=1e-6, wavelength_nm=694.3)
    
    fig_dir = os.path.join(REPO, "results", "figures")
    os.makedirs(fig_dir, exist_ok=True)
    
    # Figure 1: Original field phase
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    im = ax.imshow(E0.phase, cmap='twilight', vmin=-np.pi, vmax=np.pi)
    ax.set_title("Original Lattice Phase (z=0)")
    ax.set_xlabel("x (pixels)")
    ax.set_ylabel("y (pixels)")
    plt.colorbar(im, ax=ax, label="Phase (rad)")
    fig.savefig(os.path.join(fig_dir, "fig01_original_phase.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ fig01_original_phase.png")
    
    # Figure 2: Propagated field phase
    E_z = propagate_fresnel(E0, z=1280, pixel_size=1e-6)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    im = ax.imshow(E_z.phase, cmap='twilight', vmin=-np.pi, vmax=np.pi)
    ax.set_title("Propagated Field Phase (z=+1280 µm)")
    ax.set_xlabel("x (pixels)")
    ax.set_ylabel("y (pixels)")
    plt.colorbar(im, ax=ax, label="Phase (rad)")
    fig.savefig(os.path.join(fig_dir, "fig02_propagated_phase.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ fig02_propagated_phase.png")
    
    # Figure 3: Intensity at z=+1280
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    im = ax.imshow(E_z.intensity_normalized, cmap='hot')
    ax.set_title("Propagated Field Intensity (z=+1280 µm)")
    ax.set_xlabel("x (pixels)")
    ax.set_ylabel("y (pixels)")
    plt.colorbar(im, ax=ax, label="Normalized Intensity")
    fig.savefig(os.path.join(fig_dir, "fig03_propagated_intensity.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ fig03_propagated_intensity.png")
    
    # Figure 4: Feature positions overlay
    dbs = DeepBeamScan()
    feats_z0 = dbs.find_features(E0)
    feats_z = dbs.find_features(E_z)
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(E_z.intensity_normalized, cmap='hot', alpha=0.7)
    if feats_z0:
        ax.scatter([f['x'] for f in feats_z0], [f['y'] for f in feats_z0], c='blue', marker='o', s=20, label='z=0 features')
    if feats_z:
        ax.scatter([f['x'] for f in feats_z], [f['y'] for f in feats_z], c='red', marker='x', s=15, label='z=+1280 features')
    ax.set_title("Feature Positions: z=0 (blue) vs z=+1280 (red)")
    ax.legend()
    fig.savefig(os.path.join(fig_dir, "fig04_feature_positions.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print("  ✓ fig04_feature_positions.png")
    
    print("\nAll figures generated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
