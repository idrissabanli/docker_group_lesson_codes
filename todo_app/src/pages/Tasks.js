import React, { Component } from 'react'
import Task from '../components/Task';
import axios from 'axios';
import {Consumer} from '../context'

export default class Tasks extends Component {

    componentWillMount = async () =>{
        const {token} = this.props.userInfo;
        console.log(token);
        const response = await axios.get('http://localhost:8000/api/v1.0/tasks',
            { 
                headers: {
                    'Authorization': `Token ${token}`,
                },
            } 
        );
        console.log(response);
        this.setState({
            ...this.state,
            owntasks: response.data,
        });
    }
    
    render() {
        return (
            <Consumer>
                {
                    value => {
                        return (
                            <div className="accordion" id="accordionExample">
                                {
                                    this.state.owntasks.map(task=>{
                                        return <Task { ...task } />
                                    })
                                }
                                
                                
                            </div>
                        )
                    }
                }
            </Consumer>
        )

        
    }
}
