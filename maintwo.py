import argparse
import os

DEV_CHAT_ID = os.environ.get('DEV_CHAT_ID') or 'unknown'
repository = os.environ.get('GITHUB_REPOSITORY') or 'unknown'
event_name = os.environ.get('GITHUB_EVENT_NAME') or 'unknown'
branch = os.environ.get('GITHUB_REF') or 'unknown'
actor = os.environ.get('GITHUB_ACTOR') or 'unknown'
repository_owner = os.environ.get('GITHUB_REPOSITORY_OWNER') or 'unknown'
my_secret = os.environ.get('MY_SECRET') or 'unknown'
action_author = os.environ.get('ACTION_AUTHOR') or 'unknown'

def main():
    """
    A description of the entire function, its parameters, and its return types.
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--pr_number', type=int, help='Pull request number')
    args = parser.parse_args()

    if args.pr_number:
        print(f"This is a pull request with PR number: {args.pr_number}")
        github_pr_url = f"https://www.github.com/{repository}/pull/{args.pr_number}"
        print(github_pr_url)
    else:
        print("This is not a pull request")
        # make commit url for the push event
        if event_name == 'push':
            commit_url = f"https://www.github.com/{repository}/commit/{branch}"
            print(commit_url)
        
if __name__ == "__main__":
    main()