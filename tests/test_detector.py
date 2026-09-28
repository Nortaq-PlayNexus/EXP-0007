import numpy as np
import pytest
import sys, os
"""Test detector behavior and known limitations."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))

from app.optics.field import ComplexField
from app.optics.deep_scan import DeepBeamScan
from app.optics.propagation import propagate_fresnel


class TestDBSPlaneWave:
    def test_plane_wave_no_features(self):
        E0 = ComplexField(amplitude=np.ones((32, 32)), phase=np.zeros((32, 32)), pixel_size=1e-6, wavelength_nm=633)
        dbs = DeepBeamScan()
        count = len(dbs.find_features(E0))
        assert count == 0, f"Plane wave should have 0 features, got {count}"


class TestDBSGaussian:
    def test_gaussian_no_features(self):
        y, x = np.ogrid[:32, :32]
        amp = np.exp(-((y-16)**2 + (x-16)**2) / 100)
        E0 = ComplexField(amplitude=amp, phase=np.zeros((32, 32)), pixel_size=1e-6, wavelength_nm=633)
        dbs = DeepBeamScan()
        count = len(dbs.find_features(E0))
        assert count == 0, f"Gaussian should have 0 features, got {count}"


class TestDBSDeadParameter:
    def test_min_prominence_unused(self):
        """Verify min_prominence parameter is dead (regression test)."""
        import inspect
        src = inspect.getsource(DeepBeamScan.find_features)
        usage_lines = [l for l in src.split('\n') if 'min_prominence' in l and 'def ' not in l]
        assert len(usage_lines) == 0, f"min_prominence IS used: {usage_lines}"


class TestDBSRandomField:
    def test_random_field_overcount_documented(self):
        """Random fields produce many features — documented behavior, not a bug to fix."""
        np.random.seed(42)
        phase = np.random.uniform(-np.pi, np.pi, (32, 32))
        E0 = ComplexField(amplitude=np.ones((32, 32)), phase=phase, pixel_size=1e-6, wavelength_nm=633)
        dbs = DeepBeamScan()
        count = len(dbs.find_features(E0))
        assert count > 1000, f"Random field should overcount: {count}"


class TestPropagationDetectorConsistency:
    def test_propagated_field_deterministic(self):
        E0 = ComplexField(amplitude=np.ones((32, 32)), phase=np.zeros((32, 32)), pixel_size=1e-6, wavelength_nm=633)
        E_z1280 = propagate_fresnel(E0, z=1280, pixel_size=1e-6)
        dbs = DeepBeamScan()
        count1 = len(dbs.find_features(E_z1280))
        count2 = len(dbs.find_features(E_z1280))
        assert count1 == count2, f"Determinism check: {count1} != {count2}"
