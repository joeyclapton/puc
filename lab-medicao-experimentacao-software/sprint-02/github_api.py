import requests
import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': f'Bearer {github_token}',
}

def get_query():

    return '''
query ($queryString: String!, $cursor: String) {
        search(query: $queryString, type: REPOSITORY, first: 3, after: $cursor) {
            pageInfo {
            hasNextPage
            endCursor
            }
            edges {
            node {
                ... on Repository {
                name
                owner {
                    login
                }
                stargazerCount
                primaryLanguage {
                    name
                }
                }
            }
        }
    }
}
'''

def clone_repo(repo_name, repo_owner, number_repos):
    if(number_repos == 2):
        os.system(f'git clone https://github.com/{repo_owner}/{repo_name}.git')


def fetch_data():
    data_list = []  # Agora é uma lista, não um dicionário
    query = get_query()
    cursor = None
    has_next_page = True

    while has_next_page and len(data_list) < 9:
        variables = {
            "queryString": "stars:>500, language:java",
            "cursor": cursor
        }

        response = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)
        data = response.json()

        search_data = data.get('data', {}).get('search', {})
        edges = search_data.get('edges', [])

        page_info = search_data.get('pageInfo', {})
        data_list.extend(edges)  
        
        os.system('date +"Today is: %A %d %B"')

        # Extend a lista com novos elementos, não é uma atribuição direta
        cursor = page_info.get('endCursor')
        has_next_page = page_info.get('hasNextPage', False)
        print(f'Request data {len(data_list)}...1000 ⌛️')

    return data_list  # Retorna a lista completa
