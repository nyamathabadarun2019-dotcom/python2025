import React from "react"

export default function TaskItem(props) {
  return (
  <>
    <div className="card mb-2 p-3 d-flex flex-row flex-row justify-content-between">
        <span>Task: {props.title}</span>
        <div>
            <button className="btn btn-success btn-sm me-2">
                Done
            </button>
            <button className="btn btn-danger btn-sm">
                Delete
            </button>
        </div>
    </div>
  </>
  )
  
}