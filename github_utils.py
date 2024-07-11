import csv
import requests
import json

# Load configuration from JSON file
def load_config(file_path='config.json'):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config.get('github_access_token')

def read_csv_repositories(csv_file):
    repositories = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            repository = {
                'Rank': int(row['Rank']),
                'Repository Name': row['Repository Name'].strip(),
                'URL': row['URL'].strip(),
                'Stars': int(row['Stars']),
                'Forks': int(row['Forks'])
            }
            repositories.append(repository)
    return repositories

def calculate_deployment_frequency(repo_owner, repo_name):
    # Load GitHub access token from configuration file
    access_token = load_config()  # Reads the token from config.json

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Initialize counter for deployment frequency
    deployment_count = 0

    # GitHub API URL to fetch workflow runs
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs'

    try:
        # Make a GET request to fetch workflow runs
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Iterate through workflow runs and count successful runs (indicative of deployments)
        for run in data['workflow_runs']:
            if run['conclusion'] == 'success':
                deployment_count += 1

        return deployment_count

    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub Actions data for {repo_owner}/{repo_name}: {e}")
        return 0
