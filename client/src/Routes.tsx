import React from "react";
import {Route, Switch} from "react-router";
import Game from "./Game";
import SignupPage from "./Login/SignupPage";

const Routes = (): JSX.Element => {
    
    return (
        <Switch>
            <Route path = "/" component={SignupPage} />
            <Route path = "/games/:id" component={Game} />
        </Switch>
    )
}

export default Routes;