from github import Github
from github import Auth
from repo import Repo


def get_files(dir, obj, repo):
    for _ in dir:
        if _.type == 'dir':
            get_files(repo.get_contents(_.path), obj, repo)
        elif _.type == 'file':
            obj.add_num_files() #add file
            obj.add_ext(_.path.split('.')[-1], _.name) #add pair ext-file
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
            print(new_repo.ext)
            count += 1
            reps.append(new_repo)

    print(count)

if __name__ == '__main__':
    main()