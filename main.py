import os
import telebot

# Accessing GitHub Actions context
DEV_CHAT_ID = os.environ.get('DEV_CHAT_ID') or 'unknown'
repository = os.environ.get('GITHUB_REPOSITORY') or 'unknown'
event_name = os.environ.get('GITHUB_EVENT_NAME') or 'unknown'
branch = os.environ.get('GITHUB_REF') or 'unknown'
actor = os.environ.get('GITHUB_ACTOR') or 'unknown'
repository_owner = os.environ.get('GITHUB_REPOSITORY_OWNER') or 'unknown'
my_secret = os.environ.get('MY_SECRET') or 'unknown'

bot = telebot.TeleBot(my_secret)

# build repo url
repo_url = f"https://www.github.com/{repository}"

if event_name == 'pull_request':
    pull_request_number = os.environ.get('PULL_REQUEST_NUMBER') or 'unknown'
    repo_url = f"https://www.github.com/{repository}/pull/{pull_request_number}"

# formatted_message = f"New {event_name} on {repository} by {actor} on branch {branch}"
formatted_message = f"<b>New Event on GitHub</b>" \
                    f"\n\n" \
                    f"Repository: {repository}" \
                    f"\nEvent name: {event_name}" \
                    f"\nBranch: {branch}" \
                    f"\nActor: {actor}" \
                    f"\nRepository owner: {repository_owner}" \
                    f"\n\n<a href='{repo_url}'>{repository}</a>\nMirrored to Arweave" \
                    
bot.send_message(DEV_CHAT_ID, formatted_message, parse_mode='HTML')



