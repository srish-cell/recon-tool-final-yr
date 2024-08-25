import React,{useState} from 'react'
import axios from 'axios'

import './Program.css'





const Programs = () => {
  const [target, setTarget] = useState("");
  const [result, setResult] = useState("");
  const runScan = async () => {
    try {
      console.log(target);
      const response = await axios.post("http://localhost:5000/scan", {
        target
      });
      console.log(response);
      setResult(response.data.output);
    } catch (error) {
      setResult(error.response ? error.response.data.error : "An error occurred");
    }
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    runScan();
  };
  return (
    
  


    <div className='Programs'>
        
      <div className="TestSection">
        
        <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="protocol">Target</label>
          
          <input
            type="text"
            value={target}
            onChange={(e) => setTarget(e.target.value)}
            placeholder="Enter target IP or hostname"
          />
        </div>
        <button className="submit-btn">Start scan</button>
      </form>
      <pre>{result}</pre>
      </div>
    </div>
  )
}

export default Programs
