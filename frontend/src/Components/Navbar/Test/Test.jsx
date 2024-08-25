import React from 'react'
import './Test.css'

import user_1 from '../../../assets/sridharan.jpg'
import user_2 from '../../../assets/srish.jpg'




const Test = () => {
 return (
    <div className='test'>
        
        <div className="slider">
        <ul>
            <li> 
                <div className="slide">
                    <div className="user-info">
                        <img src={user_1} alt=""/>
                        <div>
                            <h3> Sridharan S</h3>
                            <span>Cyber Security </span>

                        </div>
                    </div>
                    <p> In this Project</p>
                </div>
            </li>
            <li> 
                <div className="slide">
                    <div className="user-info">
                        <img src={user_2} alt=""/>
                        <div>
                            <h3> Srish N</h3>
                            <span>Cyber Security </span>

                        </div>
                    </div>
                    <p> In this Project</p>
                </div>
            </li>
            
            
        </ul>
        </div>
    </div>
  )
}

export default Test
