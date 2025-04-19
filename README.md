
![](logo.jpg)
# Introduction

Several apps exist to send you notifications about words, but none of them _**let you configure what words you wanna learn**_. That is something you can write yourself, or ask GPT to do it for you. 

Everyone learns at a different pace, and wants differnt words. Given how this is a basic thing, it must be free, and in your control. 

Which is why this bot exists. So you can send yourself notifications about words you want. And see its definition and meaning every day. 

# Usage

1. Create a bot in telegram via botfather, get its token. 
2. Get your chat id by sending a message 
    A. Start a conversation with your bot (say /start).

    B. Visit this URL (replace YOUR_BOT_TOKEN with your bot’s token):
    ```
    https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
    ```
    C. Send a message to your bot in Telegram and refresh that URL — you’ll see a JSON response.

    D. Look for chat → id. That’s your chat ID.

3. clone this repo to get docker-compose-demo.yml file. edit it, put your tokens there. 
4. Run docker compose up -d, and that should be it. 
5. Add new words by adding them to words.csv, and then running `docker compose run --rm word_importer`
# Thanks
To chat gpt, and the wonderful library maintaners of Python telegram bot. And ofcourse telegram itself.

Honorable mention to [Daily Word App](https://play.google.com/store/apps/details?id=com.pramod.dailyword&hl=en_IN) on the play store, which has a pretty great and consistant notification system, but only shows you new words from [Merriam Webster](https://www.merriam-webster.com/), and their word of the Day.