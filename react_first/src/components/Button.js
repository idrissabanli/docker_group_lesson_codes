import React from 'react'

function Button(props) {
    const buttonText = props.buttonText;
    return (
        <button className="btn btn-primary">{buttonText}</button>
    )
}

export default Button;
