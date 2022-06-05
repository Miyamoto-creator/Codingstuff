def past(h, m, s):
    h_count, m_count, s_count = 0, 0, 0
    while True:
        if h > 0:
            h_count += 3600 * 1000
            h -= 1
        elif m > 0:
            m_count += 60 * 1000
            m -= 1
        elif s > 0:
            s_count += 1 * 1000
            s -= 1
        else:
            break
    return (h_count + m_count + s_count)

