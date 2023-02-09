import { useState } from "react";

import AuthPage from "./AuthPage";
import ChatsPage from "./ChatsPage";

function App() {
  const [user, setUser] = useState();

  if (!user) {
    return <AuthPage />;
  } else {
    return <ChatsPage />;
  }
}

export default App;
