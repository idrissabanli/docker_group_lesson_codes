import React, {Component} from 'react';
import './App.css';
import Navbar from './components/Navbar'
import Contact from './components/Contact';
import Products from './components/Products';
import AddProduct from './components/AddProduct';

class App extends Component {

  // deleteProduct = (id)  => {
  //     this.setState({ 'products': this.state.products.filter(product => product.id !== id )
  //   });
  // }

  // addProduct = (newProduct) => {
  //   this.setState({
  //     products: [...this.state.products, newProduct]
  //   });
  // }

  render(){
    return (
      <div className="App">
        <Navbar isAuthenticated={false}/>
        <div className="container">
          <h1 className="text-center">Hello World</h1>
          <p className="center" style={{ color: '#FF0000' }}>Salam Dunya</p>
          <Contact/>
          
          <Products/>
          <hr/>
          <AddProduct addProduct={this.addProduct}/>
        </div>
      </div>
    );
  }
}

export default App;
