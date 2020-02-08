# Чат-боты для ```Telegram``` и ```Vkontakte```
С помощью даных ботов, упростили работу с клиентами, где подготовили заранее готовые ответы на их часто задаваемы вопросы.
Теперь, служба поддержки может вздохнуть не много.

## Инструкция по запуску кода на сервере

### Регистрация и установка Heroku

Зарегистрируйтесь  на этом <a href='https://signup.heroku.com/dc'>сайте</a>.
<br>
Для работы через терминал, установите ```CLI``` для ```Heroku```, для этого
откройте у себя на компьютере ```bash``` и в нем пропишите следующие команды: 
<br>
Для ```Linux``` -<br>
```sudo snap install heroku --classic```
<br>
Для ```MacOs``` - <br>
```brew install heroku/brew/heroku```
<br>
Оставаясь в терминал, зайдите через ```bash``` в ваш аккаунт на ```Heroku```:
<br>
```heroku login```
<br>
### Загрузка кода на сервер Heroku

Загрузите с ```github``` ваш репозиторий на компьютер: 
<br>
```git clone https://github.com/djeck1432/dialog_flow_bot.git```
<br>
Откройте папку:
<br>
```cd dialog_flow_bot ```
<br>
Создайте приложения в ```Heroku``` :
<br>
```heroku create```
<br>
Загрузите ваш репозиторий на сервер ```Heroku```:
<br>
```git push heroku master```
<br>

### Настройка окружения и запуск сервера

Перейдите по <a href='https://dashboard.heroku.com/apps'>ссылке</a>, выберете свое приложения и откройте его
<br>
В меню навигации, перейдите на вкладку ```Settings```.
<br>
В разделе ```Config vars```, передайте ваши переменные окружения.
<br>
В терминале, выполните следующую команду для запуска кода на сервере:<br>
```heroku ps:scale bot=1```
<br>
Поздравляю, теперь ваш ```Bot``` работает постоянно, вне зависимости, включен ваш компьютер или нет.

### Переменые окружения 
```TELEGRAM_TOKEN_ACCESS``` - токен от вашего чат-бота в ```telegram```;<br>
```TELEGRAM_LOG_BOT_TOKEN```-токен от бота, куда будут приходить ```loggs```;<br>
```VK_TOKEN_ACCESS``` - токен от ```vkontakte```;<br>
```GOOGLE_APPLICATION_CREDENTIALS``` - ключи доступа к ```Google``` сервисам.


## Пример работы бота 
1)Названия ```TelegramBot``` - ```@DevmanLesson3_bot```;
<br>
2)Как работает ```VkontakteBot``` <a href='https://vk.com/club190053871'>здесь</a>;
<br>
3)Чат бот с логами <a href='https://t.me/devman_log_bot'>здесь</a>;
<br>
<img src='https://dvmn.org/filer/canonical/1569214094/323/'></img>
