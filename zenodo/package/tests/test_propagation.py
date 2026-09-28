import numpy as np
import pytest
import sys, os
"""Test propagation: ASM, Fresnel, reversibility, FFT conventions."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))

from app.optics.field import ComplexField
from app.optics.propagation import propagate_fresnel, propagate_angular_spectrum


def test_asm_reversibility():
    lattice = np.random.uniform(-np.pi, np.pi, (32, 32))
    E0 = ComplexField(amplitude=np.ones((32, 32)), phase=lattice, pixel_size=1e-6, wavelength_nm=633)
    E_fwd = propagate_angular_spectrum(np.exp(1j * E0.phase), z_um=100)
    E_rev = propagate_angular_spectrum(np.exp(1j * np.angle(E_fwd)), z_um=-100)
    ncc = np.sum(np.abs(E_rev) * np.abs(E0)) / (np.linalg.norm(np.abs(E_rev)) * np.linalg.norm(np.abs(E0)))
    assert ncc > 0.99, f"ASM reversibility NCC={ncc}"


def test_fresnel_sign_known_bug():
    lattice = np.random.uniform(-np.pi, np.pi, (32, 32))
    E0 = ComplexField(amplitude=np.ones((32, 32)), phase=lattice, pixel_size=1e-6, wavelength_nm=633)
    E_pz = propagate_fresnel(E0, z=100)
    E_nz = propagate_fresnel(E0, z=-100)
    ncc_pz_negz = np.sum(np.abs(E_pz) * np.abs(E_nz)) / (np.linalg.norm(np.abs(E_pz)) * np.linalg.norm(np.abs(E_nz)))
    assert ncc_pz_negz > 0.95, f"Fresnel +z matches -z (sign bug): NCC={ncc_pz_negz}"


def test_fft_convention():
    test_array = np.random.randn(8, 8) + 1j * np.random.randn(8, 8)
    fft_result = np.fft.fft2(test_array)
    ifft_result = np.fft.ifft2(fft_result)
    max_diff = np.max(np.abs(ifft_result - test_array))
    assert max_diff < 1e-14, f"FFT convention mismatch: {max_diff}"


def test_propagation_dimensions_preserved():
    E0 = ComplexField(amplitude=np.ones((32, 32)), phase=np.zeros((32, 32)), pixel_size=1e-6, wavelength_nm=633)
    E_z = propagate_fresnel(E0, z=100)
    assert E_z.amplitude.shape == (32, 32)
    assert E_z.phase.shape == (32, 32)
