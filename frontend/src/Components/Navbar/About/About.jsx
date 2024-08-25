import React from 'react'
import './About.css'
import about_img from '../../../assets/main1.jpg'

const About = () => {
  return (
    <div className='about'>
      <div className="about-left">
        <img src={about_img} alt="About this Project" className='about-img'/>
        
    </div>
     <div className="about-right">
          <h3> Reconnaissance Tool</h3>
         <h2>  </h2>
         <p> This project aims to develop an advanced digital reconnaissance tool to enhance cybersecurity efforts
         by automating the identification of security flaws within an organization's online infrastructure. 
         By integrating web scraping, port scanning, and subdomain discovery, the tool provides a comprehensive view 
         of the digital footprint, uncovering vulnerabilities such as open network ports and hidden subdomains. 
         It also facilitates thorough risk and impact analysis, enabling cybersecurity professionals to prioritize
          mitigation efforts and strengthen security posture, thereby addressing common issues like inadequate security controls, 
          exploited vulnerabilities, and configuration errors.</p>
          </div>
    </div>
  )
}

export default About
