import { useState, useEffect } from "react";
import api from "../api/api";

function TodoList() {
  const [list, setList] = useState([]);
  const [title,setTitle]=useState("")

  const getList = async () => {
    const response = await api.get("/list/get_todo");
    setList(response.data);
  };

  const todoTitle = async ()=>{
    await api.post("/list/create",{title:title})
    getList();
    setTitle("")
  }

  useEffect(() => {
    getList();
  }, []);


  return (
    <div>
      <h1>TodoList</h1>
      <input className="border w-80 p-2 mb-4 rounded" type="text"  placeholder="College" value={title} onChange={(e)=>setTitle(e.target.value)}/>
      <button className="w-50 bg-blue-600 hover:bg-blue-700 cursor-pointer mx-2 text-white p-2 rounded" onClick={todoTitle}>Add Task</button>
      {
        list.map((list)=>(
            <div key={list.id}>{list.title}</div>
        ))
      }
    </div>
  );
}

export default TodoList;
