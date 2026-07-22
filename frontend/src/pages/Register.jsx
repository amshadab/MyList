import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/api";

function Register() {
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const registerUser = async (e) => {
    e.preventDefault();

    if (
  fname.trim() === "" ||
  lname.trim() === "" ||
  email.trim() === "" ||
  password.trim() === ""
) {
  alert("All fields are required");
  return;
}

    try {
      await api.post("/user/register", {
        fname,
        lname,
        email,
        password,
      });

      alert("Registration Successful");

      setFname("");
      setLname("");
      setEmail("");
      setPassword("");

      navigate("/");
    } catch (error) {
      alert(error.response?.data?.detail || "Something went wrong");
    }
  };
  return (
    <div className="w-80 mx-auto mt-20">
      <h1 className="block text-center text-2xl font-bold mb-5">Register</h1>

      <form onSubmit={registerUser}>
        <input
          className="border w-full p-2 mb-3 rounded"
          type="text"
          placeholder="First Name"
          value={fname}
          onChange={(e) => {
            setFname(e.target.value);
          }}
        />
<input className="border w-full p-2 mb-3 rounded" type="text" placeholder="Last Name" value={lname} onChange={(e)=>{setLname(e.target.value)}} />

 <input
          className="border w-full p-2 mb-3 rounded"
          type="email"
          placeholder="Email"
          autoComplete="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          className="border w-full p-2 mb-4 rounded"
          type="password"
          placeholder="Password"
          autoComplete="new-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          className="bg-green-600 hover:bg-green-700 cursor-pointer text-white w-full p-2 rounded"
          type="submit"
        >
          Register
        </button>
        
      </form>
      <Link to="/" className="block text-center text-blue-600 hover:text-blue-800 underline mt-3">  Already have an account? Login</Link>
    </div>
  );
}

export default Register;
