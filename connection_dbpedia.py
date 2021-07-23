from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')


def get_response_dbpedia(item):
    sparql.setQuery(f'''
        SELECT ?name ?comment
        WHERE {{
            dbr:{item} rdfs:label ?name .
            dbr:{item} rdfs:comment ?comment .
            FILTER (lang(?name) = 'es')
            FILTER (lang(?comment) = 'es')
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()

    if len(qres['results']['bindings']) == 0:
        # print("---------------------")
        return "Información no encontrada"

    else:
        result = qres['results']['bindings'][0]
        comment = result['comment']['value']
        # print("---------------------me lleva")
        return comment


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
        # print ('Nombre de la pizza : ' + name + "\n Descripción : " + comment + "\n" + image_url)
    # print(get_response_dbpedia(item))
    # print_response_dbpedia(qres)