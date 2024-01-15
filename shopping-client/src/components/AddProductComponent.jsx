import React, { useState } from 'react';
import axios from 'axios';

function AddProductComponent() {
    const [productName, setProductName] = useState('');
    const [productPrice, setProductPrice] = useState('');
    const [productDescription, setProductDescription] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();

        const productData = {
            name: productName,
            price: productPrice,
            description: productDescription
        };

        try {
           
            const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/products/add`, productData);
            console.log(response.data);
            // Handle success - clear form or show success message
        } catch (error) {
            console.error('Error adding product:', error);
            // Handle error - show error message
        }
    };

    return (
        <div className="container mt-3">
            <h2>Add Product</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="productName" className="form-label">Product Name</label>
                    <input
                        type="text"
                        className="form-control"
                        id="productName"
                        value={productName}
                        onChange={(e) => setProductName(e.target.value)}
                        required
                    />
                </div>
                 <div className="mb-3">
                    <label htmlFor="productPrice" className="form-label">Product Price</label>
                    <input
                        type="number"
                        className="form-control"
                        id="productPrice"
                        value={productPrice}
                        onChange={(e) => setProductPrice(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="productDescription" className="form-label">Product Description</label>
                    <textarea className="form-control"
                        id="productDescription"
                        value={productDescription}
                        onChange={(e) => setProductDescription(e.target.value)}
                    ></textarea>
                </div>
                <button type="submit" className="btn btn-primary">Add Product</button>
            </form>
        </div>
            );
    }

export default AddProductComponent;
