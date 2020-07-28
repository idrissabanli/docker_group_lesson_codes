import React from 'react'
import PropTypes from 'prop-types';


function Button(props) {
    const buttonText = props.buttonText;
    return (
        <button className="btn btn-primary">{buttonText}</button>
    )
}

Button.propTypes = {
    buttonText: PropTypes.string.isRequired,
}

Button.defaultProps = {
    buttonText: 'Undefined'
};

export default Button;
