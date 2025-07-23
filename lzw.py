S_BITS = 7
M_BITS = 12

def compress(data):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    n_bits = S_BITS
    dsm = 2**n_bits
    w = ""
    result = []

    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            if w != "":
                result.append(dictionary[w])
            if dict_size < dsm:
                dictionary[wc] = dict_size
                dict_size += 1
            else:
                if n_bits < M_BITS:
                    n_bits += 1
                    dsm = 2 ** n_bits
                    dictionary[wc] = dict_size
                    dict_size += 1
                else:
                    pass
            w = c

    if w:
        result.append(dictionary[w])

    return result, n_bits

def decompress(compressed):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    result = []
    n_bits = S_BITS
    dsm = 2**n_bits

    w = chr(compressed[0])
    result.append(w)

    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result.append(entry)

        if dict_size < dsm:
            dictionary[dict_size] = w + entry[0]
            dict_size += 1
        else:
            if n_bits < M_BITS:
                n_bits += 1
                dsm = 2 ** n_bits
                dictionary[dict_size] = w + entry[0]
                dict_size += 1
            else:
                pass
        w = entry

    return ''.join(result)

