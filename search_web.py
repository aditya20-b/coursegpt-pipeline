import googlesearch


class SearchWeb:
    def __init__(self, num):
        self.num = num

    def google_search(self, query):
        search_results = googlesearch.search(query, num_results=self.num)
        return search_results

