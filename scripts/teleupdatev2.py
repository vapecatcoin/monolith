import argparse
import os
import telebot
import random
from telebot import types

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

GIFS_ARRAY = [
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat2.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat3.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat4.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat5.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat6.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat7.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat8.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat9.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat10.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat11.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat12.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat13.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat14.gif",
    "https://raw.githubusercontent.com/vapecatcoin/cdn/main/cat15.gif",
]

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

def send_formatted_message_with_gif(url):
    dex_tools_url = "https://www.dextools.io/app/en/bnb/pair-explorer/0xa77ba1446c11e0ef90b3e39d1c3c7a05d8f680b2"
    alpha_dapp = "https://vapecat.xyz/alpha"
    gif_url = random.choice(GIFS_ARRAY)
    formatted_message = f"ℹ️ <b>New Event on GitHub</b>" \
                    f"\n\n" \
                    f"📁 <b>Repository:</b> {repository}" \
                    f"\n🔔 <b>Event name:</b> {event_name}" \
                    f"\n🌿 <b>Branch:</b> {branch}" \
                    f"\n👤 <b>Actor:</b> {actor}" \
                    f"\n👥 <b>Repository owner:</b> {repository_owner}"
    
    # add buttons on bottom
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='See on Github', url=url)
    button2 = types.InlineKeyboardButton(text='Dextools', url=dex_tools_url)
    keyboard.add(button)
    keyboard.add(button2)

    bot.send_animation(DEV_CHAT_ID, gif_url, caption=formatted_message, parse_mode='HTML', reply_markup=keyboard)

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

        send_formatted_message_with_gif(github_pr_url)

    else:
        print("This is not a pull request")
        # make commit url for the push event
        if event_name == 'push':
            print(commit_url)
            send_formatted_message_with_gif(commit_url)
        
if __name__ == "__main__":
    main()