import requests
from bs4 import BeautifulSoup

link = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"

resp = requests.get(link)
soup = BeautifulSoup(resp.content, "html.parser")

ID = soup.find_all("tr","election_item")

with open("ELECTION_ID","w") as out:
    for v in ID:
        v1 = v.find("td","year first").string
        v2 = v.get("id").replace("election-id-","")
        out.write("{} {}\n".format(v1,v2))
