import React from "react";
import axios from 'axios';

const Context = React.createContext();

const reducer = (state, action) => {
    if (action.type === "CHANGE_USERINFO") {
      return { ...state, isAuthenticated:true, userInfo: action.payload, };
    }
    if (action.type === "SET_OWNTASKS") {
        return { ...state, owntasks: action.payload, };
      }
  };

export class Provider extends React.Component {
    state = { 
      isAuthenticated: false,
      userInfo: null,
      owntasks: [],
      dispatch: action => {
        this.setState(state => reducer(state, action));
      }
    };

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