import React, { useEffect, useState } from 'react'
import '../App.css'
import send from '../images/send.png'
import axios from 'axios'
import bot from '../images/bot.png'
import user from '../images/user.png'



const Chatbot = () => {
  // state to manage messages written in input
  const [message,setMessage]=useState('');
  // state to manage questions to be sent to backend
  const [question,setQuestion]=useState('');
  // state to mangage responses from backend
  const [response,setResponse]=useState('');

    // useEffect to run everytime question state is updated
    useEffect(()=>{
      const handleInput= async(e)=>{
        // code inside will only work if question state isn't null
        if(question){
          console.log(question)
          try{
            // post request is made to /messages route with the question params using axios and wait for res from backend
            const res = await axios.post('http://127.0.0.1:8000/messages',{text:question})
            setResponse(res.data.response.response)
            console.log(res)
          }
          catch(err){
            // handling error
            console.error("There was an error",err);
          }
        }
      }
      handleInput();
    },[question])
    
    
  const handleKey=(e)=>{
    //  changing question state when enter is pressed on input
    if(e.key=='Enter'){
      setQuestion(message);
    }
  }
  
  return (
    <div className='chatbot'>
      {/* question answer area */}
      <div className='main-box'>
      {question && <div className='message-box'>
        <img className='avatar' src={user} alt="" />
        <span className='message'>{question}</span>
        </div>}
      {response && <div className='message-box'>
        <img className='avatar' src={bot} alt="" />
        <span className='message'>{response}</span>
        </div>}
      </div>
      {/* input  */}
      <div>
        
        <img className='send' src={send} alt="" />
        <input value={message} onKeyDown={handleKey} onChange={e=>setMessage(e.target.value)} className='input' placeholder='Send a message' type="text" />
      </div>
    </div>
  )
}

export default Chatbot
