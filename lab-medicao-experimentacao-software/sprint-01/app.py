import csv
from utils import getRepositoryAge
from chart import box_plot, bar
from github_api import fetch_data

data_list = fetch_data()

with open('dados_repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    repo_ages = []
    repo_pr_merged = []
    repo_releases = []
    repo_last_update = []
    repo_language = []
    repo_closed_issues = []

    for repository_item in data_list:
        repo_info = repository_item['node']
        repo_name = repo_info['name']
        created_at = getRepositoryAge(repo_info['createdAt'])
        updated_At = getRepositoryAge(repo_info['updatedAt'])
        primary_language = repo_info['primaryLanguage']['name'] if repo_info.get('primaryLanguage') else None
        pull_requests_merged = repo_info['pullRequests']['totalCount']
        releases_count = repo_info['releases']['totalCount']
        closed_issues_count = repo_info['issues']['totalCount']
        total_issues_count = repo_info['totalIssues']['totalCount']
        
        if total_issues_count > 0:
            ratio_closed_issues = closed_issues_count / total_issues_count
        else:
            ratio_closed_issues = 0.0

        repo_ages.append(created_at)
        repo_pr_merged.append(pull_requests_merged)
        repo_releases.append(releases_count)
        repo_last_update.append(updated_At)
        repo_language.append(primary_language)
        repo_closed_issues.append(ratio_closed_issues)

        writer.writerow(['Name - ' + repo_name])
        writer.writerow(['Created ago ' + str(created_at) + ' days'])
        writer.writerow(['Primary Language - ' + str(primary_language)])
        writer.writerow(['Releases count - ' + str(releases_count)])
        writer.writerow(['Ratio closed issues - ' + str(ratio_closed_issues)])
        writer.writerow(['Merged Pull Requests - ' + str(pull_requests_merged)])
        # Adicione uma linha em branco entre os conjuntos de dados
        writer.writerow([])
        writer.writerow([])
    
    box_plot(repo_ages, 'Sistemas populares são maduros/antigos?', 'Idade do repositório em dias')
    box_plot(repo_pr_merged, 'Sistemas populares recebem muita contribuição externa?', 'Total de pull requests aceitas')
    box_plot(repo_releases, 'Sistemas populares lançam releases com frequência?', 'Total de releases')
    box_plot(repo_last_update, 'Sistemas populares são atualizados com frequência?', ' tempo até a última atualização')
    bar(repo_language, 'Sistemas populares são escritos nas linguagens mais populares', 'Linguagem utilizada')
    box_plot(repo_closed_issues, 'Sistemas populares possuem um alto percentual de issues fechadas?', 'Razão entre número de issues fechadas pelo total de issues')

print("Dados salvos em dados_repositorios.csv ✅")
