from flask import Flask, request
import os
import time

app = Flask(__name__)

# List of distracting applications to close
distracting_apps = ['spotify', 'discord', 'slack']

# List of distracting websites to block
distracting_websites = [
    'www.facebook.com',
    'www.youtube.com',
    'www.twitter.com',
    'www.instagram.com',
]

# Hosts file path
hosts_file_path = '/etc/hosts'
redirect_ip = '127.0.0.1'

def block_websites():
    with open(hosts_file_path, 'r+') as file:
        content = file.read()
        for website in distracting_websites:
            if website not in content:
                file.write(f'{redirect_ip} {website}\n')

def unblock_websites():
    with open(hosts_file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(website in line for website in distracting_websites):
                file.write(line)
        file.truncate()

def close_applications():
    for app in distracting_apps:
        os.system(f'pkill {app}')

@app.route('/focus', methods=['POST'])
def focus_mode():
    data = request.get_json()
    if data['intent'] == 'LockInIntent':
        block_websites()
        close_applications()
        # Lock the screen (Linux example, use appropriate command for your OS)
        os.system('gnome-screensaver-command -l')
        return 'Focus mode activated', 200
    return 'Invalid request', 400

if __name__ == '__main__':
    app.run(port=5000)
