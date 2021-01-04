import React, {useState} from "react";
import {login} from "./apicalls"

interface LoginPageProps {}

const LoginPage : React.FC<LoginPageProps> = (props: LoginPageProps) => {
    const [name, setName] = useState("")
    const [game, setGame] = useState("")
    
    return <div>
        <form>
            <input type="text" onChange = {(e) => setName(e.target.value)} />
            <input type="text" onChange = {(e) => setGame(e.target.value)} />
            <button onClick = {(e) => {e.preventDefault();
                                         login(name,game)}
             } />
        </form>
    </div>
    
}

export default LoginPage