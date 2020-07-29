import React, { Component } from 'react';
import {ProductConsumer} from '../context';


var uniqid = require('uniqid');

class AddProduct extends Component {
    state = {
        title: "",
        src: "",
        description: ""
    }
    onChangeInput = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    createProduct = (dispatch, e) =>{
        e.preventDefault();
        const { title, src, description } = this.state;
        const newProduct = {
            id: uniqid(),
            title,
            src, 
            description
        }

        dispatch({type:"ADD_PRODUCT", payload: newProduct});
        this.setState({
            title: "",
            src: "",
            description: ""
        })
    }

    render() {
        const {title, src, description} = this.state;
        return (
            <ProductConsumer>
                {
                    value =>{
                        const {dispatch} = value;
                        return (
                            <form onSubmit={this.createProduct.bind(this, dispatch)}  className="m-auto">
                                <h1 className="text-center" >Add product</h1>
                                <div className="form-group">
                                    <label>Title</label>
                                    <input type="text" name="title" onChange={this.onChangeInput}  value={title} className="form-control"/>
                                </div>
                                <div className="form-group">
                                    <label>Image</label>
                                    <input type="text" name="src" value={src}  onChange={this.onChangeInput}  className="form-control"/>
                                </div>
                                <div className="form-group">
                                    <label>Description</label>
                                    <textarea className="form-control" value={description} onChange={this.onChangeInput}   name="description"/>
                                </div>
                                <button type="submit" className="btn btn-primary">Yarat</button>
                        </form>
                        )
                    }
                }
            </ProductConsumer>
        )
        
    }
}

export default AddProduct;
