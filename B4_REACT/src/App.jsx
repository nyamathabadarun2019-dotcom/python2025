import { useState } from 'react'

import './App.css'

import Header from '../src/components/Header.jsx'
import TaskInput  from './components/TaskInput.jsx'
import TaskList from './components/TaskList.jsx'


function App() {
  const [taskText,setTask] = useState('')
  return (
    <>
      <Header/>
      <TaskInput/>
      <TaskList/>
       
    </>
  )
}

export default App
