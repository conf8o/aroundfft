def round_pow2(x :int) -> int:
    """xを2のべき乗に切り上げる
    
    例)
    60 -> 64
    40000 -> 65536

    Arguments:
        x (int > 0): 正の整数

    Returns:
        int: 2のべき乗の整数
    """
    
    if x < 1:
        raise ValueError("xは正の整数である必要があります。")

    return 1 << x.bit_length()
