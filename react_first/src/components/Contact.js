import React, { Component } from 'react'
import Button from './Button'

class Contact extends Component {
    render() {
        return (
            <form className="m-auto">
                <div className="form-group">
                    <label>Full name</label>
                    <input type="text" name="full_name" className="form-control"/>
                </div>
                <div className="form-group">
                    <label>Email</label>
                    <input type="text" name="email" className="form-control"/>
                </div>
                <div className="form-group">
                    <label>Subject</label>
                    <input type="text" name="subject" className="form-control"/>
                </div>
                <div className="form-group">
                    <label>Message</label>
                    <input type="text" name="message" className="form-control"/>
                </div>
                <Button buttonText="Gonder"/>
            </form>
        )
    }
}
export default Contact;
