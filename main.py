from code.get_freev2ray import freev2ray
from code.get_ishadow import ishadow
from code.get_youneed import main as youneed
from code.get_netlify import distinguishTheAgreement, netlify
from code.get_free_ss import main as freess
from code.screeningClashAvailable import clash
from code.transcoding import base64_encode
from code.timeFormat import timeFormat
from code.queryIpAttribution import testing

def ss_sub(ssToSubscribe):
    sub_addr = base64_encode(merge(ssToSubscribe))
    savefile('sub/ss-sub.txt', sub_addr)
    clash_sub = clash(ssToSubscribe)
    removeTheProtocolIsNotAvailable = base64_encode(merge(clash_sub))
    savefile('sub/ss_removeTheProtocolIsNotAvailable.txt',
             removeTheProtocolIsNotAvailable)


def v2ray_sub(v2ToSubscribe):
    sub_addr = base64_encode(merge(v2ToSubscribe))
    savefile('sub/v2ray-sub.txt', sub_addr)


def ssr_sub(ssrToSubscribe):
    sub_addr = base64_encode(merge(ssrToSubscribe))
    savefile('sub/ssr-sub.txt', sub_addr)


def trojan_sub(trojanToSubscribe):
    sub_addr = base64_encode(merge(trojanToSubscribe))
    savefile('sub/trojan-sub.txt', sub_addr)


def all_sub(allToSubscribe):
    sub_addr = base64_encode(merge(allToSubscribe))
    savefile('sub/all.txt', sub_addr)


def merge(data):
    join_result = '\n'.join(data)
    return join_result


def savefile(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print(timeFormat(), filename+'_保存成功')


def main():
    # netlify_ss, netlify_ssr, netlify_v2, netlify_tro = distinguishTheAgreement(
    #     netlify())
    netlify_v2=distinguishTheAgreement(netlify())[3]
    # youneed_ss = youneed('ss')
    # free_ss = freess()
    free_v2 = freev2ray()
    ishadow_v2 = ishadow()
    youneed_v2 = youneed('v2ray')
    # youneed_ssr = youneed('ssr')

    v2ray=free_v2+ishadow_v2+youneed_v2+netlify_v2
    # ss=youneed_ss+netlify_ss
    # ssr=youneed_ssr+netlify_ssr

    v2rayIPtesting=testing(v2ray)

    # if free_ss == None:
    #     ss_sub(ss)
    #     all_sub(v2rayIPtesting+ss+ssr+netlify_tro)
    # else:
    #     ss_sub(ss+free_ss)
    #     all_sub(ss+free_ss+v2rayIPtesting+ssr+netlify_tro)

    v2ray_sub(v2rayIPtesting)
    # ssr_sub(ssr)
    # trojan_sub(netlify_tro)
    


if __name__ == "__main__":
    main()
