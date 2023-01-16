import ctypes as ct 
from typing import Tuple
import numpy as np
from posixpath import exists, abspath
SO_PATH: str = abspath("../libZodiak.so")
assert exists(SO_PATH), "Use `make lib` to generate shared library object !"
SO_LIB: ct.CDLL = ct.CDLL(SO_PATH)
u8 = np.uint8
len_t = ct.c_size_t
uint8_tp = np.ctypeslib.ndpointer(dtype=u8, ndim=1, flags="CONTAGIOUS")
bool_t = ct.c_bool
def hash(msg: bytes) -> bytes:
    m_len = len(msg)
    msg_ = np.frombuffer(msg, dtype=u8)
    digest = np.empty(32, dtype=u8)
    args = [uint8_tp, len_t, uint8_tp]
    SO_LIB.hash.argtypes = args
    SO_LIB.hash(msg_, m_len, digest)
    digest_ = digest.tobytes()
    return digest_
def encrypt(key: bytes, nonce: bytes, text: bytes) -> Tuple[bytes, bytes]:
    k_len = len(key)
    n_len = len(nonce)
    d_len = len(data)
    t_len = len(text)
    assert k_len == 16, " Zodiak AEAD takes 16 -bytes secret key"
    assert n_len == 16, " Zodiak AEAD takes 16 -bytes nonce"
    key_ = np.frombuffer(key, dtype=u8)
    nonce_ = np.frombuffer(nonce, dtype=u8)
    data_ = np.frombuffer(data, dtype=u8)
    text_ = np.frombuffer(text, dtype=u8)
    enc = np.empty(t_len, dtype=u8)
    tag = np.empty(16, dtype=u8)
    args = [uint8_tp, uint8_tp, uint8_tp, len_t, uint8_tp]
    SO_LIB.encrypt.argtypes = args
    SO_LIB.encrypt(key_, nonce_, data_, d_len, text_, enc, t_len, tag)
    enc_ = enc.tobytes()
    tag_ = tag.tobytes()
    return enc_, tag_
def decrypt(
    key: bytes, nonce: bytes, 
)