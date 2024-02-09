import json
from flask import Flask, jsonify
from mastodon import Mastodon

app = Flask(__name__)

# Load the configuration from the JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

access_token = config['access_token']
api_base_url = config['api_base_url']

mastodon = Mastodon(access_token=access_token, api_base_url=api_base_url)

@app.route('/posts/<username>')
def get_posts(username):
    # Retrieve all toots of the user
    toots = mastodon.account_statuses(username)
    
    # Extract the URLs from the toots and compile a list
    post_urls = []
    for toot in toots:
        post_urls.append(toot['url'])

    return jsonify(post_urls)

if __name__ == '__main__':
    app.run(debug=True)
