import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { connect } from 'react-redux';
import BaseRouter from './routes';
import 'antd/dist/antd.css';
import * as actions from './store/actions/auth';

import CustomLayout from './containers/Layout';

class App extends Component{
  componentDidMount() {
    this.props.onTryAutoSignup();
  }

  render(){
  return (
    <div>
      <Router>
        <CustomLayout {...this.props}>
          <BaseRouter/>
        </CustomLayout>
      </Router>
    </div>
  );
  }
}

// Connect Apps and States, Convert state to props 
// Layout has props

const mapStateToProps = state => {
  return {
    isAuthenticated: state.token != null
  }
}

// Automatic Authentication check 
const mapDispatchToProps = dispatch => {
  return {
    onTryAutoSignup: () => dispatch(actions.authCheckState)
  }
}


export default connect(mapStateToProps,mapDispatchToProps)(App);
