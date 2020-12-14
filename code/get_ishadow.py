import requests
from requests.adapters import HTTPAdapter
from code.timeFormat import timeFormat
import parsel


def ishadow():  # https://my.ishadowx.biz
    session = requests.session()
    session.mount('https://', HTTPAdapter(max_retries=3))
    url = 'https://my.ishadowx.biz'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    resp = session.get(url=url, headers=header, timeout=10)
    data = parsel.Selector(resp.text)
    vmess = data.xpath(
        '//div[@class="hover-text"]/h4/span/@data-clipboard-text').extract()
    result = []
    for i in vmess:
        u = i[:-1]
        result.append(u)
    print(timeFormat(), '读取ishadow数据成功')
    print('-'*42)
    return result


if __name__ == "__main__":
    rep = ishadow()
    print(rep)
