import { useState } from "react";
import Login from "./pages/Login";
import { Routes, Route } from "react-router-dom";
import Register from "./pages/Register";
import { Link } from "react-router-dom";
import TodoList from "./pages/TodoList";
import ProtectedRoute from "./components/ProtectedRoute";
import PublicRoute from "./components/PublicRoute";
import TodoDetails from "./pages/TodoDetails";

function App() {
  const [count, setCount] = useState(0);

  return (
    <Routes>
      <Route path="/todos/:id" element ={<ProtectedRoute><TodoDetails/></ProtectedRoute>}/>
      <Route path="/" element={<PublicRoute><Login /></PublicRoute>} />
      <Route path="/register" element={<Register />} />
      <Route
        path="/todos"
        element={
          <ProtectedRoute>
            <TodoList />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

export default App;
