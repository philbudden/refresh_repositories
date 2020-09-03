import os
import logging
import requests

from pathlib import Path
from src.helpers.get_config import get_config

LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':

    config_user, config_dev = get_config(
        f'{Path(__file__).parent.parent}/config.ini'
    )

    workspace = config_user['workspace_path']
    sub_dirs = [f.name for f in os.scandir(workspace) if f.is_dir()]

    user = config_user['github_username']
    token = config_user['access_token']
    head = {'Authorization': 'token {}'.format(token)}
    LOGGER.info(f'Fetching repository list for {user}')
    r = requests.get(
        f'https://api.github.com/user/repos', headers=head)
    json_r = r.json()

    LOGGER.info('Found the following repositories:')
    repo_list = []
    for dict in json_r:
        name = dict['name']
        LOGGER.info(name)
        repo_list.append(name)

    LOGGER.info('Checking for missing repositories')
    missing_repos = [r for r in repo_list if r not in sub_dirs]
    os.chdir(workspace)
    for repo in missing_repos:
        LOGGER.info(f'Cloning {repo} repository into {workspace}')
        os.system(f'git clone git@github.com:{user}/{repo}.git')

    LOGGER.info('Checking for active repositories')
    active_repos = [r for r in sub_dirs if r in repo_list]
    for repo in active_repos:
        LOGGER.info(f'Updating {repo} repository')
        os.chdir(f'{workspace}/{repo}')
        os.system(f'git pull --all')
