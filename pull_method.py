import json
import os
import git


def read_json():
    import pdb;pdb.set_trace()
    src_folder = "D:\\New_dev65\\modules\\zope_build\\src"
    repo_name = os.environ.get("REPO_NAME", "jivacore.sre")
    json_file = {}
    with open("D:\\Python_basic_practice\\test_db.json") as k:
        json_file = json.load(k)
    for repo, dependent_repos in json_file.iteritems():
        if repo == repo_name:
            pull_git_repos(dependent_repos, src_folder)
    remote_heads = git.cmd.Git().ls_remote("{src_folder}/{repo_name}".format(src_folder=src_folder, repo_name=repo_name), heads=True)


def pull_git_repos(repos, src_folder):
    import pdb;pdb.set_trace()
    for repo in repos:
        g = git.Repo("{src_folder}/{repo}".format(src_folder=src_folder, repo=repo))
        g.remotes.origin.pull()


read_json()
