from github_utils import read_csv_repositories, calculate_deployment_frequency

def main():
    # Path to your CSV file containing repository information
    csv_file_path = 'repos.csv'

    # Read repositories from CSV file
    repositories = read_csv_repositories(csv_file_path)

    # Calculate deployment frequency for each repository
    for repo in repositories:
        # Extract repository owner and name from URL
        url_parts = repo['URL'].strip('/').split('/')
        repo_owner = url_parts[-2]
        repo_name = url_parts[-1]

        deployment_frequency = calculate_deployment_frequency(repo_owner, repo_name)
        print(f"Repository: {repo_name}, Deployment Frequency: {deployment_frequency}")

if __name__ == "__main__":
    main()
