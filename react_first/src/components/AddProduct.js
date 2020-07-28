import React, { Component } from 'react'

class AddProduct extends Component {
    state = {
        title: "",
        src: "",
        description: ""
    }
    onChangeInput = (e) => {
        let Obj = {};
        Obj[e.target.name] = e.target.value;
        this.setState({
            ...Obj
        });
    }

    createProduct = (e) =>{
        e.preventDefault();
        this.props.addProduct(this.state);
    }

    render() {
        const {title, src, description} = this.state;
        return (
            <form  className="m-auto">
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
                <button onClick={this.createProduct} className="btn btn-primary">Yarat</button>
        </form>
        )
    }
}

export default AddProduct;
