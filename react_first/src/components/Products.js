import React, { Component } from 'react'
import Product from './Product';
import {ProductConsumer} from '../context';


class Products extends Component {
    
    
    render() {
        return (
            <ProductConsumer>
                {
                    value => {
                        const {products} = value;
                        return (
                                 <div className="row">
                                        { products.map(product => {
                                            return (
                                                <Product key={product.id} id={product.id} deleteProduct={this.props.deleteProduct}  title={product.title} src={product.src} description={product.description} />
                                            )
                                        })
                                    }
                            </div>
                        )
                    }
                }
            </ProductConsumer>
        )

    }
}


export default Products;