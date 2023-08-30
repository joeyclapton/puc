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
{
  search(query: "stars:>5000", type: REPOSITORY, first: 10) {
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
            pageInfo {
              hasNextPage
              endCursor
            }
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

response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
data = response.json()
with open('dados_repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for repository in data['data']['search']['edges']:
        repo_info = repository['node']
        repo_name = repo_info['name']
        updated_at = repo_info['updatedAt']
        primary_language = repo_info['primaryLanguage']['name'] if repo_info['primaryLanguage'] else None
        pull_requests = repo_info['pullRequests']['edges']
        releases_count = repo_info['releases']['totalCount']
        closed_issues_count = repo_info['issues']['totalCount']
        total_issues_count = repo_info['totalIssues']['totalCount']
    
        if total_issues_count > 0:
            ratio_closed_issues = closed_issues_count / total_issues_count
        else:
            ratio_closed_issues = 0.0
    
        writer.writerow(['Name - '+repo_name])
        writer.writerow(['Updated at - '+updated_at])
        writer.writerow(['Primary Language - '+str(primary_language)])
        writer.writerow(['Releases count - '+str(releases_count)])
        writer.writerow(['Ratio closed issues - '+str(ratio_closed_issues)])
        # Adicione uma linha em branco entre os conjuntos de dados
        writer.writerow([])
        writer.writerow([])

print("Dados salvos em dados_repositorios.csv")