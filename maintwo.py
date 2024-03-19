import argparse
import os
import telebot

DEV_CHAT_ID = os.environ.get('DEV_CHAT_ID') or 'unknown'
repository = os.environ.get('GITHUB_REPOSITORY') or 'unknown'
event_name = os.environ.get('GITHUB_EVENT_NAME') or 'unknown'
branch = os.environ.get('GITHUB_REF') or 'unknown'
actor = os.environ.get('GITHUB_ACTOR') or 'unknown'
repository_owner = os.environ.get('GITHUB_REPOSITORY_OWNER') or 'unknown'
my_secret = os.environ.get('MY_SECRET') or 'unknown'
action_author = os.environ.get('ACTION_AUTHOR') or 'unknown'
commit_url = os.environ.get('COMMIT_URL') or 'unknown'

bot = telebot.TeleBot(my_secret)

MAIN_GIF = "https://raw.githubusercontent.com/vapecatcoin/cdn/main/catrings.gif"

def send_formatted_message(url):
    formatted_message = f"<b>New Event on GitHub</b>" \
                    f"\n\n" \
                    f"Repository: {repository}" \
                    f"\nEvent name: {event_name}" \
                    f"\nBranch: {branch}" \
                    f"\nActor: {actor}" \
                    f"\nRepository owner: {repository_owner}" \
                    f"\n\n<a href='{url}'>Check it out!</a>\n"
    bot.send_message(DEV_CHAT_ID, formatted_message, parse_mode='HTML', disable_web_page_preview=True)

def send_formatted_message_with_gif(url, gif_url):
    formatted_message = f"<b>New Event on GitHub</b>" \
                    f"\n\n" \
                    f"Repository: {repository}" \
                    f"\nEvent name: {event_name}" \
                    f"\nBranch: {branch}" \
                    f"\nActor: {actor}" \
                    f"\nRepository owner: {repository_owner}" \
                    f"\n\n<a href='{url}'>Check it out!</a>\n"
    bot.send_photo(DEV_CHAT_ID, gif_url, caption=formatted_message, parse_mode='HTML', supports_streaming=True)

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

        send_formatted_message_with_gif(github_pr_url, MAIN_GIF)

    else:
        print("This is not a pull request")
        # make commit url for the push event
        if event_name == 'push':
            print(commit_url)
            send_formatted_message_with_gif(github_pr_url, MAIN_GIF)
        
if __name__ == "__main__":
    main()