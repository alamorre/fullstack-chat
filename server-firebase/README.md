# Build a scalable chat app with Firebase, Next JS, and ChatEngine.io

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

Important side note: Replace `styles/gloabl.css` with [the following code too](https://raw.githubusercontent.com/alamorre/fullstack-chat/main/server-firebase/frontend/styles/globals.css).

Let's CD into this folder, install dependencies, and run in dev-mode.

```bash
cd frontend
npm install
npm run dev
```

And now you should see a pretty website on http://localhost:3000

For the final push, let's add all the code we need to our frontend!

## 5. Coding the Frontend

To start, diable StrictMode in `next.config.js` and re-run the server with `yarn dev`.

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
};

module.exports = nextConfig;
```

This allows us to connect web-sockets in a NextJS project.

Next, let's delete the following:

- `styles/Home.module.css`
- The `pages/api` directory

Next, let's create an auth page (`pages/AuthPage.tsx`) with the following code

```typescript
export default function Page() {
  return <div />;
}
```

Next, let's create an chats page (`pages/ChatsPage.tsx`) with the following code

- `pages/ChatsPage.tsx`

```typescript
import { User } from "firebase/auth";

interface ChatProps {
  user: User;
}

export default function Page(props: ChatProps) {
  return <div />;
}
```

Next, add a loading page (`pages/Loading.tsx`) with the following code:

```typescript
export default function Loading() {
  return (
    <div className="page">
      <div className="logo">☝️</div>
      <div className="text">Loading your info...</div>
    </div>
  );
}
```

Finally, modify the `pages/index.tsx` file to load the pages based on auth state:

```typescript
import { useState } from "react";

import AuthPage from "./AuthPage";
import ChatPage from "./ChatsPage";
import Loading from "./Loading";
import { auth } from "@/firebase";
import { User } from "firebase/auth";

export default function Home() {
  const [user, setUser] = useState<User | null>();
  auth.onAuthStateChanged((user) => setUser(user));

  if (user === undefined) {
    return <Loading />;
  } else if (user === null) {
    return <AuthPage />;
  } else {
    return <ChatPage user={user} />;
  }
}
```

### Enable a Firebase app and create frontend/firebase.ts

- npm install firebase
- create a .env file and replace with your values

```
NEXT_PUBLIC_FIREBASE_API_KEY=AIzaSyDqXgd1AwRdqSCpdrhf_t0-rB1MuE2sd4A
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=chat-rce.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=chat-rce
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=chat-rce.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=45443650042
NEXT_PUBLIC_FIREBASE_APP_ID=1:45443650042:web:2598e30783c0e0bd545443
NEXT_PUBLIC_FUNCTIONS_URL=https://us-central1-chat-rce.cloudfunctions.net/v1
NEXT_PUBLIC_CHAT_ENGINE_PROJECT_ID=16b08e85-e4c9-4541-b30e-45e157ec3821
```

Make sure `NEXT_PUBLIC_CHAT_ENGINE_PROJECT_ID` is there with yuor project ID.

- add this code to firebase.ts

```
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
```

Now add this code to AuthPage:

```
import { auth } from "@/firebase";
import { signInWithRedirect, GoogleAuthProvider } from "firebase/auth";

export default function AuthPage() {
  const onClick = () => {
    signInWithRedirect(auth, new GoogleAuthProvider());
  };

  return (
    <div className="page">
      <div className="logo">👋 💬 🤖 </div>
      <div className="text">Welcome to ChatRCE</div>
      <div className="text" style={{ paddingBottom: "16px" }}>
        Log in with your account to continue
      </div>
      <button className="button" onClick={onClick}>
        Log In
      </button>{" "}
      <button className="button" onClick={onClick}>
        Sign Up
      </button>
    </div>
  );
}
```

Finally, let's connect our new user to Chat Engine using [react-chat-engine-pretty](https://www.npmjs.com/package/react-chat-engine-pretty)!

Modify `pages/ChatsPage.tsx` with the following code:

```typescript
import { auth } from "@/firebase";
import { signOut, User } from "firebase/auth";
import { PrettyChatWindow } from "react-chat-engine-pretty";
interface ChatProps {
  user: User;
}

export default function Page(props: ChatProps) {
  return (
    <div style={{ height: "100vh" }}>
      <button
        style={{ position: "absolute", top: "0px", left: "0px" }}
        onClick={() => signOut(auth)}
      >
        Sign Out
      </button>
      <PrettyChatWindow
        projectId={process.env.NEXT_PUBLIC_CHAT_ENGINE_PROJECT_ID || ""}
        username={props.user.email || ""}
        secret={props.user.uid}
        style={{ height: "100%" }}
      />
    </div>
  );
}
```

And we're done!
