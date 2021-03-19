import argparse
import git

def repo_initialization():
    repo = git.Repo.clone_from('git@github.com:michelleyho/useful_bash_scripts', 'useful_bash_script')

    for branch in repo.branches:
        print(branch)

    return repo 

def create_branch(args):
    repo = repo_initialization()
    repo.git.branch(args.dest_branch)
    repo.git.checkout(args.dest_branch)
    repo.remotes.origin.push(args.dest_branch)

def create_tag(args):
    repo = repo_initialization()
#    new_tag = repo.create_tag('test-tag1', message='test tag created from test/branch_1')
    new_tag = repo.create_tag(args.new_tag_name, message=args.tag_msg)
    repo.remotes.origin.push(new_tag)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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
