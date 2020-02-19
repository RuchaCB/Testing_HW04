import requests
import json

def getInfo(UID):
    request_URL = requests.get(f'https://api.github.com/users/{UID}/repos')
    reply = request_URL.json()
    for val in reply:
        repos = val.get("name")
        
        commits_URL = requests.get(f'https://api.github.com/repos/{UID}/{repos}/commits')
        commits = commits_URL.json()
        num = 0
        for each in commits:
            num+=1
        yield(repos,num)
       

def main():
    user_ID = input("Please enter Users ID which you want to fetch results:  ")
    try:
        for repos, num in getInfo(user_ID):
            print(f"Repo: {repos} Number of commits: {num}")
    except Exception as Ex:
        print(f"Exception has occured please check the repo address used: {Ex}")


#main()