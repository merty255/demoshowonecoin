import urllib

from streamlit_agraph import agraph, Node, Edge, Config

from helpfunktions import namespace, getresult, cutpraefixe

import streamlit as st

st.set_page_config(
    page_title='Demo',

)

st.write("Hier werden zwei Verknüpfte Datensätze dargestellt")

coinscounter = 0

rests = []
nodes = []
edges = []

hashmap ={} # enthält coinsname fuer objekte

def generatesnode(coinscounter, coinurlasstring):
    coinscounter = coinscounter+1
    testquery = namespace + " select * where { <"+coinurlasstring+"> ?p ?o}   "
    nodes.append(Node(id="COIN" + str(coinscounter),
                      label="COIN",
                      size=155,
                      )
                 )

    c = len(nodes)

    safe_string = urllib.parse.quote_plus(testquery)
    safe_string = safe_string.replace("%2A", "*")
    result1 = getresult( safe_string + "&output=json")
    for r in result1:
        c = c + 1
        object = r['o']['value']
        p = r['p']['value']
        object = cutpraefixe(object)
        idobjectnode = ""
        if object  not in hashmap:
            idobjectnode = "COINnode" + str(c)
            nodes.append(Node(id=idobjectnode,
                              label=object,
                              size=155)
                         )
            hashmap[object] = idobjectnode
        else:
            idobjectnode=  hashmap[object]

        p = cutpraefixe(p)

        edges.append(Edge(id="Edge" + str(c),
                          label=p,
                          source="COIN" + str(coinscounter),
                          target=idobjectnode,
                          type="STRAIGHT")
                     )
    return coinscounter




coinscounter = generatesnode(coinscounter, "https://www.corpus-nummorum.eu/coins/23106")






config = Config(width=1200,
                height=400,
                directed=True,
                nodeHighlightBehavior=True,
                highlightColor="#F7A7A6", # or "blue"
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                # **kwargs e.g. node_size=1000 or node_color="blue"
                )


return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)

st.write("Daten von :")
st.write("https://www.corpus-nummorum.eu/coins/23106")

if __name__ == '__main__':

    pass

