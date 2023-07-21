from github import Github
from github import Auth

auth = Auth.Token("")

g = Github(auth=auth)

project = g.get_user("googlesamples")

repos = project.get_repos()

count = 0

for repo in repos:
    print(repo.name)
    count += 1

print(count)