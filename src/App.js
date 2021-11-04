import React, { Component } from 'react';
import { Exchanges } from "./components/Exchanges";
import { Container } from 'reactstrap'
import './App.css'

class App extends Component {
  state = {
    exchanges: [],
    recommendations: {}
  }

  async componentDidMount() {
    try {
      setInterval(async () => {
        const response = await fetch('/prices');
        const res_json = await response.json();

        this.setState({ 
          exchanges: res_json.exchanges,
          recommendations: res_json.recommendations,
         });
      }, 1000);
    } catch(e) {
      console.log(e);
    }
  }
  render () {
    return (
      <Container>
        <div className="App d-flex flex-column min-vh-100 justify-content-center align-items-center">
          <Exchanges exchanges= {this.state.exchanges} recs = {this.state.recommendations} />
        </div>
      </Container>
    );
  }
}
export default App;
