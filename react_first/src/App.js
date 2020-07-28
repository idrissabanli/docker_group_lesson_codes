import React, {Component} from 'react';
import './App.css';
import Navbar from './components/Navbar'
import Contact from './components/Contact';
import Products from './components/Products';


class App extends Component {

   state =  {
     'products' : [
                  {
                    id: 1,
                    title: 'Iphone 7',
                    src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                    description: 'Good product',
                  },
                  {
                    id: 2,
                    title: 'Iphone 8',
                    src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                    description: 'Good product',
                  },
                  {
                    id: 3,
                    title: 'Iphone 9',
                    src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                    description: 'Good product',
                  },
                  {
                    id: 4,
                    title: 'Iphone 10',
                    src: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-11-pro-select-2019-family?wid=882&amp;hei=1058&amp;fmt=jpeg&amp;qlt=80&amp;op_usm=0.5,0.5&amp;.v=1586586488946',
                    description: 'Good product',
                  },
          ],
  }

  deleteProduct = (id)  => {
      this.setState({ 'products': this.state.products.filter(product => product.id !== id )
    });
  }

  render(){
    return (
      <div className="App">
        <Navbar isAuthenticated={false}/>
        <div className="container">
          <h1 className="text-center">Hello World</h1>
          <p className="center" style={{ color: '#FF0000' }}>Salam Dunya</p>
          <Contact/>
          
          <Products deleteProduct={this.deleteProduct} products={this.state.products}/>
        
        </div>
      </div>
    );
  }
}

export default App;
