import React, { useState } from 'react';
import axios from 'axios';

function DiscountConfigComponent() {
    const [customerCategory, setCustomerCategory] = useState('');
    const [productCategoryId, setProductCategoryId] = useState('');
    const [percentage, setPercentage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const accessToken = localStorage.getItem('accessToken');
            const backendURL = `${process.env.REACT_APP_BACKEND_URL}/discounts`
            const discountData = {
                customer_category: customerCategory,
                product_category_id: productCategoryId,
                percentage: parseFloat(percentage) / 100, //  the percentage should be submitted as a decimal
            };
            
            const response = await axios.post(backendURL, discountData, {
                headers: {
                    'Accept': 'application/json',
                    Authorization: `Bearer ${accessToken}`,
                    'Content-Type': 'application/json'
                }
            });
            console.log(response.data);
             
        } catch (error) {
            console.error('Error creating discount:', error);
            
        }
    };

    return (
        <div className="container mt-5">
            <h2>Configure Discount</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="customerCategory" className="form-label">Customer Category</label>
                    <input
                        type="text"
                        className="form-control"
                        id="customerCategory"
                        value={customerCategory}
                        onChange={(e) => setCustomerCategory(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="productCategoryId" className="form-label">Product Category ID</label>
                    <input
                        type="text"
                        className="form-control"
                        id="productCategoryId"
                        value={productCategoryId}
                        onChange={(e) => setProductCategoryId(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="percentage" className="form-label">Discount Percentage</label>
                    <input
                        type="number"
                        className="form-control"
                        id="percentage"
                        value={percentage}
                        onChange={(e) => setPercentage(e.target.value)}
                        placeholder="Enter percentage as a whole number (e.g., 10 for 10%)"
                        required
                   
                    />
                </div>
                <button type="submit" className="btn btn-primary">Create Discount</button>
            </form>
            </div>
);
}

export default DiscountConfigComponent;