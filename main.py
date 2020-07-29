from spider.spider import Spider

def main():
    url = "https://www.indiarace.com/Home/racingCenterEvent?venueId=1&event_date=2020-03-04&race_type=RESULTS"
    spider = Spider()
    soup = spider.fetch(url)
    # print(containerDiv)

    eventInfo = spider.getEventInfo(url, soup)
    # print(eventInfo)
    races = spider.getRaces(soup)
    #print(races)
    spider.getRacesDetail(races)


if __name__ == "__main__":
    main()