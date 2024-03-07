import os
import shutil
import subprocess
import requests

def clone_azure_devops_repo(azure_devops_organization, azure_devops_project, azure_devops_pat, repo_name, clone_dir):
    try:
        subprocess.run(["git", "clone", "--mirror", f"https://dev.azure.com/{azure_devops_organization}/{azure_devops_project}/_git/{repo_name}", clone_dir], check=True)
        print("Azure DevOps repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print("Error cloning Azure DevOps repository:", e)
        exit(1)

def push_to_github_enterprise(enterprise_github_username, enterprise_github_token, repo_name, clone_dir):
    github_repo_url = f"https://{enterprise_github_username}:{enterprise_github_token}@github.enterprise.com/{enterprise_github_username}/{repo_name}.git"
    try:
        subprocess.run(["git", "-C", clone_dir, "remote", "add", "github", github_repo_url], check=True)
        print("GitHub remote added successfully.")
    except subprocess.CalledProcessError as e:
        print("Error adding GitHub remote:", e)
        exit(1)
    try:
        subprocess.run(["git", "-C", clone_dir, "push", "--mirror", "github"], check=True)
        print("Repository successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("Error pushing repository to GitHub:", e)
        exit(1)

# Azure DevOps details and GitHub Enterprise credentials
azure_devops_organization = "your_organization"
azure_devops_project = "your_project"
azure_devops_pat = input("Input Azure DevOps PAT: ")
enterprise_github_username = "your_github_username"
enterprise_github_token = input("Input GitHub Enterprise PAT: ")

# Extract repository name
repo_name = "repo_to_clone"

# Directory to clone the repository
clone_dir = "temp_repo"

# Clone the Azure DevOps repository
clone_azure_devops_repo(azure_devops_organization, azure_devops_project, azure_devops_pat, repo_name, clone_dir)

# Push to GitHub Enterprise
push_to_github_enterprise(enterprise_github_username, enterprise_github_token, repo_name, clone_dir)

# Clean up
shutil.rmtree(clone_dir)