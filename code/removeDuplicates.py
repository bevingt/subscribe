import base64
import re

def list_duplicate(data):
    new_list = [list(t) for t in set(tuple(_) for _ in data)]
    new_list.sort(key=data.index)
    return new_list

def str_duplicate(data):
    new_s = list(set(data))  # set无序
    new_s.sort(key=data.index)
    return new_s

def screening(s):
    scre=[]
    for i in s:
        if i.find('ss://') == 0:
            scre.append(base64.b64decode((re.findall('ss://(.*?)#.*',i)[0])).decode())
        elif i.find('ssr://') == 0:
            scre.append(base64.b64decode((re.findall('ssr://(.*?)#.*',i)[0])).decode())
        elif i.find('vmess://') == 0:
            a=re.findall('vmess://(.*?)',i)
            print(a)
            # b=base64.b64decode(a).decode()
            # print(b)
            # scre.append(base64.b64decode((re.findall('vmess://(.*?)',i)[0])).decode())
        elif i.find('trojan://') == 0:
            scre.append(re.findall('trojan://(.*?)#.*',i))
        else:
            continue
    return scre

# if __name__ == "__main__":