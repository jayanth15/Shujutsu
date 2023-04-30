import { useState } from 'react'
import randomColor from 'randomcolor'
import "../../App.css"
function SidebarIcon(props) {
    return (
      <div className={`rounded-full btn btn-circle bg-[#6D5DD3]
          flex items-center justify-center hover:rounded-lg hover:bg-[#d3ccff]
          text-white text-2xl m-2`}>
        {props.icon}
      </div>
    )
  }

  export default SidebarIcon