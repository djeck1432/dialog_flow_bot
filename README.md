# Chat-bots for Telegram and Vkontakte
 These bots will simplify customer service by answering frequently asked questions. 
 Support service can breath a little easier now
 <br>
 [link](https://t.me/dialogflow_example_bot)
 
### Training phrases
#### First intent
 `How to get a job with you?`<br>
 `How to work for you?`<br>
 `How to work for you`<br>
 `Is it possible to get a job with you?`<br>
 `Can I work for you?`<br>
 `I want to work as an editor for you`<br>
 
 #### Second intent
 `I can't sign in to my account`<br>
 `Login failed`<br>
 `Incorrect login or password`<br>
 `How to recover your password`<br>
 `Restore password`<br>
 `Forgot login`<br>
 `Login Problems`<br>
 `I can not enter`<br>
 `I do not remember the password`<br>
 
 #### Third intent
`How to demolish your account`<br>
`Delete my articles`<br>
`How to delete data about me`<br>
`How to delete an account`<br>
`Delete account`<br>
`I want to delete my account`<br>

#### Fourth intent
`Is the contract already in force?`<br>
`When do we sign the contract?`<br>
`I am sending the results of the meeting`<br>
`Late for a meeting`<br>
`I will transfer money under the contract soon`<br>
`When will you transfer money under the contract?`<br>
`Where is the meeting?`<br>

### Bot example

<img src='https://dvmn.org/filer/canonical/1569214094/323/'></img>

<ol>
 <li>Name of TelegramBot - @DevmanLesson3_bot;</li>
 <li>How does it work VkontakteBot <a href='https://vk.com/club190053871'>here</a>;</li>
 <li>Chatbot with logs <a href='https://t.me/devman_log_bot'>here</a>;</li> 
</ol>

## Instruction for running code on the server

### Registration and installation of Heroku

Sign up on this  <a href='https://signup.heroku.com/dc'>site</a>.
<br>
To work through the terminal install `CLI` for `Heroku`, to do this you should open `bash` on your computer and write in there next commands: 
<br>
For Linux  `Linux` -
```
sudo snap install heroku --classic
```
For `MacOs` - 
```
brew install heroku/brew/heroku
```
Staying in the terminal, log into your account on `Heroku` with `bash`:
```heroku login```
<br>
### Download code on Heroku

Download from `github` your repository to computer:
```
git clone https://github.com/djeck1432/dialog_flow_bot.git
```
Open the folder:
```
cd dialog_flow_bot
```
Create a new app on `Heroku` :
```
heroku create
```
Download your repository on the server `Heroku`:
```
git push heroku master
```

### Setting up the environment and starting the server

Go to the <a href='https://dashboard.heroku.com/apps'>link</a>, choose your app and open it.

In the navigation menu, go to the tab `Settings`.

In chapter `Config vars`, pass your environment variables.

In the terminal, do the next command for start code on the server:

`heroku ps:scale bot=1`

Congratulations, now your `Bot` is constantly working.

<a name='env'></a>

## Environment variables  

`TELEGRAM_ACCESS_TOKEN` - token from your chatbot in `Telegram`;

`TELEGRAM_LOG_BOT_TOKEN`- token from the bot, where they will come `logs`;

`VK_ACCESS_TOKEN` - token from `Vkontakte`;

`GOOGLE_APPLICATION_CREDENTIALS` - access keys to `Google` services.



### How to train a bot

1. Download the repository on your computer:
```
git clone https://github.com/djeck1432/dialog_flow_bot.git
```
2. Open the repository:
```
cd dialog_flow_bot
```
3. Install all the needed libraries:
```
pip install -r requirements.txt
```
4. Create a file `.env` and set all the variables that are described <a href='#env'>here</a><br>
5. Create a file `file.json` in format `JSON`.<br>
6. Insert into the file you created, training phrases/words of answers/questions.<br>
7. Run code:<br>
```
python3 add_intent.py
```

