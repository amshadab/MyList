import { useState, useEffect } from "react";
import api from "../api/api";

function TodoList() {
  const [list, setList] = useState([]);
  const [title,setTitle]=useState("")

  const getList = async () => {
    const response = await api.get("/list/get_todo");
    setList(response.data);
  };

  const todoTitle = async (e)=>{
    e.preventDefault();
    await api.post("/list/create",{title:title})
    getList();
    setTitle("")
  }

  useEffect(() => {
    getList();
  }, []);


  return (
    <div>
      <h1 className="flex justify-center">MyList</h1>
      <form className="flex justify-center p-5" onSubmit={todoTitle}>
      <input className="border w-80 p-2 rounded" type="text"  placeholder="College" value={title} onChange={(e)=>setTitle(e.target.value)}/>
      <button className="w-50 bg-blue-600 hover:bg-blue-700 cursor-pointer mx-2 text-white p-2 rounded">Add Task</button>
      </form>
      {
        list.map((item)=>(
            <div className="flex ml-2 mr-2 justify-between items-center border p-3 rounded mb-2" key={item.id}>{item.title}
            <button className="w-50 cursor-pointer bg-blue-600 text-white hover:bg-red-700 rounded p-2 ">Delete</button>
            </div>
        ))
      }
    </div>
  );
}

export default TodoList;
