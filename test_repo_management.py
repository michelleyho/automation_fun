import pytest
import repo_management

def test_parser_create_branch_positional():
    parser = repo_management.create_parser()
    parsed = parser.parse_args(['some_random_repo_url', 'create_branch', 'test'])
    assert parsed.remote_repo == 'some_random_repo_url'
    assert parsed.task == 'create_branch'
    assert parsed.dest_branch == 'test' 
    assert parsed.src_branch == 'master'

def test_parser_create_branch_optional():
    parser = repo_management.create_parser()
    parsed = parser.parse_args(['some_random_repo_url', 'create_branch', 'test/feature_branch', '--src_branch', 'feature_branch'])
    assert parsed.remote_repo == 'some_random_repo_url'
    assert parsed.task == 'create_branch'
    assert parsed.dest_branch == 'test/feature_branch' 
    assert parsed.src_branch == 'feature_branch'

def test_parser_create_tag_positional():
    parser = repo_management.create_parser()
    parsed = parser.parse_args(['some_random_repo_url', 'create_tag', 'test_tag'])
    assert parsed.remote_repo == 'some_random_repo_url'
    assert parsed.task == 'create_tag'
    assert parsed.new_tag_name == 'test_tag' 
    assert parsed.tag_msg == ''

def test_parser_create_tag_optional():
    parser = repo_management.create_parser()
    parsed = parser.parse_args(['some_random_repo_url', 'create_tag', 'test_tag1', '--tag_msg', 'pytest test tag'])
    assert parsed.remote_repo == 'some_random_repo_url'
    assert parsed.task == 'create_tag'
    assert parsed.new_tag_name == 'test_tag1' 
    assert parsed.tag_msg == 'pytest test tag'

#@pytest.mark.skip(reason="mock function not working yet")
def test_get_repo_name(mocker):
    #mocker.patch.object('repo_management.giturlparse.parse.name',return_value='test_test')
    mocker.patch.object('repo_management.get_repo_name.g.name',return_value='test_test')
    expected = 'test_test'
    
    actual_repo_name = repo_management.repo_initialization('some_url','')
    assert actual_repo_name == expected

