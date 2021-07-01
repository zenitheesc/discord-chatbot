<h1 align="center" style="color:white; background-color:black">ChatBot - Cavalo Caminhão</h1>
<h4 align="center">A bot that interacts in the chat, performs counts and makes meeting reminders for the Discord platform</h4>

<p align="center">
	<a href="http://zenith.eesc.usp.br/">
    <img src="https://img.shields.io/badge/Zenith-Embarcados-black?style=for-the-badge"/>
    </a>
    <a href="https://eesc.usp.br/">
    <img src="https://img.shields.io/badge/Linked%20to-EESC--USP-black?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/ZenView/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/zenitheesc/ZenView?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/ZenView/issues">
    <img src="https://img.shields.io/github/issues/zenitheesc/ZenView?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/ZenView/commits/main">
    <img src="https://img.shields.io/github/commit-activity/m/zenitheesc/ZenView?style=for-the-badge">
    </a>
    <a href="https://github.com/zenitheesc/ZenView/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/zenitheesc/ZenView?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/ZenView/commits/main">
    <img src="https://img.shields.io/github/last-commit/zenitheesc/ZenView?style=for-the-badge"/>
    </a>
    <a href="https://github.com/zenitheesc/ZenView/issues">
    <img src="https://img.shields.io/github/issues-raw/zenitheesc/ZenView?style=for-the-badge" />
    </a>
    <a href="https://github.com/zenitheesc/ZenView/pulls">
    <img src = "https://img.shields.io/github/issues-pr-raw/zenitheesc/ZenView?style=for-the-badge">
    </a>

</p>

<p align="center">
    <a href="#environment-and-tools">Environment and Tools</a> •
    <a href="#steps-to-run-and-debug">Steps to run and debug</a> •
    <a href="#how-to-contribute">How to contribute?</a> •
</p>

## Environment and tools

- [Google Sheets](https://www.google.com/sheets/about/): worksheets "commands" and "triggers" (recommended to create "manual").
- [Python](https://www.python.org/)
- [Dicord/DeveloperPortal](https://discord.com/developers/applications)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)

## Steps to run and debug

It's necessary to create a project on Heroku cloud server and import the repository there; to create a database on MongoDB (recommended Atlas) with the desired collections; to make spreadsheet with the commands and other with triggers; and start a new application on the Discord plataform to generate your bot.

To start, enter [Discord/DeveloperPortal](https://discord.com/developers/applications) and follow the steps described below:   
In applications, press 'New Application'> Name your bot > Make a description of it > Click in Bot (left bar) and click in 'Add Bot'> Copy the Discord Token and save it in `.env.example` file > In 'OAuth2' (left bar) > Select 'bot' in the scopes > List your permissions and save changes > Use a URL given in the 'scopes' area to open a website > Select which server you want to host the bot commands on. Your Bot is online.

To create a collections in the MongoDB Atlas, you can follow the steps described below:   
You need create a new project > In this project, create a Cluster > Save the connection URI in the `.env.example` > Click on the "Collections" button on the top bar > + Create Database > Name the database and collection that will be created > Insert Document > You'll initially create three documents for this bot - 1. `byProject` and `byDay` (empty objects); 2. `roles` (empty array); 3. `counters` (object), this object receives the commands keys of `Counters.py` > Cluster, database and collection must be named `discord-bot`

You need these `.env` files to connect all plataforms to run this bot project: a new application token on the Discord Developer Portal; your Google’s API `credentials.env` and `.json` (help in this [video](https://www.youtube.com/watch?v=cnPlKLEGR7E) ); the MongoDB database URI. Replace them properly in the code.

The bot`ll reply to commands with prefixe ‘>’ and triggers on_message ( ) specified in a Google Sheets (you have to create ‘commands’ and ‘triggers’ worksheets’).


## How to contribute

If you want to collaborate with the project, make a **Fork** and a descriptive **Pull Request** explain your moddifications.

Please, contact us if you find problems or have a suggestion to the project. We will be grateful for your help.

---

<p align="center">
    <a href="http://zenith.eesc.usp.br">
    <img src="https://img.shields.io/badge/Check%20out-Zenith's Oficial Website-black?style=for-the-badge" />
    </a> 
    <a href="https://www.facebook.com/zenitheesc">
    <img src="https://img.shields.io/badge/Like%20us%20on-facebook-blue?style=for-the-badge"/>
    </a> 
    <a href="https://www.instagram.com/zenith_eesc/">
    <img src="https://img.shields.io/badge/Follow%20us%20on-Instagram-red?style=for-the-badge"/>
    </a>

</p>
<p align = "center">
<a href="zenith.eesc@gmail.com">zenith.eesc@gmail.com</a>
</p>