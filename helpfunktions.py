import requests

apiname =  "https://data.corpus-nummorum.eu/sparql?query="

def getresult(query):

    r32 = requests.get(apiname + query)
    j23 = r32.json()
    final = j23["results"]["bindings"]
    return final

def cutpraefixe(surl):
    # verkuertzt die uris zur besseren uebersicht
    surl = surl.replace( "http://www.cidoc-crm.org/cidoc-crm/","crm:" )
    surl = surl.replace( "http://purl.org/dc/terms/","dcterms:" )
    surl = surl.replace( "http://purl.org/dc/dcmitype/","dcmitype:" )
    surl = surl.replace( "http://xmlns.com/foaf/0.1/", "foa:f")
    surl = surl.replace("http://www.w3.org/2003/01/geo/wgs84_pos#", "geo:" )
    surl = surl.replace( "http://nomisma.org/id/", "nm:")
    surl = surl.replace( "http://nomisma.org/ontology#","nmo:" )
    surl = surl.replace("http://www.w3.org/ns/org#","org:" )
    surl = surl.replace( "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:" )
    surl = surl.replace( "http://www.w3.org/2000/01/rdf-schema#", "rdfs:" )
    surl = surl.replace( "http://www.w3.org/2004/02/skos/core#","skos:" )
    surl = surl.replace( "http://www.w3.org/2001/XMLSchema#","xsd:" )
    return surl


namespace = """	
PREFIX crm:  <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX dcterms:  <http://purl.org/dc/terms/>
PREFIX dcmitype:  <http://purl.org/dc/dcmitype/>
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX geo:  <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX nm:  <http://nomisma.org/id/>
PREFIX nmo:  <http://nomisma.org/ontology#>
PREFIX org:  <http://www.w3.org/ns/org#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos:  <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
"""