import React, {useEffect} from "react";
import {Route, Switch} from "react-router";
import Game from "./Game";
import SignupPage from "./SignupPage";

const Routes = () => {
    
    return (
        <Switch>
            <Route path = "/" component={SignupPage} />
            <Route path = "/games/:id" component={Game} />
        </Switch>
    )
}

export default Routes;