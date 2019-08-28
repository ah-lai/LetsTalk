import React from 'react'
import MessageList from '../components/MessageList'

class Messanger extends React.Component{

    render () {
        return (
         
            <div>
                <MessageList ref='MessageList'/>
            </div> 
        );
    }
}

export default Messanger 