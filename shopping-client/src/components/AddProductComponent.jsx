import React, { useState } from 'react';
import axios from 'axios';

function AddProductComponent() {
    const [productId, setProductId] = useState('');
    const [quantity, setQuantity] = useState(0);

    const handleSubmit = async (event) => {
        event.preventDefault();
 
        const backendURL = `${process.env.REACT_APP_BACKEND_URL}/cart/add_product`;
        const data = {
            product_id: productId,
            quantity: quantity
          };       // Replace with actual quantity
        const accessToken = localStorage.getItem('accessToken');
        const config = {
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json'
            }
        };
    
        try {
            const response = await axios.post(backendURL, data, config);
            console.log(response.data);
            // Handle adding product to cart success (e.g., update cart UI, confirmation message)
        } catch (error) {
            console.error('Adding product to cart failed:', error);
            // Handle adding product to cart failure (e.g., error message to user)
        }
    }
    return (
        <div className="container mt-3">
        <h2>Add Product to Cart</h2>
        <form onSubmit={handleSubmit}>
            <div className="mb-3">
                <label htmlFor="productId" className="form-label">Product ID</label>
                <input
                    type="text"
                    className="form-control"
                    id="productId"
                    value={productId}
                    onChange={(e) => setProductId(e.target.value)}
                    required
                />
            </div>
            <div className="mb-3">
                <label htmlFor="quantity" className="form-label">Quantity</label>
                <input
                    type="number"
                    className="form-control"
                    id="quantity"
                    value={quantity}
                    onChange={(e) => setQuantity(e.target.value)}
                    min="0"
                    required
                />
            </div>
            <button type="submit" className="btn btn-primary">Add to Cart</button>
        </form>
    </div>
            );
    }

export default AddProductComponent;
