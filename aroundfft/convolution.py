import numpy as np

from .array import to_pow2_length, back_padding


def convolve(f, g):
    """高速フーリエ変換を使った畳み込み"""

    if len(f) < len(g):
        f, g = g, f

    original_f = len(f)
    original_g = len(g)

    zero = 0 if f.dtype == int else 0.

    f = to_pow2_length(f, zero)
    g = back_padding(g, len(f), zero)
    
    ffted_f = np.fft.fft(f)
    ffted_g = np.fft.fft(g)

    conv = ffted_f * ffted_g
    
    return np.abs(np.fft.ifft(conv)[:original_f + original_g - 1])
