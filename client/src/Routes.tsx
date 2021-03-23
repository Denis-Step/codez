import React from "react";
import {Route, Switch} from "react-router";
import Game from "./Game";
import HomePage from "./HomePage";
import SigninPage from "./SigninPage";

const Routes = (): JSX.Element => {
    
    return (
        <Switch>
            <Route path="/logz" component={SigninPage} />
            <Route path = "/play/:id" component={Game} />
            <Route path = "/" component={HomePage} />
        </Switch>
    )
}

export default Routes;