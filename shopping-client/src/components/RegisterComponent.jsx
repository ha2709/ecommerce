import React, { useState } from 'react';
import axios from 'axios';

function RegisterComponent() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [userType, setUserType] = useState(''); // internal or external
    const [departmentId, setDepartmentId] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(' BACKEND_URL/register', { email,
                password, userType, departmentId });
                console.log(response.data);
                 
        } catch (error) {
            console.error('Registration failed:', error);
         
        }
        };
    return (
        <div className="container mt-5">
            <form onSubmit={handleSubmit} className="w-100">
                <div className="mb-3">
                    <input type="email" value={email} className="form-control" onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
                    </div>
                <div className="mb-3">
                    <input type="password" value={password} className="form-control" onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
                </div>
                <div className="mb-3">
                    <select className="form-control" value={userType} onChange={(e) => setUserType(e.target.value)}>
                        <option value="internal">Internal Staff</option>
                        <option value="external">External Customer</option>
                    </select>
                </div>
                <div className="mb-3">
                    <input type="text" value={departmentId} className="form-control" onChange={(e) => setDepartmentId(e.target.value)} placeholder="Department ID" />
                </div>
                <button className="form-control" type="submit">Register</button>
                
            </form>
        </div>
    );
}
export default RegisterComponent;                