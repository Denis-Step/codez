import React from "react";
import {Route, Switch} from "react-router";
import Game from "./Game";
import SignupPage from "./Login/SignupPage";

const Routes = (): JSX.Element => {
    
    return (
        <Switch>
            <Route path = "/:id" component={Game} />
            <Route path = "/" component={SignupPage} />
        </Switch>
    )
}

export default Routes;