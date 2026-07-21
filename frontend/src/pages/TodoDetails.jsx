import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api from "../api/api";

function TodoDetails() {
  const { id } = useParams();
  const [todo, setTodo] = useState(null);
  const [taskTitle, setTaskTitle] = useState("");

  const getTodo = async () => {
    try {
      const response = await api.get(`/list/get_by_id/${id}`);
      setTodo(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const createTaskTitle = async (e) => {
    e.preventDefault();

    try {
      if (taskTitle.trim() === "") {
        alert("Task title cannot be empty");
        return;
      }

      await api.post(`/task/create/${id}`, {
        title: taskTitle
      });

      getTodo();
      setTaskTitle("");

    } catch (error) {
      console.log(error);
    }
  };

  const deleteTask=async (id)=>{
    try{
    await api.delete(`/task/delete/${id}`)
      
    }
    catch(error){
      console.log(error);
      
    }
  }

  useEffect(() => {
    getTodo();
  }, []);


  if (!todo) {
    return <h1>Loading...</h1>;
  }


  const updateCheck = async (id, completed) => {
    try {
      await api.put(`/task/mark/${id}`, {
        completed: completed
      });

      getTodo();

    } catch (error) {
      console.log(error);
    }
  };


  return (
    <div className="border p-3 m-3 rounded">

      <h1 className="text-2xl font-bold">
        {todo.title}
      </h1>


      <form 
        className="flex gap mt-3" 
        onSubmit={createTaskTitle}
      >

        <input
          value={taskTitle}
          onChange={(e)=>setTaskTitle(e.target.value)}
          className="border w-80 p-2 rounded"
          placeholder="Read Book"
          type="text"
        />

        <button
          type="submit"
          className="w-25 bg-yellow-800 hover:bg-yellow-900 cursor-pointer mx-2 text-white p-2 rounded"
        >
          Add Task
        </button>

      </form>


      {todo.tasks.map((task)=>(
        <div 
          className="flex items-center gap-3 border p-3 mt-2 rounded"
          key={task.id}
        >

          <input
            className="w-4 h-4 mt-0.5"
            type="checkbox"
            checked={task.completed}
            onChange={()=>{
              // updateCheck(task.id, !task.completed);
              deleteTask(task.id)
            }}
          />

          <span className="text-lg font-normal">
            {task.title}
          </span>

        </div>
      ))}

    </div>
  );
}

export default TodoDetails;