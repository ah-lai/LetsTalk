import React from 'react';
import {Route} from 'react-router-dom';

import Login from './containers/Login';
import Signup from './containers/Signup';
import Messanger from './containers/Messanger';

const BaseRouter = () => (
    <div>
        <Route exact path="/" component={Login} />{" "}
        <Route exact path="/login/" component={Login} />{" "}
        <Route exact path="/signup/" component={Signup} />{" "}
        <Route exact path="/messanger/" component={Messanger} />{" "}
    </div>
);

export default BaseRouter;