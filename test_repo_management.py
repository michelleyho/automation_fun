import pytest
import repo_management

def test_something():
    parser = repo_management.create_parser()
    parsed = parser.parse_args(['some_random_repo_url', 'create_branch', 'test'])
    assert parsed.remote_repo == 'some_random_repo_url'
    assert parsed.dest_branch == 'test' 
