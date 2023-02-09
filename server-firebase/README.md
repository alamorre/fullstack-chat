# Coming soon!

In this post, we'll be building (and deploying) a scalable, full-stack chat application using Firebase, NextJS, and ChatEngine.io!

- Firebase is a Backend as a Service (BaaS) plaform which is made by Google.
- NextJS is a Server Side Rendering Framework (SSRF) in React JS
- ChatEngine.io provides chat APIs and components for building chat apps easily.

Here, we will connect the three to make the amazing chat app above - in about 15 minutes of work!

## 1. Setting up a firebase project

Taking a step back, let's make the folder we'll run this project inside:

```bash
mkdir chat-firebase-next
cd chat-firebase-next
code .
```

To setup a firebase project, make sure you have the [Firebase CLI](https://firebase.google.com/docs/cli) installed and a [Firebase account](https://firebase.google.com/).

Now, open a terminal in this new folder, and start a firebase project with `firebase init` command. Make sure you pick the following options below:

- Select / enable `functions`
- Select "Create a new project"
- I named my project and ID "fullstack-chat-server"
- I used Javascript, but TypeScript works too

Now, when you run a free command you should see the following:

```bash
.
├── .firebaserc
├── .gitignore
├── firebase.json
└── functions/
```

I'll list each item below:

- `.firebaserc` links this folder to your new Firebase project
- `.gitignore` ignores certain files and folders for your repo
- `firebase.json` hosts settings for your local Firebase project
- `functions` is where we'll be writing our backend code ;)

On that note, let's setup an Express JS server in Cloud Functions.

## 2. Coding your backend

We'll be connect all our Users to Chat Engine so they can use Chat Engine's chat infrastructure. The Chat Engine backend will handle all our web-sockets, chat storage, and everything else.

We need to make Rest API calls to Chat Engine whenever a new user Signs Up, and delete their account whenever they leave.

To start, hop in `functions` to install axios and hop back out:

```bash
cd functions
npm i axios
cd ..
```

The dependency `axios` will make our API calls to Chat Engine.

Open the `functions/src/index.js` file in your IDE and the following code:

```typescript
import * as functions from "firebase-functions";

exports.createChatEngineUser = functions.auth.user().onCreate((user) => {
  console.log("create", user);
});

exports.deleteChatEngineUser = functions.auth.user().onDelete((user) => {
  console.log("delete", user);
});
```

This will simple state when a user signs up or deleted their account.

To deploy this, just run `firebase deploy`. You will be prompted to enable Authentication and the Blaze plan if you haven't already.

I just enabled Google Authentication and followed the steps in the website.

```bash
firebase deploy
```

Your backend be good to go! And you should see the following in your functions tab online:

[TODO: image of firebase console]

Now, let's connect this backend to ChatEngine.io!

## 3. Connect Firebase to Chat Engine

Chat Engine's APIs let us host chatrooms on their platform, and provide us tools to build pretty chat UIs. We'll be signing up our new Firebase users to Chat Engine automatically here.

Here is the documentation on Chat Engine's APIs: https://rest.chatengine.io

In particular, we'll be using their [Create User API](https://rest.chatengine.io/#6bd8427f-d6e0-4f25-8b96-e753aa73f99a) and their [Delete User API](https://rest.chatengine.io/#902cf1ff-3f42-4430-8f0d-3a7067d3213b).

To start, go to https://chatengine.io, create an account, and set up a new Project. The Private Key and Project ID will be needed for our API calls.

Now, let's add the code to `functions/src/index.js` and be sure to replace `XXX` and `YYY` with your Private Key and Project ID, respectively.

```typescript
import * as functions from "firebase-functions";

const axios = require("axios");

exports.createChatEngineUser = functions.auth.user().onCreate((user) => {
  axios.post(
    "https://api.chatengine.io/users/",
    {
      username: user.email,
      secret: user.uid,
      email: user.email,
      first_name: user.displayName,
    },
    { headers: { "Private-Key": "8c63dbce-80a7-455a-890b-9368d16e1dcb" } }
  );
});

exports.deleteChatEngineUser = functions.auth.user().onDelete((user) => {
  axios.delete("https://api.chatengine.io/users/me/", {
    headers: {
      "Project-ID": "794653df-052a-4ad2-b0aa-d6c251a10aef",
      "User-Name": user.email,
      "User-Secret": user.uid,
    },
  });
});
```

If you're using TypeScript, you may need to modify the rules in `.eslintrc.js` like I did below:

```json
  rules: {
    // prettier-ignore
    "quotes": ["error", "double"],
    "import/no-unresolved": 0,
    // prettier-ignore
    "indent": ["off", "always"],
    "object-curly-spacing": ["off", "always"],
    "@typescript-eslint/no-var-requires": ["off", "always"],
  }
```

Our backend is complete! Now users have access to Chat Engine when they sign up and their account goes away is they delete their data!

Let's setup a frontend and connect it to Firebase and Chat Engine!

## 4. Set up the Frontend

At the top level of our project, we'll run the command below to make a NextJS project. Be sure to select the following too:

```bash
npx create-next-app@latest --ts
```

- Name the project "frontend"
- "No" for using .eslint
- "No" for using the `src/` directory
- "No" for using the `app/` directory
- "Yes" for using the `@` imports

I highly recommend TypeScript with Chat Engine, you'll see why soon :)

Now you should have a `frontend/` folder right next to `functions/`.

Let's CD into this folder and start adding code.

```bash
cd frontend
```
