import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navigation from "./components/Nav";
import Container from "react-bootstrap/esm/Container"
import Home from "./views/Home"
import { useState } from "react";
import ListView from "./views/ListView";

export default function App() {
  

  return ( 
    <BrowserRouter>
      <Container data-bs-theme='dark'>
        <Navigation />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/list' element={<ListView />}/>
        </Routes>
      </Container>
    </BrowserRouter>
  )
}
