def encrypt(text,key):
    byte_key = bytes(key,"ascii")
    byte_text = bytes(text,"ascii")
    enc_text = bytearray(len(byte_text))
    for index,value in enumerate(byte_text):
        enc_text[index] = value ^ byte_key[index%16]
    return enc_text.decode()
            
def format_pass(key):
    if len(key)<16:
        key = key + ("*"*(16-len(key)))
    else:
        key = key[0:16]
    return key


