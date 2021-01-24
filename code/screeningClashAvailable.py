import base64
import re

def clash(data):
    encryption=['aes-256-gcm','AES-256-GCM','aes-128-gcm','AES-128-GCM','chacha20-poly1305','ChaCha20-Poly1305','chacha20-ietf-poly1305','ChaCha20-IETF-Poly1305','none','plain']
    clash_list = []
    for arr in data:  # 清理不适用clash的SS加密方式
        ss_link = re.findall('ss://(.*?)#.*', arr)
        sl_decode = base64.b64decode(''.join(ss_link)).decode()
        if sl_decode.split(':')[0] not in encryption:
            continue
        else:
            clash_list.append(arr)
    return clash_list