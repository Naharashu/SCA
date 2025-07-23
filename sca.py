import lzw, rlea

def compress(data):
    rle_encoded = rlea.rle_encode(data)
    encoded = lzw.compress(rle_encoded)
    return encoded

def decompress(encoded):
    decoded_lzw = lzw.decompress(encoded)
    final_result = rlea.rle_decode(decoded_lzw)
    return final_result

data = "Hello, my name is Dabbian, ABCDDDERD!"

# Стиснення
encoded, n_bits = compress(data)
print("SCA Encoded:", encoded)
print(f"LZW encoded: {lzw.compress(data)[0]}")

# Розпакування
decompressed = decompress(encoded)

print(len(encoded))
print(len(data))
print("Decompressed:", decompressed)