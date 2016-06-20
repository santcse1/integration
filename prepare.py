#!/usr/bin/env python3

import json
import os
import subprocess

work_dir = os.path.realpath(os.curdir)

f = open('config.txt', 'r')
config = json.load(f.read())

for pr in config:
    os.chdir(work_dir)
    subprocess.check_call(['git', 'clone', '--depth', '50', '-b', pr['base_branch'],
        'https://github.com/{}/{}.git'.format(pr['owner'], pr['repo'])])
    os.chdir(pr['repo'])
    subprocess.check_call(['git', 'fetch', 'origin', 'pull/{}/head'.format(pr['number'])])
    subprocess.check_call(['git', 'checkout', pr['base_sha']])
    subprocess.check_call(['git', 'merge', pr['head_sha']])


