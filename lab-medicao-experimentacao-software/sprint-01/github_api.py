import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

def getToken():
    
    return github_token

def getQuery():

    return '''
    query ($queryString: String!, $cursor: String) {
        search(query: $queryString, type: REPOSITORY, first: 3, after: $cursor) {
            pageInfo {
            hasNextPage
            endCursor
            }
            edges {
            node {
                ... on Repository {
                name
                updatedAt
                createdAt
                primaryLanguage {
                    name
                }
                pullRequests(states: MERGED) {
                    totalCount
                }
                releases {
                    totalCount
                }
                issues(states: CLOSED) {
                    totalCount
                }
                totalIssues: issues {
                    totalCount
                }
                }
            }
            }
        }
        }
'''

