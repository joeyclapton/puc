import requests
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
    edges {
      node {
        ... on Repository {
          name
          updatedAt
          primaryLanguage {
            name
          }
          pullRequests(states: MERGED, first: 10) {
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
    
    
    print(f"Repository: {repo_name}")
    print(f"Last Updated: {updated_at}")
    print(f"Primary Language: {primary_language}")
    print(f"Ratio of Closed Issues: {ratio_closed_issues}")
    print(f"Releases Count: {releases_count}")
    print("\n")
