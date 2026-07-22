import { useState, useEffect } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

function TodoList() {
  const [list, setList] = useState([]);
  const [title, setTitle] = useState("");
  const navigate = useNavigate();
  const [user, setUser] = useState(null);

  const deleteTodo = async (id) => {
    try {
      const response = await api.delete(`/list/delete/${id}`);
      console.log(response);
      getList();
    } catch (error) {
      console.log(error);
    }
  };

  const getUser = async () => {
    try {
      const response = await api.get("/user/me");
      setUser(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const getList = async () => {
    try {
      const response = await api.get("/list/get_todo");
      setList(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const renameTodo = async(id,oldTitle)=>{
    const newTitle = prompt("Enter New Title",oldTitle)
    if(!newTitle || newTitle.trim()===""){
      return;
    }
    try{
      await api.put(`/list/update/${id}`,{title:newTitle})
      getList();
    }
    catch(error){
      console.log(error);
      
    }
  }

  const todoTitle = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post("/list/create", {
        title: title,
      });

      console.log(response);

      getList();
      setTitle("");
    } catch (error) {
      console.log(error.response);
    }
  };

  useEffect(() => {
    getList();
    getUser();
  }, []);

  const handleLogout = async () => {
    await api.post("/user/logout");
    navigate("/");
  };

  return (
    <div>
      <div className="flex justify-between items-center bg-gray-800 text-white px-6 py-4">
        <h1>MyList</h1>

        <div className="flex items-center gap-4">
          <h1 className="capitalize">
            {user && `${user.fname} ${user.lname}`}
          </h1>

          <button
            onClick={handleLogout}
            className="bg-red-600 hover:bg-red-700 cursor-pointer text-white w-20 p-2 rounded"
          >
            Logout
          </button>
        </div>
      </div>

      {/* Create Todo */}
      <form className="flex justify-center p-5" onSubmit={todoTitle}>
        <input
          className="border w-80 p-2 rounded"
          type="text"
          placeholder="College"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <button className="w-25 bg-green-800 hover:bg-green-900 cursor-pointer mx-2 text-white p-2 rounded">
          Add List
        </button>
      </form>

      {/* Todo List */}
      {list.map((item) => (
        <div
          key={item.id}
          onClick={() => navigate(`/todos/${item.id}`)}
          className="flex ml-2 mr-2 justify-between items-center border p-3 rounded mb-2 cursor-pointer"
        >
          <span>{item.title}</span>
          <div className="flex gap-2">
<button onClick={(e)=>{
  e.stopPropagation();
  renameTodo(item.id);
}} className="w-15 cursor-pointer bg-blue-800 text-white hover:bg-blue-900 rounded p-2">Edit</button>
          <button
            onClick={(e) => {
              e.stopPropagation();
              deleteTodo(item.id);
            }}
            className="w-15 cursor-pointer bg-red-800 text-white hover:bg-red-900 rounded p-2"
          >
           <span>&#128465;</span>
          </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default TodoList;
