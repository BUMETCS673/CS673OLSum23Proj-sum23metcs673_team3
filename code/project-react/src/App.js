import logo from './logo.svg';
import './App.css';
import Card from "./components/Card";
// import {createBrowserRouter,RouterProvider} from "react-router-dom";
//
// const router = createBrowserRouter([
//         {
//             path: "/",
//             element: <Card />,
//             children: [
//                 {children: [
//                         { index: true, element: <Catalog/> },
//                         {
//                             path: "/catalog",
//                             element: <Catalog />,
//
//                         },
//                     ],
//                 },
//
//             ],
//         },
// ])

function App() {
  return (
    <div className="App">
      <Card/>
    </div>
  );
}

export default App;
