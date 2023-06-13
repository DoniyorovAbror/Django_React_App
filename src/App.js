import * as React from "react";
import "./index.css"
import { Route, Routes } from "react-router-dom";
import { Header } from "./components/Header/Header.js";
import { Category } from "./components/Category/Category.js";
import { Foods } from "./components/Foods/Foods.js";
import { FoodDetail } from "./components/FoodDetail/FoodDetail";
import { Footer } from "./components/Footer/Footer.js"

function App() {
  return (
    <div className='App'>
      <Header />
        <Routes>
          <Route path='/' element={<Category />} />
          <Route path='/:receipt_id' element={<Foods />} />
          <Route path='/:receipt_id/:id' element={<FoodDetail />} />
        </Routes>
      <Footer />
    </div>
  );
}

export default App;
