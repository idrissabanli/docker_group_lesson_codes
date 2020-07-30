import React from 'react';
import './App.css';
import SingIn from './pages/SingIn';
import Navbar from './layouts/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import PrivateRoute from './utils/PrivateRoute';
import AuthRoute from './utils/AuthRoute';

import Tasks from './pages/Tasks';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import NotFound from './pages/NotFound';
import {Consumer} from './context'


function App() {

  return (
    <Consumer>

      {
        value =>{
          const {isAuthenticated, userInfo} = value;
          return (
            <div className="App">
              <Router>
                <Navbar/>
              <Switch>
                  <AuthRoute exact authed={isAuthenticated}  path="/login" component={SingIn}/>
                  <PrivateRoute exact authed={isAuthenticated} path='/' >
                      <Tasks userInfo={userInfo}/>
                  </PrivateRoute>
                  <Route component={NotFound}/>
                </Switch>
              </Router>
            </div>
          );
        }
      }
    </Consumer>
  )
  
}

export default App;
