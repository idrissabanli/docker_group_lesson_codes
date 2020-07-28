import React, { Component } from 'react'
import PropTypes from 'prop-types';
import Product from './Product';


class Products extends Component {
    
    
    render() {
        return (
            <div className="row">
                { this.props.products.map(product => {
                    return (
                        <Product key={product.id} id={product.id} deleteProduct={this.props.deleteProduct}  title={product.title} src={product.src} description={product.description} />
                    )
                })
                }
            </div>
           
        )
    }
}

Products.propTypes = {
    products: PropTypes.array.isRequired,
    deleteProduct: PropTypes.func.isRequired,
}


export default Products;