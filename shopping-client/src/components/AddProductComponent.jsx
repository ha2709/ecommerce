import React, { useState } from 'react';
import axios from 'axios';

function AddProductComponent() {
    const [productId, setProductId] = useState('');
    const [quantity, setQuantity] = useState(0);

    const handleSubmit = async (event) => {
        event.preventDefault();

        const productData = {
            product_id: productId,
            quantity: Number(quantity)
        };
        const backendURL = `${process.env.REACT_APP_BACKEND_URL}/cart/add_product`;
        const data = new URLSearchParams();
        data.append('product_id', 'theProductId');  
        data.append('quantity', '1');                
        
        const config = {
            headers: {
                'Accept': 'application/json',
                Authorization: `Bearer ${accessToken}`,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        };
    
        try {
            const accessToken = localStorage.getItem('accessToken');
            const response = await axios.post(backendURL, productData, config);
            console.log(response.data);
            
        } catch (error) {
            console.error('Adding product to cart failed:', error);
             
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
