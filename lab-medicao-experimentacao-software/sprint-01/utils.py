from datetime import datetime

def getRepositoryAge(created_at):
    date = datetime
    
    created_on = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")

    age = date.now() - created_on

    return age.days