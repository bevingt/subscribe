import base64
import re
import json
# from get_freev2ray import freev2ray
# from get_ishadow import ishadow
# from get_youneed import main as youneed
# from get_netlify import distinguishTheAgreement,netlify
# from get_free_ss import main as freess


def list_duplicate(data):
    new_list = [list(t) for t in set(tuple(_) for _ in data)]
    new_list.sort(key=data.index)
    return new_list

def str_duplicate(data):
    new_s = list(set(data))  # set无序
    new_s.sort(key=data.index)
    return new_s

def screening(s):
    ss_scr=[]
    ssr_scr=[]
    v2ray_scr=[]
    trojan_scr=[]
    for i in s:
        if i.find('ss://') == 0:
            ss_scr.append(base64.b64decode(re.findall('ss://(.*?)#.*',i)[0]).decode())
        elif i.find('ssr://') == 0:
            enssr=base64.b64decode(i[6:]).decode()
            ssr=enssr.split('/')[0]
            ssr_scr.append(ssr)
        elif i.find('vmess://') == 0:
            env2ray=base64.b64decode(i[8:]).decode()
            v2_json=json.loads(env2ray)
            try:
                v2_json.pop('v')
                v2_json.pop('ps')
                v2_json.pop('remark')
                v2_json.pop('')
            except KeyError:
                v2ray_scr.append(v2_json)
                # continue
            v2ray_scr.append(v2_json)
        elif i.find('trojan://') == 0:
            trojan_scr.append(re.findall('trojan://(.*?)#.*',i))
        else:
            continue
    return ss_scr,ssr_scr,v2ray_scr,trojan_scr

# def summary():
#     netlify_ss, netlify_ssr, netlify_v2, netlify_tro=distinguishTheAgreement(netlify())
#     youneed_ss=youneed('ss')
#     free_ss=freess()
#     free_v2=freev2ray()
#     ishadow_v2=ishadow()
#     youneed_v2=youneed('v2ray')
#     youneed_ssr= youneed('ssr')
#     alldata=youneed_ss+netlify_ss+free_ss+free_v2+ishadow_v2+youneed_v2+netlify_v2+youneed_ssr+netlify_ssr+netlify_tro
#     result=screening(alldata)
#     print(result)

if __name__ == "__main__":
    # ss=['ss://cmM0LW1kNTpsbmNuLm9yZyBkNWZANDYuMTcuNDUuMTU4Ojk3MTA=#WWW.YOUNEED.WIN']
    # ssr=['ssr://NDYuMTcuNDUuMTU4Ojk3MTA6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2daRFZtLz9vYmZzcGFyYW09VjFkWExsbFBWVTVGUlVRdVYwbE8mcHJvdG9wYXJhbT1WMWRYTGxsUFZVNUZSVVF1VjBsTyZyZW1hcmtzPVYxZFhMbGxQVlU1RlJVUXVWMGxPJmdyb3VwPVYxZFhMbGxQVlU1RlJVUXVWMGxP']
    # v2ray=['vmess://eyJ2IjoiMiIsInBzIjoid3d3LnlvdW5lZWQud2luIiwiYWRkIjoiMTA0LjE5LjQ3LjE0NyIsInBvcnQiOiI0NDMiLCJpZCI6IjMxMWU5NjhjLTAzOGUtMTFlYi1iNzAwLTUxMmYzNWUzOWUxMSIsImFpZCI6IjE2IiwibmV0Ijoid3MiLCJ0eXBlIjoibm9uZSIsImhvc3QiOiJ2Mi5rZHBkLm1lIiwicGF0aCI6Ii9IOVNNdHkzTy8iLCJ0bHMiOiJ0bHMifQ==']
    # trojan=['trojan://5a2d9c00-6e55-466e-bf61-262a08b02318@trotro.ml:443#%E4%BA%8C%E7%88%B7%E5%85%8D%E8%B4%B9%E7%BF%BB%E5%A2%99%E7%BD%91https%3A%2F%2F5414.ml']
    # a=screening(trojan)
    # print(a)
    summary()