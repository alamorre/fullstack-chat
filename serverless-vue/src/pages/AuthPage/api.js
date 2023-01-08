import axios from "axios";

const login = (username, password) => {
  return axios.post("/login", { username, password });
};

const signup = (username, password) => {
  return axios.post("/signup", { username, password });
};

export { login, signup };
