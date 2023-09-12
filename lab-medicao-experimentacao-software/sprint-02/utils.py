from datetime import datetime

def getRepositoryAge(date_info):
    date = datetime
    
    created_on = datetime.strptime(date_info, "%Y-%m-%dT%H:%M:%SZ")

    age = date.now() - created_on

    return age.days