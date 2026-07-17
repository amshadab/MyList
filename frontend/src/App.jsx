import { useState } from 'react'
import Login from './pages/Login'
import { Routes, Route } from "react-router-dom";
import Register from "./pages/Register"
import Dashboard from './pages/Dashboard';
import { Link } from 'react-router-dom';

function App() {
  const [count, setCount] = useState(0)

  return (
<Routes>
  <Route path='/' element={<Login/>}/>
  <Route path='/register' element={<Register/>}/>
  <Route path='/dashboard' element={<Dashboard/>}/>
</Routes>
  )
}

export default App
