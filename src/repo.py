
class Repo:
    def __init__(self, name):
        self.name = name #done
        self.languages = [] #done
        self.num_commits = 0 #done
        self.num_files = 0 #done
        self.ext = {} #extensões e arquivos por extensão
        self.num_commits_file = {} #arquivos e numero de commits por arquivo 
        self.stars = 0 #done
        self.watchers = 0 #done
        self.forks = 0 #done
        self.num_pull_req_open = 0 #done
        self.num_pull_req_closed = 0 #done
        self.num_pull_req_total = 0 #done
        self.num_issues_open = 0 #done
        self.num_issues_closed = 0 #done
        self.num_issues_total = 0 #done
        return
    
    def add_num_commits(self, number):
        self.num_commits += number
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

    def add_star(self, number):
        self.stars = number
        return
    
    def add_watcher(self, number):
        self.watchers = number
        return
    
    def add_fork(self, number):
        self.forks = number
        return
    
    def add_pull_req(self, repo):
        
        self.num_pull_req_open = repo.get_pulls(state='open').totalCount
        self.num_pull_req_closed = repo.get_pulls(state='closed').totalCount
        self.num_pull_req_total = repo.get_pulls(state='all').totalCount
        return
    
    def add_issue(self, repo):

        self.num_issues_open = repo.get_issues(state = 'open').totalCount
        self.num_issues_closed = repo.get_issues(state = 'closed').totalCount
        self.num_issues_total = repo.get_issues(state = 'all').totalCount
        
        return
    
    def add_language(self, lang):
        
        if lang not in self.languages:
            self.languages.append(lang)
    
    