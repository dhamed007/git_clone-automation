# Azure DevOps to GitHub Enterprise Migration

This project automates the process of migrating code repositories from Azure DevOps to GitHub Enterprise. It provides a Python script that clones a repository from Azure DevOps and pushes it to GitHub Enterprise while maintaining the repository history and metadata.

# Table of Contents
Overview
Features
Prerequisites
Setup
Usage
Contributing
License
Overview
Migrating code repositories between version control platforms can be a tedious task, especially when dealing with large projects or multiple repositories. This project aims to simplify the migration process by providing an automated solution.

# Features
Clone from Azure DevOps: Clones a repository from Azure DevOps using Git.
Push to GitHub Enterprise: Pushes the cloned repository to GitHub Enterprise with preserved history and metadata.
Simple Configuration: Requires minimal configuration with just Azure DevOps and GitHub Enterprise credentials.
Prerequisites
Before using this project, ensure you have the following prerequisites:

Azure DevOps account with access to the repository you want to migrate.
GitHub Enterprise account with access to create repositories.
Python installed on your system (version 3.x).
Setup
Clone the Repository: Clone this repository to your local machine.


git clone https://github.com/your_username/azure-devops-to-github-enterprise.git
Install Dependencies: Navigate to the project directory and install the required Python dependencies.


cd azure-devops-to-github-enterprise
pip install -r requirements.txt
Configure GitHub Enterprise Credentials: Set up your GitHub Enterprise credentials as environment variables or pass them directly to the script (see Usage section).

# Usage
To migrate a repository from Azure DevOps to GitHub Enterprise, follow these steps:

Run the Python script azd-gh-automation.py with the necessary parameters:


python migrate.py
You will be prompted to enter your Azure DevOps Personal Access Token (PAT) and GitHub Enterprise PAT.

Follow the instructions provided by the script. It will clone the repository from Azure DevOps and push it to GitHub Enterprise.

After successful migration, verify the repository on GitHub Enterprise.

# Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.
---
