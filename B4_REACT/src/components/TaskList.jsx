import TaskItem from "./TaskItem.jsx";
import { useState } from "react"

export default function TaskList() {
    
    return (
        <>
      
        <TaskItem title={'pyhthon'}/>
        <TaskItem title={'Java'}/>
        <TaskItem title={'pyhthon1'}/>
        </>
    )
}


// HTML -> Components - Visual block as component
// Break the UI into pieces - Header, TaskInput, TaskList, TaskItem
// App.jsx as container where we compose our UI
// 'React is components first'


// 
