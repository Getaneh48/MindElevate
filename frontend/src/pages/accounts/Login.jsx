import './login.scss';
import logo from '../../assets/images/MindElevate.png';
import { useRef, useState } from 'react';
import config from '../../config/config';
import { useNavigate } from 'react-router';

export default function Login() {
    const username = useRef();
    const password = useRef();
    const [errors, setErrors] = useState(null);
    const navigate = useNavigate();

    const handleUserLogin = async () => {
        const userInfo = {
            username: username.current.value,
            password: password.current.value,
        }

        const url = `${config.api_url}/login`;
        const header_options = {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userInfo),
        }

        const response = await fetch(url, header_options);
        if (response.ok) {
            const respData = await response.json();
            if (respData.success) {
                setErrors(null);
                localStorage.setItem('access_token', respData.access_token);
                navigate('/melv');
            }
        } else {
            const respError = await response.json();
            if (response.status == 401) {
                setErrors(respError.message)
            }
            
        }

    }

    return (
        <div className="login-container">
            <header className='login-header'>
                <img src={logo} alt="App logo" />
            </header>
            <main className='login-body'>
                <div className="login-form-container">
                    <div className="login-form">
                        <span className="login-form-title">
                            Welcome Back
                        </span>
                        <span className="error-message">{errors ? errors : ''}</span>
                        <div className="login-form-group">
                            <div className="login-form-input-group">
                                <span className="label">Username</span>
                                <input type="text" ref={username}/>
                            </div>
                            <div className="login-form-input-group">
                                <span className="label">Password</span>
                                <input type="password" ref={password} />
                            </div>
                            <button className='login-btn' onClick={handleUserLogin}>Sign in</button>
                        </div>
                    </div>
                </div>
            </main>
            <footer>
                <span className="copyright">Copyright&copy;{new Date().getFullYear()}, MindElevate</span>
            </footer>
        </div>
    )
}