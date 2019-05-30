import requests
import sys

url = "https://api.github.com/users/"

githubname = input("enter the githubname please:")


response_repos = requests.get(url + githubname + "/repos")
repos=response_repos.json()


try:

    for i in range(len(repos)):
        print(repos[i]["name"])

except KeyError:
    sys.stderr.write("Not a valid githubname")
