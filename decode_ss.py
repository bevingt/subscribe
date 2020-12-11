import base64
import json
import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
import execjs
import requests
import re
import parsel
import time


def decrypt_data(key, iv, endata):
    ctr = Counter.new(128, initial_value=int(binascii.hexlify(iv), 16))
    # print(ctr)
    modes = [
        AES.new(key, AES.MODE_ECB),
        AES.new(key, AES.MODE_CBC, iv),
        AES.new(key, AES.MODE_OFB, iv),
        AES.new(key, AES.MODE_CTR, counter=ctr),
        AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    ]
    rtdatas = None
    for mode in modes:
        try:
            dec = mode.decrypt(endata).decode('utf-8')
            # print(dec[-200:])     # 解密后文本结尾可能存在'\0'
            dec = dec.rstrip('\0')  # 去除结尾空白符'\0'
            rtdatas = json.loads(dec)['data']
            break
        except:
            pass
    return rtdatas


def decode_c(c):
    # x = execjs.compile('''
    #     function encc(r){var n=str2bin(r),t=al(n,r.length),o=new Array(8);o[0]=1937774191,o[1]=1226093241,o[2]=388252375,o[3]=3666478592,o[4]=2842636476,o[5]=372324522,o[6]=3817729613,o[7]=2969243214;for(var a=0;a<t;a++)o=zip(o,n,a);return word2str(o,"").substr(0,16)}function word2str(r,n){for(var t=Array(8).join("0"),o=0;o<r.length;o++)r[o]=(t+(r[o]>>>0).toString(16)).slice(-8);return r.join(n)}function str2bin(r){for(var n=new Array(r.length>>2),t=0;t<8*r.length;t+=8)n[t>>5]|=(255&r.charCodeAt(t/8))<<24-t%32;return n}function al(r,n){r[n>>2]|=128<<24-n%4*8;for(var t=1+(n+8>>6),o=16*t,a=1+(n>>2);a<o;a++)r[a]=0;return r[o-1]=8*n,t}function p0(r){return r^br(r,9)^br(r,17)}function p1(r){return r^br(r,15)^br(r,23)}function br(r,n){return r<<n|r>>>32-n}function zip(r,n,o){for(var a=new Array(68),u=new Array(64),f=0;f<68;f++)a[f]=f<16?n[16*o+f]:p1(a[f-16]^a[f-9]^br(a[f-3],15))^br(a[f-13],7)^a[f-6];for(f=0;f<64;f++)u[f]=a[f]^a[f+4];var e,i,c,b,v=r[0],g=r[1],l=r[2],d=r[3],s=r[4],h=r[5],p=r[6],w=r[7];for(f=0;f<64;f++)i=(e=br(aa(br(v,12),s,br(t(f),f)),7))^br(v,12),c=aa(ff(v,g,l,f),d,i,u[f]),b=aa(gg(s,h,p,f),w,e,a[f]),d=l,l=br(g,9),g=v,v=c,w=p,p=br(h,19),h=s,s=p0(b);return r[0]^=v,r[1]^=g,r[2]^=l,r[3]^=d,r[4]^=s,r[5]^=h,r[6]^=p,r[7]^=w,r}function t(r){return 0<=r&&r<16?2043430169:r<64?2055708042:void 0}function ff(r,n,t,o){return 0<=o&&o<16?r^n^t:o<64?r&n|r&t|n&t:void 0}function gg(r,n,t,o){return 0<=o&&o<16?r^n^t:o<64?r&n|~r&t:void 0}function sa(r,n){var t=(65535&r)+(65535&n);return(r>>16)+(n>>16)+(t>>16)<<16|65535&t}function aa(){for(var r=0,n=0;n<arguments.length;n++)r=sa(r,arguments[n]);return r}
    #    ''')

    with open('js/encc.js', encoding='utf-8') as f:
        js = f.read()
    x = execjs.compile(js)
    return x.call('encc', c)


def get_token():
    url = 'https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfEr5MUAAAAACiN9ZgH4842Va__LHuZTbX7ztl0&co=aHR0cHM6Ly9mcmVlLXNzLnNpdGU6NDQz&hl=zh-CN&v=qc5B-qjP0QEimFYUxcpWJy5B&size=invisible'
    resp = requests.get(url, timeout=10)
    if resp.status_code == 200:

        token = re.findall('value="(.*?)"', resp.text)
        return token
    else:
        print('连接失败，未获取token')


def getdata3(a, b, c, token):
    url_data = {
        'a': a,
        'b': b,
        'c': c,
        't': token
    }
    url = 'https://free-ss.site/data3.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    resp = requests.post(url=url, headers=headers, data=url_data, timeout=10)
    if resp.status_code == 200:
        return resp.text
    else:
        print('连接失败，未获取data3加密数据')
    # print(resp.text)


def get_key():
    url = 'https://free-ss.site'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers, timeout=10)
    if resp.status_code == 200:
        data = parsel.Selector(resp.text)
        js = data.xpath('//script').extract()[9]
        # key_list=re.findall('else{(.*?)}',js)
        key = re.findall("var [a-z]='(.*?)';", js)[3:]
        return key
    else:
        print('连接失败，未获取key值')
    # print(key)


def run():
    count = 1
    while count <= 2:
        keys = get_key()
        a = keys[0]
        b = keys[1]
        c = decode_c(keys[2])

        t = get_token()
        ss = getdata3(a, b, c, t)

        key = bytes(a, encoding="utf-8")
        iv = bytes(b, encoding="utf-8")
        endata = base64.b64decode(str(ss))
        ssdata = decrypt_data(key, iv, endata)
        if ssdata == None:
            count = 1
            time.sleep(1)
            print('data3数据未抓到，重试')
        else:
            count += 1
    # print(ssdata)
    ss_url = []
    for i in ssdata:
        ssurl = i[4]+':'+i[3]+'@'+i[1]+':'+i[2]
        base_ssurl = base64.b64encode(ssurl.encode())
        ss_url.append('ss://'+base_ssurl.decode("utf-8") +
                        '#'+i[6]+'_free-ss.site')

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '读取free-ss数据成功')
    print('-'*42)
    return ss_url


if __name__ == "__main__":
    run()

    # initial_value=int(binascii.hexlify(iv), 16)
