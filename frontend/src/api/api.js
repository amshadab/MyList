import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    withCredentials: true,
});


api.interceptors.response.use(
    (response) => response,

    async (error) => {

        const originalRequest = error.config;


        // If refresh request itself fails, stop
        if (originalRequest.url === "/user/refresh") {
            return Promise.reject(error);
        }


        // Try refresh only once
        if (
            error.response?.status === 401 &&
            !originalRequest._retry
        ) {

            originalRequest._retry = true;

            try {

                await api.post("/user/refresh");

                return api(originalRequest);

            }
            catch(refreshError) {

                return Promise.reject(refreshError);

            }
        }


        return Promise.reject(error);
    }
);


export default api;