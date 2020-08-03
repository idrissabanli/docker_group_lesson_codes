import React, { Component } from 'react';
import axios from  'axios';
import {Consumer} from '../context';

class AddTask extends Component {
    state = { 
        title: "",
        description: "",
        assigned_to: null,
        deadline: "",
        users: [],
    }

    componentDidMount = async () => {
        console.log('here');
       
        // const {token} = JSON.parse(localStorage.getItem('userInfo'))
        // console.log(token);
        const response = await axios.get('http://localhost:8000/api/v1.0/auth/users/');
        this.setState({
            ...this.state,
            users:response.data,
        });
    
    }

    createTask = async (dispatch, e) => {
        e.preventDefault();
        const {token} = JSON.parse(localStorage.getItem('userInfo'))
        const {title, description, assigned_to, deadline} = this.state;
        console.log(assigned_to);
        // assigned_to = parseInt(assigned_to)
        const newTaskData = {
            title,
            description,
            deadline,
            'assigned_to': [parseInt(assigned_to)]
        }
        const response = await axios.post('http://localhost:8000/api/v1.0/tasks/',  newTaskData, 
        { 
            headers: {
                'Authorization': `Token ${token}`,
            },
        } );
        if (response.status === 201){
            dispatch({type:'ADD_TASK', payload:response.data});
            this.props.history.push('/');
        }
        console.log(response);
    }

    inputChange = (e) =>{
        this.setState({
            [e.target.name]: e.target.value,
        })
    }

    render() {
        return (
        <Consumer >
            
            {
                value => {
                    const {dispatch} = value;
                    const {title, description, assigned_to, users, deadline} = this.state;
                    return (
                        <div className="container">
                            <form onSubmit={this.createTask.bind(this, dispatch)} method="post">
                                <div className="form-group">
                                    <label>Title</label>
                                    <input type="text" className="form-control" onChange={this.inputChange} name="title" required value={title}/>
                                </div>
                                <div className="form-group">
                                    <label>Desctiption</label>
                                    <textarea name="description" className="form-control"  onChange={this.inputChange}  value={description} cols="30" rows="10"></textarea>
                                </div>
                                <div className="form-group">
                                    <label>Assigned To</label>
                                    <select name="assigned_to" onChange={this.inputChange} className="form-control"  >
                                    <option>Select User</option>
                                        {
                                            users.map(user => { return assigned_to === user.id ?  
                                                (<option defaultValue key={user.id} value={user.id}>{user.username}</option>) : 
                                                (<option key={user.id} value={user.id}>{user.username}</option>) } )
                                        }
                                    </select>
                                </div>
                                <div className="form-group">
                                    <label>Deadline</label>
                                    <input type="datetime" className="form-control" onChange={this.inputChange} name="deadline" required value={deadline}/>
                                </div>

                                <button type="submit" className="btn btn-primary">Yarat</button>


                            </form>

                        </div>
                    )
                }
            }


        </Consumer>
        )

        
    }
}

export default AddTask;
