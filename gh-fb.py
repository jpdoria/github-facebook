import hashlib
import hmac
import os
import facebook
from flask import Flask, request


app = Flask(__name__)


def fb_post(author, repo_name, repo_url, commit_message, commit_id, description):
    """
    This function receives the params from the webhook() then invokes the put_wall_post() to create a new post on
    the user's timeline on Facebook.
    """
    fb = facebook.GraphAPI(access_token=os.environ['FB_USER_TOKEN'], version='2.7')
    picture = 'https://cdn.lazyadm.in/Octocat/Octocat.jpg'
    attachment = {
        'name': '[GitHub] {0}/{1}'.format(author, repo_name),
        'link': repo_url,
        'caption': 'GitHub',
        'description': description,
        'picture': picture
    }

    fb.put_wall_post(message='[{0}] {1} | {2} - {3}'.format(commit_id, repo_name, commit_message, author),
                     attachment=attachment)


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Compute the hash using GH_WEBHOOK_SECRET and ensure that the hash from GitHub matches.

    Reference: https://developer.github.com/webhooks/securing/
    """
    x_hub_signature = request.headers.get('X-Hub-Signature')

    if x_hub_signature is None:
        return 404
    else:
        sha_name, signature = x_hub_signature.split('=')
        mac = hmac.new(bytes(os.environ['GH_WEBHOOK_SECRET'], 'utf-8'), msg=request.data, digestmod=hashlib.sha1)

        if hmac.compare_digest(mac.hexdigest(), signature):
            print('Hash OK')
        else:
            print('Forbidden')
            return 'Forbidden', 403

    """
    Basically, this retrieves information after pushing a code to GitHub. Information like: author, repository name,
    repository URL, commit message, and timestamp.

    An example of webhook payload can be found here:
    https://developer.github.com/v3/activity/events/types/#webhook-payload-example-19
    """
    data = request.get_json()
    author = data['head_commit']['author']['username']
    repo_name = data['repository']['name']
    repo_url = data['repository']['url']
    commit_message = data['head_commit']['message']
    commit_id = data['head_commit']['id'][:7]
    description = data['repository']['description']

    fb_post(author, repo_name, repo_url, commit_message, commit_id, description)
    print('Post OK')
    return 'OK', 200


@app.route('/', methods=['GET'])
def main():
    return """<!DOCTYPE html>
<head>
    <title>Whoa!</title>
</head>
<body>
    <h1>o_O</h1>
    <p>A visitor from the unknown! Hello, are you doing?</p>
    <img src="http://loremflickr.com/600/400/">
</body>""", 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)