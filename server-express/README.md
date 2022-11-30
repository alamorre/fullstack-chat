# Connect Express to Chat Engine!

This simple repo shows how to easily add chat functionality into an Express project with [Chat Engine](https://chatengine.io).

To understand the code, please watch [this video]()!

## Setup Steps

Make your express server support chat - in 3 steps:

### 1 - Setup a Chat Engine server

Go to [Chat Engine](https://chatengine.io) to setup your own chat server.

- Click "New Project" and follow the steps
- Your `Project ID` and `Private Key` will be required for step 2

### 2 - Connect `.env` to Chat Engine

We will connect to your Chat Engine server with environment varibles.

This allows you to connect to different chat-servers in local vs staging vs production.

Replace the UUIDs below with your own. In `.env` write:

```
CHAT_ENGINE_PROJECT_ID=5d498a31-cd23-42b7-b367-4fcc9463bd2f
CHAT_ENGINE_PRIVATE_KEY=49a46286-91c3-4f9c-92bf-284ae51b7628
```

### 3 - Install & Start

Run the following two lines of code in `server-express/`.

```
npm install
npm run start
```

Done! Your Express server is on `localhost:3001` and connected to Chat Engine!

All new `/signup` users are on Chat Engine, and their credentiuals are found upon `/login`.

To understand the code, please watch [this video]()!
