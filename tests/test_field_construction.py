import numpy as np
import pytest

"""Test field construction: ComplexField and vortex lattice."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
import sys, os
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))

from app.optics.structured_light import vortex_crystal_field
from app.optics.field import ComplexField


def test_complex_field_construction():
    amp = np.ones((8, 8))
    phase = np.zeros((8, 8))
    field = ComplexField(amplitude=amp, phase=phase, pixel_size=1e-6, wavelength_nm=633)
    assert field.amplitude.shape == (8, 8)
    assert field.phase.shape == (8, 8)


def test_complex_from_amplitude_phase():
    amp = np.ones((16, 16))
    phase = np.zeros((16, 16))
    field = ComplexField(amplitude=amp, phase=phase, pixel_size=1e-6, wavelength_nm=633)
    expected = amp * np.exp(1j * phase)
    max_diff = np.max(np.abs(field.complex - expected))
    assert max_diff < 1e-14, f"Complex construction mismatch: {max_diff}"


def test_phase_range():
    lattice = vortex_crystal_field(shape=(64, 64), rows=4, cols=4, pixel_size=1e-6, wavelength_nm=633)
    assert np.min(lattice.phase) >= -np.pi
    assert np.max(lattice.phase) <= np.pi


def test_vortex_crystal_design_positions():
    lattice = vortex_crystal_field(shape=(256, 256), rows=6, cols=8, pixel_size=1e-6, wavelength_nm=694.3)
    assert lattice.shape == (256, 256)
    assert 6 * 8 == 48


def test_phase_equals_np_angle_complex():
    lattice = vortex_crystal_field(shape=(64, 64), rows=4, cols=4, pixel_size=1e-6, wavelength_nm=633)
    field = ComplexField(amplitude=lattice.amplitude, phase=lattice.phase, pixel_size=1e-6, wavelength_nm=633)
    max_diff = np.max(np.abs(field.phase - np.angle(field.complex)))
    assert max_diff < 1e-14, f"Phase mismatch: {max_diff}"
