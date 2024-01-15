import React, { useState } from 'react';
import axios from 'axios';
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL
console.log(4, BACKEND_URL)
function LoginComponent() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const backendURL = `${process.env.REACT_APP_BACKEND_URL}/login`;
        const data = new URLSearchParams();
        data.append('grant_type', '');
        data.append('username', 'chgiahuy@gmail.com');
        data.append('password', 'string');
        data.append('scope', '');
        data.append('client_id', '');
        data.append('client_secret', '');
        const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        };
        try {
            const response = await axios.post(backendURL, data, config  );
            console.log(response.data);
            localStorage.setItem('accessToken', response.data.access_token);
  
        } catch (error) {
            console.error('Login failed:', error);
             
        }
    };

    return (
        <div className="container mt-3">
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                <label htmlFor="customerCategory" className="form-label">Email</label>
                    <input type="email" className="form-control" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Email" />
                </div>
                <div className="mb-3">
                <label htmlFor="customerCategory" className="form-label">Password</label>
                    <input type="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default LoginComponent;
