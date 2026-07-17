import { Link } from "react-router-dom";
import { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
    const response = await api.post("/user/login", { email, password });
    navigate("/dashboard");
    }
    catch (error){
        alert(error.response?.data?.detail || "Something went Wrong")
    }
  }

  return (
    <div className="w-80 mx-auto mt-20">
      <h1 className="block text-center text-2xl font-bold mb-5">Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          className="border w-full p-2 mb-3 rounded"
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="border w-full p-2 mb-4 rounded"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          className="bg-blue-600 hover:bg-blue-700 cursor-pointer  text-white w-full p-2 rounded"
          type="submit"
        >
          Login
        </button>
      </form>

      <Link
        to="/register"
        className="block text-center text-blue-600 hover:text-blue-800 underline"
      >
        Don't have an account? Register
      </Link>
    </div>
  );
}

export default Login;
