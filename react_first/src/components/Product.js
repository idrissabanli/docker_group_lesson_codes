import React, { Component } from 'react'
import PropTypes from 'prop-types';


class Product extends Component {
    state = {
        backgroundColor: 'white',
        isVisable : true
    }
    deleteElement = (e) =>{
        this.props.deleteProduct(this.props.id);
    }
    change = () => {
        this.setState({
            isVisable : !this.state.isVisable
        });
    }
    changeBgColor = () => {
        this.setState({
            backgroundColor : 'orange'
        });
    }
    render() {
        return (
            <div className="col-3">
                <div className={'card ' + this.state.backgroundColor} >
                    <img className="card-img-top" src={this.props.src} alt="Card image cap"/>
                    <div className="card-body">
                        <h5 className="card-title">{this.props.title}</h5>
                        { this.state.isVisable ? <p className="card-text">{this.props.description}</p> : null }
                        
                        <div className="d-flex justify-content-between flex-wrap">

                        <a href="#" className="btn btn-primary">Go</a>
                        <button onClick={this.change}  className="btn btn-warning"> { this.state.isVisable? "Hide" : "Show" }</button>
                        <button onClick={this.deleteElement}  className="btn btn-danger">Remove</button>
                        <button onClick={this.changeBgColor}  className="btn btn-default">Change Color</button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

Product.propTypes = {
    src: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    description:  PropTypes.string.isRequired,
    deleteProduct: PropTypes.func.isRequired,
}

export default Product;
