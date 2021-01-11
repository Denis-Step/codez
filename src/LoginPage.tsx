import React, {useState} from "react";
import {register} from "./apicalls";
import ReactDOM from "react-dom";


interface LoginPageProps {}

const LoginPage : React.FC<LoginPageProps> = (props: LoginPageProps) => {
    const [name, setName] = useState("")
    const [password, setPassword] = useState("")
    
    return <div>
        <form id="user-registration">
            <input type="text" onChange = {(e) => setName(e.target.value)} />
            <input type="password" onChange = {(e) => setPassword(e.target.value)} />
            <button onClick = {(e) => {e.preventDefault();
                                         login(name, password)}
             } />
        </form>
    </div>
    
}
ReactDOM.render(
        <LoginPage />,
    document.getElementById("root")
  );
  