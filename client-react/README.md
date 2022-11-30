# Connect React to Chat Engine!

This simple repo shows how to easily add chat functionality into a React project with [Chat Engine](https://chatengine.io).

To understand the code, please watch [this video]()!

## Setup Steps

Setup this chat client in 3 steps below.

These steps assume you have already setup one of the server projects in `../server-*` (for example, `server-express`).

### 1 - Setup a Chat Engine server

Go to [Chat Engine](https://chatengine.io) to setup your own chat server.

- Click "New Project" and follow the steps
- Your `Project ID` and `Private Key` will be required for step 2

### 2 - Connect `.env` to Chat Engine

We will connect to your Chat Engine server with environment varibles.

This allows you to connect to different chat-servers in local vs staging vs production.

Replace the UUID below with your own. In `.env` write:

```
REACT_APP_CHAT_ENGINE_PROJECT_ID=5d498a31-cd23-42b7-b367-4fcc9463bd2f
```

### 3 - Install & Start

Run the following two lines of code in `client-react/`.

```
npm install
npm run start
```

Done! Your Express server is on `localhost:3000` and connected to Chat Engine!

All new "Sign Up" users are on Chat Engine, and their credentiuals are found upon "Login".

To understand the code, please watch [this video]()!
