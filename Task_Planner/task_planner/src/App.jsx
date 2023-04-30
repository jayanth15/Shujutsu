import './App.css'
import Main from './componenets/Main/Main';
import {
  Routes,
  Route,
  Link,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
  Outlet
} from 'react-router-dom';
import Register from './componenets/Users/Register';

function App() {
  const val = "What is Lorem Ipsum?  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
  const router = createBrowserRouter(
    createRoutesFromElements(
    <Route path="/" element={<Root />} >
    <Route index element={<Main />}/>
    <Route path="/register" element={<Register />}/>
    </Route>
    )
  )
  return (
    <div className='App'>
      <RouterProvider router={router}/>
    </div>
  );
}
const Root = () => {
  return (
    <>
    <div>
      <Outlet></Outlet>
    </div>
    </>
  )
}

export default App
