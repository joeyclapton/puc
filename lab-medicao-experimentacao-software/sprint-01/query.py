import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
}

query = '''
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
          updatedAt
          primaryLanguage {
            name
          }
          pullRequests(states: MERGED, first: 1) {
            edges {
              node {
                title
                createdAt
                mergedAt
                url
                author {
                  login
                }
              }
            }
          }
          releases {
            totalCount
          }
          issues(states: CLOSED) {
            totalCount
          }
          totalIssues: issues {
            totalCount
          }
        }
      }
    }
  }
}
'''

def fetch_data(query):
    data_list = []  # Agora é uma lista, não um dicionário

    cursor = None
    has_next_page = True

    while has_next_page and len(data_list) < 1000:
        variables = {
            "queryString": "stars:>500",
            "cursor": cursor
        }

        response = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)
        data = response.json()

        search_data = data.get('data', {}).get('search', {})
        edges = search_data.get('edges', [])

        page_info = search_data.get('pageInfo', {})

        data_list.extend(edges)  # Extend a lista com novos elementos, não é uma atribuição direta
        cursor = page_info.get('endCursor')
        has_next_page = page_info.get('hasNextPage', False)
        print(f'Request data {len(data_list)}...1000 ⌛️')

    return data_list  # Retorna a lista completa

data_list = fetch_data(query)

with open('dados_repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for repository_item in data_list:
        repo_info = repository_item['node']
        repo_name = repo_info['name']
        updated_at = repo_info['updatedAt']
        primary_language = repo_info['primaryLanguage']['name'] if repo_info.get('primaryLanguage') else None
        pull_requests = repo_info['pullRequests']['edges']
        releases_count = repo_info['releases']['totalCount']
        closed_issues_count = repo_info['issues']['totalCount']
        total_issues_count = repo_info['totalIssues']['totalCount']

        if total_issues_count > 0:
            ratio_closed_issues = closed_issues_count / total_issues_count
        else:
            ratio_closed_issues = 0.0

        writer.writerow(['Name - ' + repo_name])
        writer.writerow(['Updated at - ' + updated_at])
        writer.writerow(['Primary Language - ' + str(primary_language)])
        writer.writerow(['Releases count - ' + str(releases_count)])
        writer.writerow(['Ratio closed issues - ' + str(ratio_closed_issues)])
        # Adicione uma linha em branco entre os conjuntos de dados
        writer.writerow([])
        writer.writerow([])

print("Dados salvos em dados_repositorios.csv ✅")
