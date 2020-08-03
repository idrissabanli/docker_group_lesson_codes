import React, { Component } from 'react'

class Task extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-header" id="headingOne">
                <h2 className="mb-0">
                    <button className="btn btn-link" type="button" data-toggle="collapse" data-target={"#collapse" + this.props.id}  aria-expanded="true" aria-controls={"collapse" + this.props.id} >
                    {this.props.title}
                    </button>
                </h2>
                </div>
                <div id={"collapse" + this.props.id}  className="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                <div className="card-body">
                    {this.props.description}
                </div>
                </div>
          </div>
        )
    }
}

export default Task;
