import React, { Component } from 'react';
import {Consumer} from '../context';
import axios from 'axios'
import {Redirect} from 'react-router-dom';

class SingIn extends Component {

    constructor(props){
        super()
        if(localStorage.getItem('userInfo')){
            props.history.push('/');
        }
    }

    state = {
        redirectToReferrer: false,
        username: '',
        password: ''
    }

    signIn = async (dispatch, e) =>{
        e.preventDefault();
        const {username, password} = this.state;
        const userData = {
            username,
            password
        }
        const response = await axios.post('http://localhost:8000/api/v1.0/auth/login/', userData);
        console.log(response);
        if (response.status === 200){
            localStorage.setItem('userInfo', JSON.stringify(response.data)); 
            dispatch({type:"CHANGE_USERINFO", payload:response.data});
            this.setState({
                redirectToReferrer: true
            });
        }
            
    }

    changeInput = (e) =>{
        this.setState({
            [e.target.name]: e.target.value,
        });
    }

    render() {
        if (this.state.redirectToReferrer)
            return <Redirect to="/" />

        return (
            <Consumer>
                {
                    value => {
                        const {dispatch} = value;
                        return (
                            <div className="m-auto sign-in d-flex align-items-center">
                                <form onSubmit={this.signIn.bind(this, dispatch)} method="POST">
                                    <div className="form-group">
                                        <input type="text" id="username" name="username" onChange={this.changeInput} value={this.state.username} className="form-control" placeholder="Enter username" required="" autoFocus=""/>
                                    </div>
                                    <div className="form-group">
                                        <input type="password" id="password" name="password" onChange={this.changeInput} value={this.state.password} className="form-control" placeholder=" Enter password" required=""/>
                                    </div>
                                    <button className="btn btn-lg btn-primary btn-block" type="submit">Sign In</button>
                                </form>
                            </div>
                        )
                    }
                }
            </Consumer>
        )

        
    }
}
export default SingIn;
