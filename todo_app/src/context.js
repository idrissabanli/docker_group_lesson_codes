import React from "react";
import axios from 'axios';

const Context = React.createContext();

const reducer = (state, action) => {
    if (action.type === "CHANGE_USERINFO") {
      return { ...state, isAuthenticated:true, userInfo: action.payload, setState: true };
    }
    if (action.type === "SET_OWNTASKS") {
        return { ...state, owntasks: action.payload, setState: true};
      }
    if (action.type === "ADD_OWN_TASKS") {
        return { ...state, owntasks: action.payload, setState: true };
      }
    if (action.type === "ADD_TASK") {
        console.log(action.payload)
        return  {
                    ...state,
                    owntasks: [...state.owntasks, action.payload],
                    setState: true
                }
    }
  };

export class Provider extends React.Component {
    state = { 
        isAuthenticated: localStorage.getItem('userInfo') ? true: false,
        userInfo: this.isAuthenticated ? JSON.parse(localStorage.getItem('userInfo')): [],
        owntasks: [],
        setState: true,
        dispatch: action => {
            this.setState(state => reducer(state, action) );
            this.forceUpdate();
        }
    };

    shouldComponentUpdate(nextProps) {
        console.log('here setState: '+ this.state.setState);
        return this.state.setState;
    }
    componentDidMount = () =>{
        this.setState({...this.state})
    }

    componentDidUpdate = async (prevProps, prevState, snapshot) =>{
        if (this.state.isAuthenticated){
            const {token} = JSON.parse(localStorage.getItem('userInfo'))
            console.log(token);
            const response = await axios.get('http://localhost:8000/api/v1.0/tasks',
                { 
                    headers: {
                        'Authorization': `Token ${token}`,
                    },
                } 
            );
            this.setState({
                ...this.state,
                owntasks: response.data,
                setState:false,
            });
        }
    }

    render() {
        const { children } = this.props;
        return ( 
        <Context.Provider value={this.state}>
            {children}
        </Context.Provider>
        );
    }
}

export const Consumer = Context.Consumer;