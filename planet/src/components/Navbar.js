import React, { useEffect, useState } from 'react'
import Group from '../images/Group.png'
import logo from '../images/logo.png'
import '../App.css'
import { useRef } from 'react'
import file_icon from '../images/file.png'
import axios from 'axios'

const Navbar = () => {
  // for storing fle state ... initailay set to null
  const [file,setFile]=useState(null);
  
  // ref to input field for taking input of file
  const fileInputRef = useRef(null);

  // handling button click on upload pdf button
  const hanldeButton=()=>{
    // when clicked it ref to the input field and click it
    fileInputRef.current.click();
  }

  // useEffect for calling function everytime when file state is changed
  useEffect(()=>{
    // function to handle file upload
    const handleUpload = async(e)=>{
      // function will make changes only when file state isn't null i.e. file contains some file
      if(file){
      const formData = new FormData();
      formData.append('file',file)

      console.log(file);

      try{
        // making a post request at our required route using axios and waiting for response from fastapi backend
        const headers = {'Content-Type':file.type}
        const response = await axios.post('http://127.0.0.1:8000/upload',formData,headers);
        console.log('file uploaded:',response.data);
      }
      catch(err){
        // hanlding errors in post request
        console.error('error uploading',err);
      }
      }
    }
    // calling the function
    handleUpload();
  },[file])

  const handleFileUpload=async(e)=>{
    // changing file state
    setFile(e.target.files[0]);
  }

  

  return (
    // navbar
    <div className='nav'>
      {/* ai planet logo  */}
        <div className='logo'>
            <img src={logo} alt="" />
        </div>
        
        {/* upload button and uploaded file name area */}
        <div className='ubox'>
        {file && <span className='show'>
          <img src={file_icon} alt="" />
          <p>{file.name}</p>
          </span>}
        <button onClick={hanldeButton} className='btn'> 
          <input ref={fileInputRef} onChange={handleFileUpload} className='file-input' type="file" />
          <img src={Group} alt="" />
            <span>Upload PDF</span>
        </button>
        </div>

    </div>
  )
}

export default Navbar
