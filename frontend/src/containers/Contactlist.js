import React from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';

import { List, Avatar } from 'antd';


class contactlist extends React.Component{

    state = {
        contactdata: [],
        errors: null 
      };

    componentDidMount() {
        this.fetchdata();
    }

    fetchdata(){
        axios.get('http://127.0.0.1:8000/user/')

        .then(res => {
            console.log(res.data)
            this.setState({
                contactdata: res.data,
            });
        })
        .catch(error => this.setState({error}));
    }

    render(){
        const {contactdata} = this.state;
        return(
        <List
            itemLayout="horizontal"
            dataSource={contactdata}
            renderItem={item => (
                <List.Item>
                    <List.Item.Meta
                        avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
                        title={<Link to={`/messanger?${item.id}`}>{item.username}</Link>} //redirect to messanger and pass user id
                    />
                </List.Item>
            )}
        />
        );
    }
}



export default contactlist