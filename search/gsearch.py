from googlesearch import search
def search_google(query, num):
    results = []
    for url in search(query, num_results=num):
        results.append(url)
    return "\n".join(results)
