# About

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](http://forthebadge.com)

Post Git commit message on user's Facebook timeline.

# Prerequisites

- Facebook account
- GitHub account
- Heroku account
- Heroku CLI: download it [here](https://devcenter.heroku.com/articles/heroku-cli)

# How to use this application

## Heroku

- Go to any directory in your machine.

```
cd ~
```

- Clone this repository.

```
git clone https://github.com/jpdoria/github-facebook.git
```

- Change directory to `github-facebook`.

```
cd github-facebook
```

- Log on to Heroku.

```
heroku login
```

- Create a new app. Heroku will provide you your app domain. Please copy it (e.g., https://morning-waters-xxxxx.herokuapp.com/).

```
heroku create
```

- Deploy app to Heroku.

```
git push heroku master
```

## GitHub

- Log on to **[GitHub](https://github.com)** and go **[Settings > Developer settings > Integrations](https://github.com/settings/integrations)**.
- Click the **Register new integration** button.
    * Integration name: github-facebook
    * Description: Post Git commit message on user's Facebook timeline.
    * Homepage URL: https://morning-waters-xxxxx.herokuapp.com/
    * Callback URL: https://morning-waters-xxxxx.herokuapp.com/
    * Webhook URL: https://morning-waters-xxxxx.herokuapp.com/webhook
    * Webhook secret (optional): *this will be your GH_WEBHOOK_SECRET; just create a random string here.*
- Scroll down to **Permissions & events**.
    * Search for **Repository contents**.
    * Select **Read-only**
    * Tick **Push**
    * Where can this intregation be installed? Tick **Only this account**.
- Click the **Create integration** button.
- Scroll and up you will be asked to create a **Private key**.
- Back to top of the same page, click the **Install** button.
- Select **All repositories** then click the **Install** button.

## Facebook

- Log on to **[Facebook for Developers](https://developers.facebook.com)**.
- Click **My Apps** dropdown box and select **Add a New app**.
    * Display Name: *your desired app name*
    * Contact Email: *your email address*
    * Category: Productivity
- Click the **Create App ID** button.
- Complete the **Security Check (CAPTCHA)**.
- You will be redirected to **Product Setup** page.
- Find **Facebook Login** then click the **Get Started** button.
    * Valid OAuth redirect URIs: http://localhost:3000
    * Click the **Save Changes** button.
- Go to **[Tools & Support](https://developers.facebook.com/tools-and-support/) > Graph API Explorer**.
    * Application: *select the new application you've just created*
    * Click the **Get Token dropdown button > Get User Access Token**.
    * Tick **publish_actions** then click the **Get Access Token** button.
    * Allow your application to post to Facebook for you.
- Go to **[Tools & Support](https://developers.facebook.com/tools-and-support/) > Access Token Tool**.
- Find the **User Token** of your app then click the **Debug** button.
- Click the **Extend Access Token** button.
- A new long-lived access token will be generated. *This is your FB_USER_TOKEN. Just copy.*

### Heroku again.

- Set environment variables to your app.

```
heroku config:set GH_WEBHOOK_SECRET=<the webhook secret we created in GitHub>
heroku config:set FB_USER_TOKEN=<your new long-lived access token from Facebook>
```

### And finally!

- Do a `git push` now and check your Facebook timeline!

# Contribution

This project is still young and there are things that need to be done. If you have ideas that would improve this app, feel free to contribute!

# License

MIT License

Copyright (c) 2017 John Paul P. Doria

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.