import { useState } from 'react'
import "../../App.css"
import SidebarIcon from './SidebarIcon'
function Sidebar() {
    return (
      <div>
      <div className="fixed top-0
      left-0 h-screen w-22 m-0 flex flex-col bg-[#202028] text-white shadow-lg
      content-center p-1 overflow-y-auto no-scrollbar">
        <SidebarIcon icon="T"/>
        <SidebarIcon icon="T"/>
        <SidebarIcon icon="T"/>
        <SidebarIcon icon="T"/>
        <SidebarIcon icon="T"/>
        <SidebarIcon icon="+"/>
      </div>
      </div>
    )
  }

  export default Sidebar