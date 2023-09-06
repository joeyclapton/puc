import requests
import csv
from utils import getRepositoryAge
from graph import gen_box_plot
from github_api import getToken, getQuery

github_token = getToken()

headers = {
    'Authorization': f'Bearer {github_token}',
}

query = getQuery();

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

        data_list.extend(edges)  
        # Extend a lista com novos elementos, não é uma atribuição direta
        cursor = page_info.get('endCursor')
        has_next_page = page_info.get('hasNextPage', False)
        print(f'Request data {len(data_list)}...1000 ⌛️')

    return data_list  # Retorna a lista completa

data_list = fetch_data(query)

with open('dados_repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    repo_ages = []
    repo_pr_merged = []
    repo_releases = []

    for repository_item in data_list:
        repo_info = repository_item['node']
        repo_name = repo_info['name']
        created_at = getRepositoryAge(repo_info['createdAt'])
        primary_language = repo_info['primaryLanguage']['name'] if repo_info.get('primaryLanguage') else None
        pull_requests_merged = repo_info['pullRequests']['totalCount']
        releases_count = repo_info['releases']['totalCount']
        closed_issues_count = repo_info['issues']['totalCount']
        total_issues_count = repo_info['totalIssues']['totalCount']

        repo_ages.append(created_at)
        repo_pr_merged.append(pull_requests_merged)
        repo_releases.append(total_issues_count)

        if total_issues_count > 0:
            ratio_closed_issues = closed_issues_count / total_issues_count
        else:
            ratio_closed_issues = 0.0

        writer.writerow(['Name - ' + repo_name])
        writer.writerow(['Days on created - ' + str(created_at)])
        writer.writerow(['Primary Language - ' + str(primary_language)])
        writer.writerow(['Releases count - ' + str(releases_count)])
        writer.writerow(['Ratio closed issues - ' + str(ratio_closed_issues)])
        writer.writerow(['Merged Pull Requests - ' + str(pull_requests_merged)])
        # Adicione uma linha em branco entre os conjuntos de dados
        writer.writerow([])
        writer.writerow([])

    gen_box_plot(repo_ages, 'Idade dos repositórios', 'Dias')
    gen_box_plot(repo_pr_merged, 'Total de PRs', 'Total de pull requests aceitas')
    gen_box_plot(repo_releases, 'Total de releases', '')

print("Dados salvos em dados_repositorios.csv ✅")
