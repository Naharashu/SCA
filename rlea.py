def rle_encode(text):
    if not text:
        return ""

    result = ""
    count = 1
    prev = text[0]

    for char in text[1:]:
        if char == prev:
            count += 1
        else:
            result += prev + (str(count) if count > 1 else "")
            prev = char
            count = 1
    result += prev + (str(count) if count > 1 else "")
    return result

def rle_decode(encoded):
    
    result = ""
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        result += char * (int(count) if count else 1)
    return result

