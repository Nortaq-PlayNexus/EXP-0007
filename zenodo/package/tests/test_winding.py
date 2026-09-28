import numpy as np
import pytest
import sys, os
"""Test winding number calculation and regression tests for known bugs."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))

from app.optics.field import ComplexField
from app.optics.deep_scan import DeepBeamScan
from app.optics.propagation import propagate_fresnel


def winding_count_fixed(phase_2d):
    """Fixed winding_count — no double-np.angle."""
    ph = phase_2d.astype(np.float64)
    a, b, c, d = ph[:-1,:-1], ph[:-1,1:], ph[1:,1:], ph[1:,:-1]
    dphi = lambda x, y: np.mod(x - y + np.pi, 2*np.pi) - np.pi
    curl = dphi(b,a) + dphi(c,b) + dphi(d,c) + dphi(a,d)
    charge = np.round(curl / (2*np.pi))
    return int(np.sum(np.abs(charge) > 0.5))


def winding_count_buggy(phase_2d):
    """Buggy winding_count — double np.angle (documented regression test)."""
    ph = np.angle(phase_2d)
    a, b, c, d = ph[:-1,:-1], ph[:-1,1:], ph[1:,1:], ph[1:,:-1]
    dphi = lambda x, y: np.mod(x - y + np.pi, 2*np.pi) - np.pi
    curl = dphi(b,a) + dphi(c,b) + dphi(d,c) + dphi(a,d)
    charge = np.round(curl / (2*np.pi))
    return int(np.sum(np.abs(charge) > 0.5))


class TestWindingFlatPhase:
    def test_fixed_gives_zero(self):
        phase = np.zeros((32, 32))
        assert winding_count_fixed(phase) == 0

    def test_buggy_gives_zero(self):
        phase = np.zeros((32, 32))
        assert winding_count_buggy(phase) == 0


class TestWindingSingleVortex:
    def test_fixed_gives_one(self):
        y, x = np.ogrid[:64, :64]
        phase = np.arctan2((y-32).astype(float), (x-32).astype(float))
        assert winding_count_fixed(phase) == 1, f"Fixed gave {winding_count_fixed(phase)}"

    def test_buggy_gives_127_regression(self):
        """Regression test: buggy method gives 127 on 1 vortex (DO NOT FIX)."""
        y, x = np.ogrid[:64, :64]
        phase = np.arctan2((y-32).astype(float), (x-32).astype(float))
        result = winding_count_buggy(phase)
        assert result == 127, f"Buggy method should give 127, got {result}"


class TestWindingFourVortices:
    def test_fixed_gives_four(self):
        positions = [(16,16),(16,48),(48,16),(48,48)]
        phase = np.zeros((64, 64))
        for cy, cx in positions:
            phase += np.arctan2((np.ogrid[:64,64][0]-cy).astype(float), (np.ogrid[:64,64][1]-cx).astype(float))
        assert winding_count_fixed(phase) == 4, f"Fixed gave {winding_count_fixed(phase)}"

    def test_buggy_gives_609_regression(self):
        """Regression test: buggy method gives 609 on 4 vortices."""
        positions = [(16,16),(16,48),(48,16),(48,48)]
        phase = np.zeros((64, 64))
        for cy, cx in positions:
            phase += np.arctan2((np.ogrid[:64,64][0]-cy).astype(float), (np.ogrid[:64,64][1]-cx).astype(float))
        result = winding_count_buggy(phase)
        assert result == 609, f"Buggy method should give 609, got {result}"


class TestDetectorKnownVortex:
    def test_dbs_single_vortex(self):
        """DBS should correctly count 1 vortex (regression for overcount)."""
        y, x = np.ogrid[:64, :64]
        amp = np.exp(-((y-32)**2 + (x-32)**2) / 50)
        phase = np.arctan2((y-32).astype(float), (x-32).astype(float))
        E0 = ComplexField(amplitude=amp, phase=phase, pixel_size=1e-6, wavelength_nm=633)
        dbs = DeepBeamScan()
        count = len(dbs.find_features(E0))
        assert count == 1, f"DBS should give 1 for single vortex, got {count}"
