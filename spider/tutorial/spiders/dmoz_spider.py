import scrapy
import json
from tutorial.items import AppStoreItem

class AppstoreSpider(scrapy.Spider):
    name = "ios"
    allowed_domains = ["itunes.apple.com"]
    start_urls = []
    start = 0
    for i in range(10,12):
        end = start + 100
        endString = '%d' % end
        startString = '%d' % start
        start = end + 1
        url1 = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=895682747&displayable-kind=11&startIndex=%s&endIndex=%s&sort=1&appVersion=all" % (startString,endString)
        url2 = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=895682747&displayable-kind=11&startIndex=%s&endIndex=%s&sort=1&appVersion=current" % (startString,endString)
        start_urls.append(url1)
        start_urls.append(url2)

    def start_requests(self):

        headers = {
            "Host": "itunes.apple.com",
            "X-Apple-Tz": "28800",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "X-Apple-Store-Front": "143465-19,32",
            "Proxy-Connection": "keep-alive",
            "If-Modified-Since": "Mon, 30 Oct 2017 05:09:14 GMT",
            "Accept-Language": "zh-Hans;q=1.0, en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "X-Apple-I-MD-RINFO": "17106176",
            "X-Apple-I-MD-M": "4yta1gxLU2/1yorU7oVB982KDbxQfTgDNV0Kx6rMh83dcH6GSFvvMX4j2xTK1pydINZyrdPRmrAqnMrx",
            "User-Agent": "iTunes/12.5.5 (Macintosh; OS X 10.11.6) AppleWebKit/601.7.7",
            "X-Apple-I-Client-Time": "2017-10-30T06:38:41Z",
            "Referer": "https://itunes.apple.com/cn/app/%E4%BA%AC%E4%B8%9C%E9%87%91%E8%9E%8D-%E6%96%B0%E4%BA%BA%E9%A2%86666%E5%85%83%E5%A4%A7%E7%A4%BC%E5%8C%85/id895682747?mt=8",
            "X-Apple-I-MD": "AAAABQAAABB/8E70ajsA2bpSsQneRzRzAAAAAQ==",
            "X-Dsid": "1851386458",
            "Cookie": "groupingPillToken=1_iphone; mt-asn-1851386458=5; mt-asn-1952598692=5; mt-tkn-1851386458=AquPBN7pBVJrtDMwCG1MrwviP60xe4f/EE45hsAOovLfR/ovUuHxcsKrlj2pxor0U9F3HIkuroemH+0MuFQnpjqUFC4oYoymULT5CpIKnJ3VpDni/Y/moZel5PjbSHG4GD+Ijl5r7uyk/NbjAbcP2c6m643pr8/RJ8pEGPfTmpVhsZJWGga7Uku1jMcsYZwUcq4thww=; mt-tkn-1952598692=AmPsxyX+Zm3hcSBdOCr1LAg942a/+QI1OZsorJ+0WD2wkyUHZ6Dv3jDaRipaZfgo7xzHgpeVUdtG70RFfh0FA5pOHGZGJ/5b/MiFc4VGex0OtgQ9XasD8i89/gI1Ai21Fi7kJkngVal3DewE6NPKYC8difiYN7R7wY/nH/Z3bcgGM9wio22SK/ZdDyrs38XhS717EKw=; X-Dsid=1851386458; itspod=24; mz_at0-1851386458=AwQAAAEBAAHWuQAAAABZo5zH8UZyjuA18kRtUGbvu8lLlA89jpk=; mz_at0-1952598692=AwQAAAEBAAHWUwAAAABX91VVP4AXK30/tKDBEUr2V9fwfUERl9A=; mz_at_ssl-1851386458=AwUAAAEBAAHWUwAAAABYFwZni0EdGJhw1mXiPHOZnkeCs8m3DaU=; mz_at_ssl-1952598692=AwUAAAEBAAHWUQAAAABXfIMB4QjT3cNSHm+BuLBHSWqkz1Ndd0g=; s_vi=[CS]v1|2B45BA5205011739-600001038013C541[CE]; xp_ab=1#isj11bm+3579+17Eg4xa0; xp_abc=17Eg4xa0; xp_ci=3z34ZpILzCUZz4Vrz9pTzlq8yrxrJ",
            "iCloud-DSID": "1851386458"
        }
        for url in self.start_urls:
            yield scrapy.Request(url,
                                   headers=headers,
                                       callback=self.parse)


    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        siteitems = sites['userReviewList']
        for item in siteitems:
            appStoreItem = AppStoreItem()
            appStoreItem['userReviewId'] = item['userReviewId'].encode("utf-8")
            appStoreItem['body'] = item['body'].encode("utf-8")
            dateString = item['date'].encode("utf-8")
            dateStringList = dateString.split('T')
            date = dateStringList[0]
            time = dateStringList[1]
            appStoreItem['date'] = date
            appStoreItem['time'] = time
            appStoreItem['name'] = item['name'].encode("utf-8")
            appStoreItem['rating'] = item['rating']
            appStoreItem['title'] = item['title'].encode("utf-8")
            yield appStoreItem


class AndroidSpider(scrapy.Spider):
    name = "andorid"
    allowed_domains = ["itunes.apple.com"]
    start_urls = []
    start = 0
    for i in range(0,2):
        end = start + 100
        endString = '%d' % end
        startString = '%d' % start
        start = end + 1
        url1 = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=895682747&displayable-kind=11&startIndex=%s&endIndex=%s&sort=1&appVersion=all" % (startString,endString)
        url2 = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=895682747&displayable-kind=11&startIndex=%s&endIndex=%s&sort=1&appVersion=current" % (startString,endString)
        start_urls.append(url1)
        start_urls.append(url2)

    def start_requests(self):

        headers = {
            "Host": "itunes.apple.com",
            "X-Apple-Tz": "28800",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "X-Apple-Store-Front": "143465-19,32",
            "Proxy-Connection": "keep-alive",
            "If-Modified-Since": "Mon, 30 Oct 2017 05:09:14 GMT",
            "Accept-Language": "zh-Hans;q=1.0, en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "X-Apple-I-MD-RINFO": "17106176",
            "X-Apple-I-MD-M": "4yta1gxLU2/1yorU7oVB982KDbxQfTgDNV0Kx6rMh83dcH6GSFvvMX4j2xTK1pydINZyrdPRmrAqnMrx",
            "User-Agent": "iTunes/12.5.5 (Macintosh; OS X 10.11.6) AppleWebKit/601.7.7",
            "X-Apple-I-Client-Time": "2017-10-30T06:38:41Z",
            "Referer": "https://itunes.apple.com/cn/app/%E4%BA%AC%E4%B8%9C%E9%87%91%E8%9E%8D-%E6%96%B0%E4%BA%BA%E9%A2%86666%E5%85%83%E5%A4%A7%E7%A4%BC%E5%8C%85/id895682747?mt=8",
            "X-Apple-I-MD": "AAAABQAAABB/8E70ajsA2bpSsQneRzRzAAAAAQ==",
            "X-Dsid": "1851386458",
            "Cookie": "groupingPillToken=1_iphone; mt-asn-1851386458=5; mt-asn-1952598692=5; mt-tkn-1851386458=AquPBN7pBVJrtDMwCG1MrwviP60xe4f/EE45hsAOovLfR/ovUuHxcsKrlj2pxor0U9F3HIkuroemH+0MuFQnpjqUFC4oYoymULT5CpIKnJ3VpDni/Y/moZel5PjbSHG4GD+Ijl5r7uyk/NbjAbcP2c6m643pr8/RJ8pEGPfTmpVhsZJWGga7Uku1jMcsYZwUcq4thww=; mt-tkn-1952598692=AmPsxyX+Zm3hcSBdOCr1LAg942a/+QI1OZsorJ+0WD2wkyUHZ6Dv3jDaRipaZfgo7xzHgpeVUdtG70RFfh0FA5pOHGZGJ/5b/MiFc4VGex0OtgQ9XasD8i89/gI1Ai21Fi7kJkngVal3DewE6NPKYC8difiYN7R7wY/nH/Z3bcgGM9wio22SK/ZdDyrs38XhS717EKw=; X-Dsid=1851386458; itspod=24; mz_at0-1851386458=AwQAAAEBAAHWuQAAAABZo5zH8UZyjuA18kRtUGbvu8lLlA89jpk=; mz_at0-1952598692=AwQAAAEBAAHWUwAAAABX91VVP4AXK30/tKDBEUr2V9fwfUERl9A=; mz_at_ssl-1851386458=AwUAAAEBAAHWUwAAAABYFwZni0EdGJhw1mXiPHOZnkeCs8m3DaU=; mz_at_ssl-1952598692=AwUAAAEBAAHWUQAAAABXfIMB4QjT3cNSHm+BuLBHSWqkz1Ndd0g=; s_vi=[CS]v1|2B45BA5205011739-600001038013C541[CE]; xp_ab=1#isj11bm+3579+17Eg4xa0; xp_abc=17Eg4xa0; xp_ci=3z34ZpILzCUZz4Vrz9pTzlq8yrxrJ",
            "iCloud-DSID": "1851386458"
        }
        print len(self.start_urls)
        for url in self.start_urls:
            yield scrapy.Request(url,
                                   headers=headers,
                                       callback=self.parse)

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        siteitems = sites['userReviewList']
        for item in siteitems:
            appStoreItem = AppStoreItem()
            appStoreItem['userReviewId'] = item['userReviewId'].encode("utf-8")
            appStoreItem['body'] = item['body'].encode("utf-8")
            dateString = item['date'].encode("utf-8")
            dateStringList = dateString.split('T')
            date = dateStringList[0]
            time = dateStringList[1]
            appStoreItem['date'] = date
            appStoreItem['time'] = time
            appStoreItem['name'] = item['name'].encode("utf-8")
            appStoreItem['rating'] = item['rating']
            appStoreItem['title'] = item['title'].encode("utf-8")
            yield appStoreItem

