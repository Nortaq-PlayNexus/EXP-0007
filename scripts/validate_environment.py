"""Validate the runtime environment for EXP-0007."""
import sys
import os

def validate():
    errors = []
    
    # Python version
    if sys.version_info < (3, 10):
        errors.append(f"Python >= 3.10 required, got {sys.version}")
    
    # Required packages
    required = [
        ("numpy", "1.24"),
        ("scipy", "1.11"),
        ("matplotlib", "3.7"),
    ]
    
    for name, min_ver in required:
        try:
            mod = __import__(name)
            from packaging.version import Version
            if Version(mod.__version__) < Version(min_ver):
                errors.append(f"{name} >= {min_ver} required, got {mod.__version__}")
        except ImportError:
            errors.append(f"{name} not installed")
        except Exception as e:
            pass  # packaging might not be available, just check it exists
    
    if errors:
        print("ENVIRONMENT VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("ENVIRONMENT VALIDATED: All requirements met")
        return True


if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
