#!/usr/bin/env python3
import os
import subprocess
import random
from datetime import datetime, timedelta

# Ensure we're in the right directory
os.chdir('/Users/kalabtenadeg/Documents/projects/devops-2021')

# Initialize repo
if not os.path.exists('.git'):
    subprocess.run(['git', 'init'], check=True, capture_output=True)
    subprocess.run(['git', 'config', 'user.name', 'DevOps Learner'], check=True)
    subprocess.run(['git', 'config', 'user.email', 'devops@example.com'], check=True)

def commit(date_str, msg, files_dict):
    for fpath, content in files_dict.items():
        os.makedirs(os.path.dirname(fpath) or '.', exist_ok=True)
        with open(fpath, 'w') as f:
            f.write(content)
    
    subprocess.run(['git', 'add', '-A'], check=True, capture_output=True)
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    subprocess.run(['git', 'commit', '-m', msg, '--quiet'], env=env, check=True, capture_output=True)

print("Creating DevOps 2021 repository with 624 commits...")
print("=" * 60)

# Generate 624 dates throughout 2021
dates = []
start = datetime(2021, 1, 1)
end = datetime(2021, 12, 31)

for _ in range(624):
    days = random.randint(0, (end - start).days)
    date = start + timedelta(days=days)
    # Favor weekdays
    while date.weekday() >= 5 and random.random() > 0.3:
        days = random.randint(0, (end - start).days)
        date = start + timedelta(days=days)
    # Random time between 9 AM and 6 PM
    hour = random.randint(9, 18)
    minute = random.randint(0, 59)
    date = date.replace(hour=hour, minute=minute)
    dates.append(date)

dates.sort()

count = 0
# Initial commit
commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), 
       'Initial commit - Start DevOps learning journey', 
       {'README.md': '# DevOps Learning Journey 2021\n\nLearning DevOps throughout 2021'})
count += 1

# Q1 - Linux and Bash
scripts = [
    ('scripts/disk_check.sh', '#!/bin/bash\ndf -h\n', 'Add disk space check script'),
    ('scripts/backup.sh', '#!/bin/bash\ntar -czf backup.tar.gz /data\n', 'Add backup script'),
    ('scripts/monitor.sh', '#!/bin/bash\ntop -bn1 | head -20\n', 'Add monitoring script'),
    ('.gitignore', '*.log\n*.swp\n.DS_Store\n', 'Add gitignore'),
]

for fpath, content, msg in scripts:
    if count < len(dates):
        commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), msg, {fpath: content})
        count += 1
        if count % 50 == 0:
            print(f"Created {count} commits...")

# Q2 - Docker
docker_files = [
    ('docker/Dockerfile', 'FROM nginx:alpine\nCOPY index.html /usr/share/nginx/html/\n', 'Add nginx Dockerfile'),
    ('docker/index.html', '<h1>DevOps 2021</h1>\n', 'Add HTML file'),
    ('docker-compose.yml', 'version: "3"\nservices:\n  web:\n    build: .\n    ports:\n      - "80:80"\n', 'Add docker-compose'),
]

for fpath, content, msg in docker_files:
    if count < len(dates):
        commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), msg, {fpath: content})
        count += 1
        if count % 50 == 0:
            print(f"Created {count} commits...")

# Q3 - Kubernetes
k8s_files = [
    ('kubernetes/deployment.yaml', 'apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: app\n', 'Add K8s deployment'),
    ('kubernetes/service.yaml', 'apiVersion: v1\nkind: Service\nmetadata:\n  name: app-service\n', 'Add K8s service'),
    ('terraform/main.tf', 'provider "aws" {\n  region = "us-east-1"\n}\n', 'Add Terraform config'),
]

for fpath, content, msg in k8s_files:
    if count < len(dates):
        commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), msg, {fpath: content})
        count += 1
        if count % 50 == 0:
            print(f"Created {count} commits...")

# Q4 - CI/CD
cicd_files = [
    ('.github/workflows/ci.yml', 'name: CI\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n', 'Add GitHub Actions'),
    ('ansible/playbook.yml', '---\n- hosts: all\n  tasks:\n    - name: Install Docker\n', 'Add Ansible playbook'),
    ('monitoring/prometheus.yml', 'global:\n  scrape_interval: 15s\n', 'Add Prometheus config'),
]

for fpath, content, msg in cicd_files:
    if count < len(dates):
        commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), msg, {fpath: content})
        count += 1
        if count % 50 == 0:
            print(f"Created {count} commits...")

# Fill remaining commits with variations
file_templates = [
    ('scripts/util_{}.sh', '#!/bin/bash\necho "Script {}"\n', 'Add utility script {}'),
    ('docker/app_{}/Dockerfile', 'FROM alpine\nRUN apk add curl\n', 'Add Dockerfile for app {}'),
    ('kubernetes/config_{}.yaml', 'apiVersion: v1\nkind: ConfigMap\n', 'Add ConfigMap {}'),
    ('docs/guide_{}.md', '# Guide {}\n\nDocumentation\n', 'Add documentation {}'),
    ('terraform/resource_{}.tf', 'resource "aws_instance" "server_{}" {{}}\n', 'Add Terraform resource {}'),
    ('scripts/deploy_{}.sh', '#!/bin/bash\necho "Deploying {}"\n', 'Add deployment script {}'),
    ('monitoring/alert_{}.yml', 'alert: High CPU {}\n', 'Add alert rule {}'),
]

idx = 0
while count < min(624, len(dates)):
    template_idx = idx % len(file_templates)
    fpath_template, content_template, msg_template = file_templates[template_idx]
    
    fpath = fpath_template.format(idx)
    content = content_template.format(idx)
    msg = msg_template.format(idx)
    
    commit(dates[count].strftime('%a %b %d %H:%M:%S %Y +0000'), msg, {fpath: content})
    count += 1
    idx += 1
    
    if count % 50 == 0:
        print(f"Created {count} commits...")

print(f"\n{'='*60}")
print(f"SUCCESS! Created {count} commits")
print(f"{'='*60}")
