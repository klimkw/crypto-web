import React, { useEffect, useState } from 'react';
import { Exchanges } from "./components/Exchanges";
import { Container } from 'reactstrap'
import './App.css'

function App() {
  const [exchanges, setExchanges] = useState([]);
  const [recs, setRecs] = useState({});
  useEffect(() => {
    fetch("/prices").then(response =>
      response.json().then(data => {
        setExchanges(data.exchanges);
        setRecs(data.recommendations)
      })
  );
}, []);
  return (
    <Container>
      <div className="App d-flex flex-column min-vh-100 justify-content-center align-items-center">
        <Exchanges exchanges= {exchanges} recs = {recs} />
      </div>
    </Container>
  );
}
export default App;
