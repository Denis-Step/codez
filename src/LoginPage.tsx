import React, {useState} from "react";
import {login} from "./apicalls"

interface LoginPageProps {}

const LoginPage : React.FC<LoginPageProps> = (props: LoginPageProps) => {
    const [name, setName] = useState("")
    
    return <div>
        <form>
            <input type="text" onChange = {(e) => setName(e.target.value)} />
            <button onClick = {(e) => {e.preventDefault();
                                         login(name)}
             } />
        </form>
    </div>
    
}

export default LoginPage