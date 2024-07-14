import './login.scss';
import logo from '../../assets/images/MindElevate.png';

export default function Login() {
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
                        <div className="login-form-group">
                            <div className="login-form-input-group">
                                <span className="label">Username</span>
                                <input type="text" />
                            </div>
                            <div className="login-form-input-group">
                                <span className="label">Password</span>
                                <input type="password"  />
                            </div>
                            <button className='login-btn'>Sign in</button>
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