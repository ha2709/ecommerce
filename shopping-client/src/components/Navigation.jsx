import React from 'react';
// import { Routes, Route } from 'react-router-dom';

import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import LoginComponent from './LoginComponent';
import RegisterComponent from './RegisterComponent';
import VerifyEmailComponent from './VerifyEmailComponent';
import DiscountConfigComponent from './DiscountConfigComponent';
import AddProductComponent from './AddProductComponent';

function Navigation() {
    return (
        <Router>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">MyApp</Link>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                        <li className="nav-item">
                            <Link className="nav-link" to="/login">Login</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/register">Register</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/verify/:token">Verify Email</Link>
                        </li>                       
                        <li className="nav-item">
                            <Link className="nav-link" to="/add-product">Add Product</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/config-discount">Configure Discounts</Link>
                        </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div className="container mt-4">
                <Routes>
                    <Route exact path="/config-discount" element={<DiscountConfigComponent/>} />
                    <Route exact path="/login" element={<LoginComponent/>} />
                    <Route exact path="/register" element={<RegisterComponent/>} />
                    <Route path="/verify/:token" element={<VerifyEmailComponent/>} />
                    <Route exact path="/add-product" element={<AddProductComponent/>} />
                </Routes>
            </div>
         </Router>
        );
    }
        
export default Navigation;