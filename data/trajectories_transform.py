######################################
#
# (Python version 3)
#
# Usage : python trajectories_transform.py florian.json > florian-dhlab.json
#
######################################

import sys, json
from dateutil.parser import parse

# global vars
dhlab_nodes = []
dhlab_links = []

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

# create dh_lab nodes based on original nodes, with empty years,
# add also 'index' field for finding node when creating links
for n in data["nodes"]:
    dn = {
        "name": n["name"],
        "index": data["nodes"].index(n),
        "year": set()
    }
    dhlab_nodes.append(dn)

# iterate through links in original format
for l in data["links"]:

    # create set of years where source and target are present for this link
    indate  = parse(l["inserteddate"]).year
    outdate = parse(l["deleteddate"]).year
    years = range(indate,outdate+1)

    # find source and target node of the link, put them in a list
    nodes = list(filter(lambda n: n["index"] == l["source"] or n["index"] == l["target"], dhlab_nodes))

    # for source and target nodes, append years of this link to already existing set of years
    for n in nodes:
        n["year"] = n["year"].union(set(years))

    # for each year, create a link between source and target and put in dhlab_links
    for y in years:
        dl = {
            "source": nodes[0]["index"],
            "target": nodes[1]["index"],
            "value": 1,
            "year": y
        }
        dhlab_links.append(dl)

# converts nodes set to sorted lists
for n in dhlab_nodes:
    n["year"] = sorted(list(n["year"]))

# create final structure and print it
dh_data = {
    "nodes": dhlab_nodes,
    "links": dhlab_links
}
print(json.dumps(dh_data, indent=2, separators=(',', ': ')))