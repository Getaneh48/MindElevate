import './register.scss';
import logo from '../../assets/images/MindElevate.png';
import { Link, useNavigate } from 'react-router-dom';
import { useRef, useState } from 'react';
import config from '../../config/config';

export default function Register(){
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();
    const username = useRef();
    const email = useRef();
    const password =useRef();
    const confirm_password = useRef();


    function isValidEmail(email) {
        const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        return regex.test(email);
    }

    const validateUserInfo = (user) => {
        const t_errors = {}
        if (user.username == null || user.username == '') {
            t_errors['username'] = "username required";
        }

        if (user.email == null || user.email == '') {
            t_errors['email'] = "email required";
        } else {
            if (!isValidEmail(user.email)) {
                t_errors['email'] = 'Invalid email address';
            }
        }

        if (user.password != user.confirm_password) {
            t_errors['password'] = 'password doesn\'t match';
        } else { 
            if (user.password.length < 8) {
                errors['password'] = 'minimum password length should be 8';
            } else {
                // password complexity checker
                const lowercase = /[a-z]+/;
                const uppercase = /[A-Z]+/;
                const special = /[!@#$%^&*()_+-={}\\[\]|\\:;'<,>.?/~`]/;
                if (!lowercase.test(user.password) ||
                    !uppercase.test(user.password) ||
                    !special.test(user.password)) {
                        t_errors['password'] = 'password does not meet complexity criteria';
                    }
            }
        }
        setErrors(t_errors);
        if (Object.keys(t_errors).length > 0) {
            return false;
        }

        return true;

    }
    const handleUserRegistration = async () => {

        const userInfo = {
            'username': username.current.value,
            'email': email.current.value,
            'password': password.current.value,
            'confirm_password': confirm_password.current.value,
        }

        if (validateUserInfo(userInfo)) {
            const url = `${config.api_url}/register`;
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(userInfo),
                };

                // Make the fetch request
                const response = await fetch(url, options);
                console.log(response);
                if (response.ok) {
                    // Parse the response as JSON
                    const responseData = await response.json();
                    if (responseData.success) {
                        // save the token to a local storage
                        localStorage.setItem('access_token', responseData.access_token)
                        navigate('/melv')
                    }
                } else {
                    if (response.status == 400){
                        const responseData = await response.json();
                        if(responseData.message == 'validation error') {
                            setErrors(responseData.data);
                        }
                    }
                }
        }

        console.log(userInfo);
    }


    return (
        <div className="register-container">
            <header className='register-header'>
                <img src={logo} alt="App logo" />
            </header>
            <main className='register-body'>
                <div className="register-form-container">
                    <div className="register-form">
                        <div className="register-form-title-container">
                            <span className="register-form-title">Welcome to MindElevate</span>
                            <span className="register-form-subtitle">Unlock your reading journey</span>
                        </div>
                        
                        <div className="register-form-group">
                            
                            <div className="register-form-input-group">
                                <span className="label">Username</span>
                                <input type="text" ref={username}/>
                                <span className="error">{'username' in errors ? errors.username : ''}</span>
                            </div>

                            <div className="register-form-input-group">
                                <span className="label">Email</span>
                                <input type="text" ref={email}/>
                                <span className="error">{'email' in errors ? errors.email : ''}</span>
                            </div>

                            <div className="register-form-input-group">
                                <span className="label">Password</span>
                                <input type="password" ref={password}/>
                            </div>

                            <div className="register-form-input-group">
                                <span className="label">Confirm Password</span>
                                <input type="password" ref={confirm_password}/>
                                <span className="error">{'password' in errors ? errors.password : ''}</span>
                            </div>

                            <div className="register-actions">
                                <button className='join-btn' onClick={handleUserRegistration}>Join</button>
                                <div className="separator">
                                    <span className="left-line"><hr /></span>
                                    <span className="or-text">OR</span>
                                    <span className="right-line"><hr /></span>
                                    
                                </div>
                                <div className="privacy-policy">
                                By continuing, you agree to MindElevate&apos;s <Link to="/">Terms of Service</Link> and acknowledge you&apos;ve read our Privacy Policy.
                                </div>
                                <div className="member-confirmation">
                                        <span>Already on MindElevate?</span>
                                        <Link to="/login">Sign in</Link>
                                </div>
                            </div>
                            
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