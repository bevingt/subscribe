from code.get_freev2ray import freev2ray
from code.get_ishadow import ishadow
from code.get_youneed import main as youneed
from code.get_netlify import distinguishTheAgreement,netlify
from code.get_free_ss import main as freess
from code.screeningClashAvailable import clash
from code.transcoding import base64_encode
from code.timeFormat import timeFormat

def ss_sub(ssToSubscribe):
    sub_addr = base64_encode(merge(ssToSubscribe))
    savefile('ss-sub.txt',sub_addr)
    clash_sub=clash(ssToSubscribe)
    removeTheProtocolIsNotAvailable = base64_encode(merge(clash_sub))
    savefile('ss_removeTheProtocolIsNotAvailable.txt',removeTheProtocolIsNotAvailable)


def v2ray_sub(v2ToSubscribe):
    sub_addr = base64_encode(merge(v2ToSubscribe))
    savefile('v2ray-sub.txt',sub_addr)    

def ssr_sub(ssrToSubscribe):
    sub_addr = base64_encode(merge(ssrToSubscribe))
    savefile('ssr-sub.txt',sub_addr)

def trojan_sub(trojanToSubscribe):
    sub_addr = base64_encode(merge(trojanToSubscribe))
    savefile('trojan-sub.txt',sub_addr)

def all_sub(allToSubscribe):
    sub_addr = base64_encode(merge(allToSubscribe))
    savefile('list.txt',sub_addr)

def merge(data):
    join_result = '\n'.join(data)
    return join_result


def savefile(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print(timeFormat(), filename+'_保存成功')

def main():
    netlify_ss, netlify_ssr, netlify_v2, netlify_tro=distinguishTheAgreement(netlify())
    youneed_ss=youneed('ss')
    # netlify_ss=netlify('ss')
    free_ss=freess()
    free_v2=freev2ray()
    ishadow_v2=ishadow()
    youneed_v2=youneed('v2ray')
    # netlify_v2=netlify('v2ray')
    youneed_ssr= youneed('ssr')
    # netlefy_tro= netlify('trojan')
    ss_sub(youneed_ss+netlify_ss+free_ss)
    v2ray_sub(free_v2+ishadow_v2+youneed_v2+netlify_v2)
    ssr_sub(youneed_ssr+netlify_ssr)
    trojan_sub(netlify_tro)
    all_sub(youneed_ss+netlify_ss+free_ss+free_v2+ishadow_v2+youneed_v2+netlify_v2+youneed_ssr+netlify_ssr+netlify_tro)


if __name__ == "__main__":
    main()