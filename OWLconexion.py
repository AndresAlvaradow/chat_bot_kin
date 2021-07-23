from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    'http://localhost:3030/ds/sparql')


def get_response_pizzas():
    sparql.setQuery('''
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX saidi: <http://www.semanticweb.org/msigf65thin/ontologies/2021/5/PizzaTutorial#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf saidi:NamedPizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

def get_response_ingredients(pizza):
    sparql.setQuery(f'''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX saidi:<http://www.semanticweb.org/msigf65thin/ontologies/2021/5/PizzaTutorial#>
        SELECT ?name
        WHERE {{ saidi:{pizza} rdfs:subClassOf ?o .
        ?o owl:someValuesFrom ?h .
        ?h rdfs:label ?name
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres


if __name__ == '__main__':
    get_response_pizzas()
