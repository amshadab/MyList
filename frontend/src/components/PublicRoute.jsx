import { Navigate } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/api";


function PublicRoute({ children }) {

    const [loading, setLoading] = useState(true);
    const [user, setUser] = useState(null);


    useEffect(() => {

        const checkUser = async () => {

            try {

                const response = await api.get("/user/me");

                setUser(response.data);

            }
            catch(error) {

                setUser(null);

            }
            finally {

                setLoading(false);

            }

        };


        checkUser();

    }, []);



    if(loading) {
        return <h1>Loading...</h1>;
    }


    if(user) {
        return <Navigate to="/todos" replace />;
    }


    return children;

}


export default PublicRoute;