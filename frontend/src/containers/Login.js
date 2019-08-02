import React from 'react';
import { Form, Icon, Input, Button, Spin } from 'antd';
import {connect} from 'react-redux';
//import {NavLink} from 'react-router-dom';
import * as actions from '../store/actions/auth';

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;


class NormalLoginForm extends React.Component {
  handleSubmit = e => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        this.props.onAuth(values.userName,values.password);
      }
    });
    //this.props.history.push('/'); //redirect to message
  };

  render() {

    let errorMessage = null;

    if (this.props.error) {
        errorMessage = (
            <p>{this.props.error.message}</p>
        )
    }

    const { getFieldDecorator } = this.props.form;
    return (
    <div>
        {errorMessage}
        {
            this.props.loading ? 

            <Spin indicator={antIcon}/>

            :

            <Form onSubmit={this.handleSubmit} className="login-form">
                
                <Form.Item>
                {getFieldDecorator('username', {
                    rules: [{ required: true, message: 'Please input your username!' }],
                })(
                    <Input
                    prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
                    placeholder="Username"
                    />,
                )}
                </Form.Item>

                <Form.Item>
                {getFieldDecorator('password', {
                    rules: [{ required: true, message: 'Please input your Password!' }],
                })(
                    <Input
                    prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
                    type="password"
                    placeholder="Password"
                    />,
                )}
                </Form.Item>

                <Form.Item>
                    <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                        Login
                    </Button>
                </Form.Item>
            </Form>
        }

    </div>
    );
  }
}

// need sign up link

const WrappedNormalLoginForm = Form.create({ name: 'normal_login' })(NormalLoginForm);

//State
const mapStateToProps = (state) => {
    return{
        loading: state.loading,
        error: state.error
    }
}

//Post
const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username,password) => dispatch(actions.authLogin(username,password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(WrappedNormalLoginForm);
