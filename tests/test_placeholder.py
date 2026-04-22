"""Placeholder test — ensures CI passes until real tests are written."""
import pen_core


def test_version():
    """Verify package has a version attribute."""
    assert hasattr(pen_core, "__version__")
    assert pen_core.__version__ == "0.0.1"
