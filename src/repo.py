
class Repo:
    def __init__(self):
        self.num_commits = 0
        self.num_files = 0
        self.ext = {} #extensões e numero de arquivos por extensão
        self.num_commits_file = {} #arquivos e numero de commits por arquivo
        self.stars = 0
        self.watchers = 0
        self.forks = 0
        self.num_pull_req = 0
        self.num_issues = 0
        return
    
    def add_num_commits(self):
        self.num_commits += 1
        return

    def add_num_files(self):
        self.num_files += 1
        return
    
    def add_ext(self, ext, file):
        if ext in self.ext:
            self.ext[ext].append(file)
        else:
            self.ext[ext] = [file]
        return
    
    def add_commit_file(self, filename):
        if filename in self.num_commits_file:
            self.num_commits_file[filename] += 1
        else:
            self.num_commits_file[filename] = 1
        return

    def add_star(self):
        self.stars += 1
        return
    
    def add_watcher(self):
        self.watchers += 1
        return
    
    def add_fork(self):
        self.forks += 1
        return
    
    def add_pull_req(self):
        self.num_pull_req += 1
        return
    
    def add_issue(self):
        self.num_issues += 1
        return
    
    