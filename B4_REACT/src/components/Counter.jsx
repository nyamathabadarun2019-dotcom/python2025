import { useState} from "react"



export default function Counter(){
    const [count ,setCounter] = useState(1)
    

    return(
        <>
           <div style={{textAlign: "center"}}>
            <h2>Counter {count} </h2>
            <button onClick={()=> setCounter(count+1)}>Increment</button>
            <button onClick={()=>setCounter(count-1)}>Decrement</button>
            <button onClick={()=> setCounter(0)}>Reset</button>

           </div>
        
        </>
    )

}