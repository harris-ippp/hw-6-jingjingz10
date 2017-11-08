import requests
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    year=line.split()
    link = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(year[1])
    resp = requests.get(link)
    soup = BeautifulSoup(resp.content, "html.parser")
    file_name = "president_general_"+ year[0] +".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
