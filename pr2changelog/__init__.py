import os
import json
import requests
from .document import Document
from .change import Change

__version__ = '0.1.0'

os.environ['INPUT_FILE_NAME'] = 'CHANGELOG.md'

try:
    REPO = os.environ['INPUT_REPO']
    TOKEN = os.environ['INPUT_GITHUB_TOKEN']
    PR_NUMBER = os.environ['INPUT_PR_NUMBER']
    CHANGE_TOKEN = os.environ['INPUT_CHANGE_TOKEN']
    FILE_NAME = os.environ['INPUT_FILE_NAME']
except KeyError:
    print("Something is wrong with envs!")
    raise KeyError


api_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
print(api_url)

r = requests.get(api_url)
data = json.loads(r.text)
print(data)

document = Document(FILE_NAME)
change = Change(data)