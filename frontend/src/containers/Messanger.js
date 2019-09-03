import React from 'react';
import {Component} from 'react';
import MessageList from '../components/MessageList';
import MessageFormSubmit from '../components/MessageFormSubmit';

class Messanger extends Component {

    render(){

        var urlParams = window.location.search; 
        urlParams = urlParams.slice(1);
        console.log(urlParams)

        return(
            <div className='Messanger'>

                <div>
                    <MessageList/>
                </div>

                <div>
                    <MessageFormSubmit/>
                </div>

            </div>
        )
    }
}


export default Messanger 