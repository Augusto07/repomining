from github import Github
from github import Auth

auth = Auth.Token("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")

g = Github(auth=auth)

project = g.get_user("googlesamples")

repos = project.get_repos()

count = 0

#get_content -> obter todos os arquivos do dir raiz

for repo in repos:
    if repo.language == "Java":
        print(repo.name, repo.language)
        count += 1

print(count)