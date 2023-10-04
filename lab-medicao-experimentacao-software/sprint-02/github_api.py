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
    print(number_repos)
    os.system(f'cd repos && git clone https://github.com/{repo_owner}/{repo_name}.git')

def generate_metrics(repo_name):
    os.system(f'''
     java -jar /Users/joeyclapton/rd/puc-lab/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar  /Users/joeyclapton/rd/puc/lab-medicao-experimentacao-software/sprint-02/repos/{repo_name} true 0 true /Users/joeyclapton/rd/puc/lab-medicao-experimentacao-software/sprint-02/metrics/
''')

def fetch_data():
    data_list = []  # Agora é uma lista, não um dicionário
    query = get_query()
    cursor = None
    has_next_page = True
    count = 0
    max_items = 100


    while count < max_items:
        variables = {
            "queryString": "stars:>500, language:java",
            "cursor": cursor
        }

        response = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)
        data = response.json()

        search_data = data.get('data', {}).get('search', {})
        edges = search_data.get('edges', [])
        
        if not edges:
            break
        
        for edge in edges:
            repo_name = edge['node']['name']
            repo_owner = edge['node']['owner']['login']
            
            print(repo_name)
            print(repo_owner)

            data_list.append(edge)
            clone_repo(repo_name, repo_owner, len(data_list))
        
        page_info = search_data.get('pageInfo', {})
        cursor = page_info.get('endCursor')
        has_next_page = page_info.get('hasNextPage', False)
        
        if not has_next_page:
            break
        
        count += len(edges)
        print(f'Request data {len(data_list)}...{max_items} ⌛️')


    return data_list  # Retorna a lista completa
