import requests
import os
import time  # Import the time module for rate limiting

def clone_github_org_repos():
    # Prompt the user for the GitHub organization name
    org_name = input("Enter the GitHub organization name: ")

    # Make the URL to the input GitHub organization's repository page
    org_url = f"https://api.github.com/orgs/{org_name}/repos?per_page=200"

    # Add your GitHub token here if needed
    # headers = {"Authorization": "token YOUR_GITHUB_TOKEN"}

    try:
        # Send a GET request to the GitHub API
        response = requests.get(org_url)  # Add headers=headers if using authentication

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        repos = response.json()

        # Clone all the repositories
        for repo in repos:
            repo_url = repo['html_url'] + '.git'
            repo_name = repo['name']

            # Check if the directory already exists
            if not os.path.exists(repo_name):
                os.system(f"git clone {repo_url}")
            else:
                print(f"Repository '{repo_name}' already exists, skipping.")

            # Add a delay to avoid hitting rate limits
            time.sleep(1)

        print("Cloning completed.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    clone_github_org_repos()
