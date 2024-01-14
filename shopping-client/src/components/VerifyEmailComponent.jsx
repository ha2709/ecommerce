import React, { useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function VerifyEmailComponent() {
    const { token } = useParams();

    useEffect(() => {
        const verifyEmail = async () => {
            try {
                const response = await axios.get(`YOUR_BACKEND_URL/verify?token=${token}`);
                console.log(response.data);
                // Handle verification success
            } catch (error) {
                console.error('Email verification failed:', error);
                // Handle verification failure
            }
        };

        if (token) {
            verifyEmail();
        }
    }, [token]);

    return (
        <div>
            Verifying your email...
        </div>
    );
}

export default VerifyEmailComponent;