import base64
import re

def clash(data):
    clash_list = []
    for arr in data:  # 清理不适用clash的SS加密方式
        ss_link = re.findall('ss://(.*?)#.*', arr)
        sl_decode = base64.b64decode(''.join(ss_link)).decode()
        if sl_decode.split(':')[0] == 'chacha20':
            continue
        else:
            clash_list.append(arr)
    return clash_list