import '../../App.css'
import Sidebar from '../Sidebar/Sidebar'
import Topbar from '../Navbar/Navbar'
import Cards from '../Tasks/Cards'
import Modal from '../Tasks/Addtask'
import {Routes, Route} from "react-router-dom"

function Main() {
  const val = "What is Lorem ssum?  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  return (
    <div className="bg-[#363654] w-screen h-screen relative">
      <Sidebar />
      <Topbar />
      <Modal />
      <div className="ml-20 top-16 relative">
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 ml-6">
          <Cards text={val} />
          <Cards />
          <Cards />
          <Cards />
        </div>
      </div>
    </div>
  );
}

export default Main
