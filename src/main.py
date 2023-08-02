from github import Github
from github import Auth
from repo import Repo
import csv


def get_files(dir, obj, repo):
    for _ in dir:
        if _.type == 'dir':
            get_files(repo.get_contents(_.path), obj, repo)
        elif _.type == 'file':
            obj.add_num_files() #add file
            obj.add_ext(_.path.split('.')[-1], _.name) #add pair ext-file
    return


def get_commits_per_file(obj, repo):

    commits = repo.get_commits()
    for commit in commits:
        commit_arquivos = commit.files
        for arquivo in commit_arquivos:
            caminho_arquivo = arquivo.filename
            obj.add_commit_file(caminho_arquivo)

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

def main():

    auth = Auth.Token("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")
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
            #get_files(repo.get_contents('.'), new_repo, repo)
            new_repo.add_star(repo.stargazers_count)
            new_repo.add_watcher(repo.watchers_count)
            new_repo.add_fork(repo.forks_count)
            new_repo.add_issue(repo)
            new_repo.add_pull_req(repo)
            #get_commits_per_file(new_repo, repo)
            print(new_repo.ext)
            count += 1
            reps.append(new_repo)
    
    write_csv_general(reps)

    return reps

if __name__ == '__main__':
    main()