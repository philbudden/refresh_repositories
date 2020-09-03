# Refresh Repositories

Simple package for keeping local copies of all your GitHub repositories up to date.

Useful if you want to keep a backup of all repos and you regulalry work from other systems.

### Installation

```
pip install -r requirements.txt
pip install -e .
```

### Configuration

Complete the user_settings parameters in config.ini:
- workspace_path: the directory containing your repositories
- github_username: the username for the github account you want to sync with
- access_token: [a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

You will also need to be able to [connect to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

### Usage

```
python /src/main.py
```

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
[MIT](https://choosealicense.com/licenses/mit/)