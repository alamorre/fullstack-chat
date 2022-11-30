import { useState } from "react";
import axios from "axios";

const AuthPage = (props) => {
  const [username, setUsername] = useState();
  const [secret, setSecret] = useState();
  const [email, setEmail] = useState();
  const [first_name, setFirstName] = useState();
  const [last_name, setLastName] = useState();

  const onLogin = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:3001/login", { username, secret })
      .then((r) => props.onAuth({ ...r.data, secret })) // NOTE: over-ride secret
      .catch((e) => console.log(JSON.stringify(e.response.data)));
  };

  const onSignup = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:3001/signup", {
        username,
        secret,
        email,
        first_name,
        last_name,
      })
      .then((r) => props.onAuth({ ...r.data, secret })) // NOTE: over-ride secret
      .catch((e) => console.log(JSON.stringify(e.response.data)));
  };

  return (
    <div style={{ margin: "24px" }}>
      {/* Login Form */}
      <form onSubmit={onLogin}>
        <h3>Login</h3>
        <label>
          Username:
          <input
            type="text"
            name="username"
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Secret:
          <input
            type="password"
            name="secret"
            onChange={(e) => setSecret(e.target.value)}
          />
        </label>
        <br />
        <input type="submit" value="Login" />
      </form>
      {/* Sign Up Form */}
      <form onSubmit={onSignup}>
        <h3>or Sign Up</h3>
        <label>
          Username:
          <input
            type="text"
            name="username"
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            name="secret"
            onChange={(e) => setSecret(e.target.value)}
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="text"
            name="email"
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <br />
        <label>
          First name:
          <input
            type="text"
            name="first_name"
            onChange={(e) => setFirstName(e.target.value)}
          />
        </label>
        <br />
        <label>
          Last name:
          <input
            type="text"
            name="last_name"
            onChange={(e) => setLastName(e.target.value)}
          />
        </label>
        <br />
        <input type="submit" value="Sign Up" />
      </form>
    </div>
  );
};

export default AuthPage;
