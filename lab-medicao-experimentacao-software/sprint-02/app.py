import csv
from github_api import fetch_data
import os

data_list = fetch_data()

def clone_repo(repo_name, repo_owner, number_repos):
    print(number_repos)
    os.system(f'cd repos && git clone https://github.com/FudanSELab/train-ticket.git')

def generate_metrics(repo_name):
    os.system(f'''
     java -jar /Users/joeyclapton/rd/puc-lab/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar  /Users/joeyclapton/rd/puc/lab-medicao-experimentacao-software/sprint-02/repos/{repo_name} true 0 true /Users/joeyclapton/rd/puc/lab-medicao-experimentacao-software/sprint-02/metrics/
''')

os.system('gh repo clone ...')
with open('lista_repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for repository_item in data_list:
        repo_info = repository_item['node']
        repo_name = repo_info['name']
        repo_stars = repo_info['stargazerCount']
        repo_owner = repo_info['owner']['login']
        primary_language = repo_info['primaryLanguage']['name'] if repo_info.get('primaryLanguage') else None

        writer.writerow(['Name - ' + repo_name])
        writer.writerow(['Primary Language - ' + str(primary_language)])
        writer.writerow(['Primary Language - ' + str(repo_stars)])

        # Adicione uma linha em branco entre os conjuntos de dados
        writer.writerow([])
        writer.writerow([])

print("Dados salvos em dados_repositorios.csv ✅")
