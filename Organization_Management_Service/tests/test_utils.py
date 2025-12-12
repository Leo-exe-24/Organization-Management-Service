import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import utils

def test_hash_and_verify_short():
    pw = "pass123!"
    h = utils.hash_password(pw)
    assert utils.verify_password(pw, h)

def test_long_password_multibyte():
    pw = "あ" * 200
    h = utils.hash_password(pw)
    assert utils.verify_password(pw, h)
