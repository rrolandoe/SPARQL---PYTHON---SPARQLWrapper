"""
Tomado como referencia de la siguiente pag.
http://sparql-wrapper.sourceforge.net/

@reroes
"""
from SPARQLWrapper import SPARQLWrapper, JSON
import sys

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/%s> rdfs:label ?label }
"""%sys.argv[1])
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])
