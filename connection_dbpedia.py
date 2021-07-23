from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')


def get_response_dbpedia_pizzas():
    sparql.setQuery(f'''
      SELECT ?name ?res  ?image 
         WHERE {{
            ?object dbo:type dbr:Pizza .
            ?object  dbp:mainIngredient ?res .
            ?object rdfs:label ?name .
      
            ?object dbo:thumbnail ?image 
            FILTER (lang(?name) = 'es')
            
        }}
    ''')

    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    return qres



if __name__ == '__main__':

    result = get_response_dbpedia_pizzas()
    for item in result:
        name, comment, image_url = result['name']['value'], result['comment']['value'], result['image']['value']
