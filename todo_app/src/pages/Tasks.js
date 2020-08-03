import React, { Component } from 'react'
import Task from '../components/Task';
import {Consumer} from '../context'

class Tasks extends Component {

    constructor(props){
        super()
        console.log('constructor worked');
    }

    componentDidMount(){
        console.log('componentDidMount worked');
    }
    componentDidUpdate(){
        console.log('componentDidUpdate worked');
    }
    render() {
        console.log('render worked');
        return (
            <Consumer>
                {
                    value => {
                        const {owntasks} = value;
                        return (
                            <div className="container">
                                <h1 className="text-center">My Tasks</h1>
                            <div className="accordion" id="accordionExample">
                                {
                                    owntasks.map(task=>{
                                        return <Task key={task.id} { ...task } />
                                    })
                                }
                                
                                
                            </div>
                            </div>
                        )
                    }
                }
            </Consumer>
        )

        
    }
}

export default Tasks;