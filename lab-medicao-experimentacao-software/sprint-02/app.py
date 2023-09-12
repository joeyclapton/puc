from github_api import fetch_data
import os

data_list = fetch_data()

def clone_repo(repo_name, repo_owner, number_repos):
    print(number_repos)
    if(number_repos == 9):
        os.system(f'git clone https://github.com/{repo_owner}/{repo_name}.git')

os.system('gh repo clone ...')
for repository_item in data_list:
    repo_info = repository_item['node']
    repo_name = repo_info['name']
    repo_owner = repo_info['owner']['login']
    primary_language = repo_info['primaryLanguage']['name'] if repo_info.get('primaryLanguage') else None
    print("Entrou aqui")
    clone_repo(repo_name, repo_owner, len(data_list))

print("Dados salvos em dados_repositorios.csv ✅")
