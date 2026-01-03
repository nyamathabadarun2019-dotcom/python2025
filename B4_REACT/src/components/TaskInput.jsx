import React  from "react";
import {useState} from "react"

export default function TaskInput(){
    
return (

<>
<div className="input-group mb-4">
    <input
    className="from-control"
    placeholder="Enter a new task..."
    onChange={(e)=> setTask(e.target.value)}
    />
    <button className="btn btn-primary">
        Add Task
        </button>
        <p>{taskText}</p>

</div>

</>

)

}