import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8081",
});

const ApiService = {
  login: async(username: string, password: string) => {
    const response = await api.post("/auth/singin", {
      "username": username,
      "password": password
    })
    return response.data
  },
  getUser: async () => {
    const response = await api.get("/user", {
      headers: {
        Authorization: "bearer " + localStorage.getItem("system_tcc"),
      },
    })

    return response.data
  }
}

export default ApiService;