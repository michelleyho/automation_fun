import argparse
import git
import giturlparse

def repo_initialization(repo_url, repo_name):
    g = giturlparse.parse(repo_url)
    if not repo_name:
        repo_name = g.name

    cloned_repo = git.Repo.clone_from(repo_url, repo_name)

    for branch in cloned_repo.branches:
        print(branch)

    return cloned_repo 

def create_branch(args):
    repo = repo_initialization(args.remote_repo, args.repo_name)
    repo.git.branch(args.dest_branch)
    repo.git.checkout(args.dest_branch)
    repo.remotes.origin.push(args.dest_branch)

def create_tag(args):
    repo = repo_initialization(remote_repo, args.repo_name)
    new_tag = repo.create_tag(args.new_tag_name, message=args.tag_msg)
    repo.remotes.origin.push(new_tag)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('remote_repo', help="remote repo to clone")
    parser.add_argument('--repo_name', help="name for cloned remote repo")
    subparser = parser.add_subparsers(dest='task')
    create_branch_parser = subparser.add_parser('create_branch')
    create_tag_parser = subparser.add_parser('create_tag')
    
    create_branch_parser.add_argument('dest_branch', help="New branch name")
    create_branch_parser.set_defaults(func=create_branch)
    create_branch_parser.add_argument('--src_branch', default='master', help="Original branch to branch from")

    create_tag_parser.add_argument('new_tag_name', help="New tag name")
    create_tag_parser.set_defaults(func=create_tag)
    create_tag_parser.add_argument('--tag_msg', default='', help="Tag message")
    
    args = parser.parse_args() 
    args.func(args)
