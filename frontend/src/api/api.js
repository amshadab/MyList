import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,
});

const plainApi = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,
});

api.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    if (  error.response?.status === 401 &&
        !originalRequest._retry &&
        originalRequest.url !== "/user/refresh") {
      if (originalRequest._retry) {
        return Promise.reject(error);
      }
      originalRequest._retry = true;
      try {
        await plainApi.post("/user/refresh");
        return api(originalRequest);
      } catch (error) {
        console.log("Refresh token Expire");
        await plainApi.post("/user/logout");
        window.location.href = "/";
      }

      console.log("Access token expire");
    }
    return Promise.reject(error);
  },
);

export default api;
