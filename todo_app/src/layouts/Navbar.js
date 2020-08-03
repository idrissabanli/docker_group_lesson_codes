import React from 'react';
import {Link} from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <Link to='/' className="navbar-brand">Todo Project </Link>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div className="navbar-nav">
                    <Link to='/' className="nav-item nav-link">Home </Link>
                    <Link to='/add' className="nav-item nav-link">Add Task </Link>
                    <Link to='/login' className="nav-item nav-link">Sign In </Link>
                </div>
            </div>
        </nav>
    )
}
export default Navbar;
