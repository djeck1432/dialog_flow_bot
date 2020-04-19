# Chat-bots for Telegram and Vkontakte
 These bots will simplify customer service by answering frequently asked questions. 
 Support service can breath a little easier now

## Instruction for running code on the server

### Registration and installation of Heroku

Sign up on this  <a href='https://signup.heroku.com/dc'>site</a>.
<br>
To work through the terminal install ```CLI``` for ```Heroku```, to do this you should open ``bash`` on your computer and write in there next commands: 
<br>
For Linux  ```Linux``` -<br>
```sudo snap install heroku --classic```
<br>
For ```MacOs``` - <br>
```brew install heroku/brew/heroku```
<br>
Staying in the terminal, log into your account on ```Heroku``` with ```bash```:
<br>
```heroku login```
<br>
### Download code on Heroku

Download from ```github``` your repository to computer:
<br>
```git clone https://github.com/djeck1432/dialog_flow_bot.git```
<br>
Open the folder:
<br>
```cd dialog_flow_bot ```
<br>
Create a new app on ```Heroku``` :
<br>
```heroku create```
<br>
Download your repository on the server ```Heroku```:
<br>
```git push heroku master```
<br>
### Setting up the environment and starting the server

Go to the <a href='https://dashboard.heroku.com/apps'>link</a>, choose your app and open it.
<br>
In the navigation menu, go to the tab ```Settings```.
<br>
In chapter```Config vars```, pass your environment variables.
<br>
In the terminal, do the next command for start code on the server:<br>
```heroku ps:scale bot=1```
<br>
Congratulations, now your `` Bot`` is constantly working.
<a name='env'></a>

## Environment variables  

```TELEGRAM_ACCESS_TOKEN``` - token from your chat bot in ```telegram```;<br>
```TELEGRAM_LOG_BOT_TOKEN```- token from the bot, where they will come ```loggs```;<br>
```VK_ACCESS_TOKEN``` - token from ```vkontakte```;<br>
```GOOGLE_APPLICATION_CREDENTIALS``` - access keys to ```Google``` services.


### Bot example
1)Name of ```TelegramBot``` - ```@DevmanLesson3_bot```;
<br>
2)How does it work ```VkontakteBot``` <a href='https://vk.com/club190053871'>here</a>;
<br>
3)Chat bot with logs <a href='https://t.me/devman_log_bot'>here</a>;
<br>
<img src='https://dvmn.org/filer/canonical/1569214094/323/'></img>


### How to train a bot

1. Download the repository on your computer:<br>
```git clone https://github.com/djeck1432/dialog_flow_bot.git```
2. Open the repository: <br>
```cd dialog_flow_bot```
3. Install all needed libraries:<br>
```pip install -r requirements.txt```
4. Create a file ```.env``` and set all the variables that are described <a href='#env'>here</a><br>
5. Create a file ```file.json```in format ```json```.<br>
6. Insert into the file you created, training phrases / words of answers / questions.<br>
7. Run code:<br>
```python3 add_intent.py```

