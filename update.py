import os
from git.repo import Repo

giturl = 'https://github.com/Andy-Jen/openCV_ws'
file_path = 'gitserver'

local_path = os.path.join(file_path)


if os.path.exists(file_path):
    print('Find git server, check version...')
    repo = Repo(local_path)

    for tag in repo.tags:
        print(tag.name)
else:
    print('Nofind git server, Git clone for giturl...')
    Repo.clone_from(giturl, to_path=local_path, branch='master')






