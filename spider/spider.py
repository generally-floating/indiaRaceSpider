import sys
from bs4 import BeautifulSoup
import requests

from dataObject.eventInfo import EventInfo

class Spider:
    def fetch(self, url):
        r = requests.get(url) #Fetch HTML Page
        soup = BeautifulSoup(r.text, "html.parser") #Parse HTML Page
        # Finding all divs with class name container-fluid
        containerDivs = soup.findAll("div", {"class": "container-fluid"})
        # there are 3 divs with class name container-fluid, 
        # we want the last entry in containerDivs
        if len(containerDivs) != 3:
            sys.exit("containerDivs fetched are not equal to 3")
        return containerDivs[2] 

    def getEventInfo(self, url, soup):
        # print(url)
        queryString = url.split("?")[1]
        queryParams = queryString.split("&")
        venueId = queryParams[0].split("=")[1]
        eventDate = queryParams[1].split("=")[1]
        raceType = queryParams[2].split("=")[1]

        # print(venueId)
        # print(eventDate)
        # print(raceType)

        x = soup.findAll("div", {"class": "home"})
        y = x[0].findAll("h3")
        z = y[0].text.split("-")
        venueName = z[1].strip()
        # print(venueName)

        e = EventInfo(venueId, venueName, eventDate, raceType)
        # print(e)

    def getRaces(self, soup):
        races = list()
        for c in soup.children:
            # print("==================")
            # print(type(c))
            if c != "\n":
                # print(c)
                id = c.get('id')
                if id and ("race" in id): 
                    races.append(c)
        print("Number of Races: ", len(races))
        return races
 
    def getRacesDetail(self, races):
        for race in races:
            self.getRaceDetail(race)
            break #todo: remove when gerRaceDetail finishes
    
    # todo: continue here
    def getRaceDetail(self, race):
        # print("getRaceDetail")
        # print(race)
        self.getRaceInfo(race)
    
    # todo: start here
    def getRaceInfo(self, race):
        print("getRaceInfo")
        pass

        
        
    
#     def getRaces(self, soup):
#         print ("Fetch All Races:")
        
# #         mydivs = soup.findAll("div", {"class": "container-fluid"})
# #         print(mydivs)
#         #print(soup.find(class="container-fluid"))