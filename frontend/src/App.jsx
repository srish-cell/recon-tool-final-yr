import React from 'react'
import Navbar from './Components/Navbar/Navbar'
import Main from './Components/Navbar/Main/Main'
import Programs from './Components/Navbar/Programs/Program'
import Title from './Components/Navbar/Title/Title'
import About from './Components/Navbar/About/About'
import Test from './Components/Navbar/Test/Test'
import Footer from './Components/Footer/Footer'

const App = () => {
  return (
    <div>
      <Navbar/>
      <Main/>
      <div className="container">
          <Title subTitle='' title=''/>
      <Programs/>
      <About/>
      <Title subTitle='' title='Team Members'/>   
      <Test/>
      <Footer/>
      </div>
      
    </div>
  )
}

export default App
