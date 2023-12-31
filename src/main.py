from github import Github
from github import Auth
from repo import Repo
import requests
import csv


def get_commits_per_file(obj, repo):

    commits = repo.get_commits()
    for commit in commits:
        commit_arquivos = commit.files
        for arquivo in commit_arquivos:
            caminho_arquivo = arquivo.filename
            obj.add_commit_file(caminho_arquivo)
            obj.add_num_files()
            obj.add_ext(caminho_arquivo.split('.')[-1], caminho_arquivo)

    print(obj.num_commits_file)
    return

def write_csv_general(reps):

    with open('repos_info.csv', mode='w', newline='') as csvfile:

        fieldnames = ['name', 'languages', 'num_commits', 'num_files', 'stars', 'watchers',
                      'forks', 'num_pull_req_open', 'num_pull_req_closed', 'num_pull_req_total',
                      'num_issues_open', 'num_issues_closed', 'num_issues_total']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for repo in reps:
            writer.writerow({
                'name': repo.name,
                'languages': ', '.join(repo.languages),
                'num_commits': repo.num_commits,
                'num_files': repo.num_files,
                'stars': repo.stars,
                'watchers': repo.watchers,
                'forks': repo.forks,
                'num_pull_req_open': repo.num_pull_req_open,
                'num_pull_req_closed': repo.num_pull_req_closed,
                'num_pull_req_total': repo.num_pull_req_total,
                'num_issues_open': repo.num_issues_open,
                'num_issues_closed': repo.num_issues_closed,
                'num_issues_total': repo.num_issues_total,
            })
    return

def write_csv_arq_ext(reps):

    with open('arq_ext_info.csv', mode='w', newline='') as csvfile:

        fieldnames = ['name', 'ext', 'file_name']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for repo in reps:
            for ext, files in repo.ext.items():
                for file in files:
                    writer.writerow({
                        'name': repo.name,
                        'ext': '.'+ str(ext),
                        'file_name': file,
                    })
    return

def write_csv_arq_commit(reps):

    with open('arq_file_info.csv', mode='w', newline='') as csvfile:

        fieldnames = ['name', 'file_name', 'commit_num']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for repo in reps:
            for filename, commits in repo.num_commits_file.items():
                writer.writerow({
                    'name': repo.name,
                    'file_name': str(filename),
                    'commit_num': commits,
                })
    return


def mining_from_api(auth_token, repo_name):

    url = f"https://api.github.com/repos/googlesamples/{repo_name}"
    header = {}
    header["Authorization"] = auth_token

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        dados_repositorio = response.json()
        numero_watchers = dados_repositorio["subscribers_count"]
        return numero_watchers

def mining_from_pkg(auth_token):

    auth = Auth.Token(auth_token)
    g = Github(auth=auth)
    project = g.get_user("googlesamples")
    repos = project.get_repos()
    count = 0
    reps = []
    for repo in repos:

        if repo.language in ['Java', 'Kotlin']:

            print(repo.name, repo.language)

            new_repo  = Repo(repo.name) #add name
            new_repo.add_language(repo.language) #add lang
            new_repo.add_num_commits(repo.get_commits().totalCount) #add number of commits
            new_repo.add_star(repo.stargazers_count)
            new_repo.add_watcher(mining_from_api(auth_token, repo.name))
            new_repo.add_fork(repo.forks_count)
            new_repo.add_issue(repo)
            new_repo.add_pull_req(repo)
            get_commits_per_file(new_repo, repo)
            print(new_repo.ext)
            count += 1
            reps.append(new_repo)
    
    write_csv_general(reps)
    write_csv_arq_ext(reps)
    write_csv_arq_commit(reps)

    return reps



def main():

    auth_token = input("insira o token:")
    mining_from_pkg(auth_token)
    return

if __name__ == '__main__':
    main()