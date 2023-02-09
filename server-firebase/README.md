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
