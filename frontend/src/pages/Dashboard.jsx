import { useEffect,useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

function Dashboard(){
const [user,setUser]=useState(null);
const navigate=useNavigate();

const getUser=async()=>{
    try{
    const response = await api.get("/user/me")
    setUser(response.data)
    }
    catch(error){
        console.log(error)
    }
}
useEffect(()=>{
    getUser();
},[])

const handleLogout=async ()=>{
    await api.post("/user/logout")

    navigate("/")
}
    return (
               <div>
            <h1>Dashboard</h1>
            <button onClick={handleLogout} className="bg-red-600 hover:bg-red-700 cursor-pointer text-white w-80 p-2 rounded" type="submit">Logout</button>
       </div>
    )
}

export default Dashboard;