from github import Github
import requests
import json

g = Github("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")

def lambda_handler(event, context):
    print('## EVENT')
    data = event['body']
    #print(data)
    string = json.loads(data)
    target_repo = string['repository']['full_name']
    print(target_repo)
    repo = g.get_repo(target_repo)
    branch = repo.get_branch("main")
    print(branch)
    branch.edit_protection(required_approving_review_count=2, enforce_admins=True)
    # print(event['Records'][0]['repository']['full_name'])