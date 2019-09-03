import React from 'react'
import axios from 'axios';

export default class MessageList extends React.Component{

    state = {
      messages: [],
      isLoading: true,
      errors: null,
      senderID: null
    };

    componentDidMount(){
 
        this.getMessage();
        this.interval = setInterval(() => {
            this.getMessage();
          }, 1000);
    }   

    getMessage() {
        const userID = localStorage.getItem('userID')

        axios.post('http://127.0.0.1:8000/getmessage/',{userID: userID})

        .then(response => {
            console.log(response.data)
            this.setState({
                messages: response.data,
                isLoading: false
            });
        })
        .catch(error => this.setState({ error, isLoading: false}));
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        const { isLoading, messages } = this.state;

        let url = window.location.href;
        var urlParams = window.location.search; 
        urlParams = urlParams.slice(1);
        console.log(urlParams)

        return (
          <React.Fragment>
            <div>
              {!isLoading ? (
                messages.map(message => {
                  const { _id, senderID, content } = message;
                  return (
                    <div key={_id}>
                      <div>{senderID}</div>
                      <div>{content}</div>
                    </div>
                  );
                })
              ) : (
                <p>Loading...</p>
              )}
            </div>
          </React.Fragment>
        );
      }
}

