import numpy as np

from .core import round_pow2


def back_padding(xs: np.ndarray, n: int, a) -> np.ndarray:
    """n個の要素になるように後ろをaで埋める
    
    Arguments:
        xs (np.ndarray[shape=(m,)]): 配列
        n (int > m): 要素数
        a (xs.dtype): 埋める値

    Returns:
        np.ndarray[shape=(n,)]: 余分なところをaで埋めた配列
    """

    
    if len(xs.shape) > 1:
        raise ValueError("配列xsは一次元配列である必要があります。")

    if xs.shape[0] > n:
        raise ValueError("nは配列xsの要素数より大きい必要があります。")

    if xs.dtype != type(a):
        raise ValueError("aの型は配列xsの要素の型と一致している必要があります。")
    
    v = np.ones(n, dtype=type(a)) * a
    v[:xs.shape[0]] = xs
    return v


def to_pow2_length(xs: np.ndarray, a) -> np.ndarray:
    """要素数が2のべき乗になるように後ろをaで埋める
    
    Arguments:
        xs (np.ndarray[shape=(n,)]): 一次元配列
        a (xs.dtype): 埋める値

    Returns:
        np.ndarray[shape=(2**p,)]: 要素数が2のべき乗で後ろがaで埋まった配列
    """

    return back_padding(xs, round_pow2(xs.shape[0]), a)
