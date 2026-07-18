import { useState } from 'react'
import Login from './pages/Login'
import { Routes, Route } from "react-router-dom";
import Register from "./pages/Register"
import Dashboard from './pages/Dashboard';
import { Link } from 'react-router-dom';
import TodoList from "./pages/TodoList"

function App() {
  const [count, setCount] = useState(0)

  return (
<Routes>
  <Route path='/' element={<Login/>}/>
  <Route path='/register' element={<Register/>}/>
  <Route path='/dashboard' element={<Dashboard/>}/>
  <Route path="/todos" element={<TodoList/>}/>
</Routes>
  )
}

export default App
