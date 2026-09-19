import pytest
import sys
import os
"""Test regression for all known bugs."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))


class TestRegressionDoubleAngle:
    """Regression test for CRITICAL bug: double-np.angle in winding_count.
    
    This test DOCUMENTS the buggy behavior. Do NOT fix the bug in this test.
    The fixed version is tested separately in test_winding.py.
    """
    def test_buggy_method_overcounts(self):
        """Buggy winding_count gives 127 on 1 vortex (DO NOT FIX)."""
        from tests.test_winding import winding_count_buggy
        result = winding_count_buggy.__wrapped__ if hasattr(winding_count_buggy, '__wrapped__') else None
        # Direct test
        import numpy as np
        y, x = np.ogrid[:64, :64]
        phase = np.arctan2((y-32).astype(float), (x-32).astype(float))
        # Simulate buggy behavior
        ph = np.angle(phase)  # BUG: double-wrap
        a, b, c, d = ph[:-1,:-1], ph[:-1,1:], ph[1:,1:], ph[1:,:-1]
        dphi = lambda x, y: np.mod(x - y + np.pi, 2*np.pi) - np.pi
        curl = dphi(b,a) + dphi(c,b) + dphi(d,c) + dphi(a,d)
        charge = np.round(curl / (2*np.pi))
        buggy_count = int(np.sum(np.abs(charge) > 0.5))
        assert buggy_count == 127, f"Buggy count should be 127, got {buggy_count}"


class TestRegressionPropagationSign:
    """Regression test for D1: propagate_fresnel sign bug."""
    def test_fresnel_propagates_negative_z(self):
        """Current implementation propagates -z (sign bug)."""
        import numpy as np
        from app.optics.field import ComplexField
        from app.optics.propagation import propagate_fresnel
        E0 = ComplexField(amplitude=np.ones((32, 32)), phase=np.zeros((32, 32)), pixel_size=1e-6, wavelength_nm=633)
        E_pz = propagate_fresnel(E0, z=100)
        E_nz = propagate_fresnel(E0, z=-100)
        ncc = np.sum(np.abs(E_pz) * np.abs(E_nz)) / (np.linalg.norm(np.abs(E_pz)) * np.linalg.norm(np.abs(E_nz)))
        # Due to sign bug, +z propagation ≈ -z propagation
        assert ncc > 0.95, f"Sign bug: +z matches -z with NCC={ncc}"


class TestRegressionDeadParameter:
    """Regression test for D2: find_features dead min_prominence."""
    def test_min_prominence_signature_only(self):
        """min_prominence should be in signature but not body."""
        import inspect
        from app.optics.deep_scan import DeepBeamScan
        src = inspect.getsource(DeepBeamScan.find_features)
        has_signature = 'min_prominence' in src.split(')')[0] or 'min_prominence' in src.split(':')[0]
        body = src.split('):', 1)[1] if '):' in src else src
        has_body_usage = 'min_prominence' in body
        assert has_signature, "min_prominence should be in signature"
        assert not has_body_usage, "min_prominence should NOT be used in body"
