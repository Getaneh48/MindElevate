import './mainlayout.scss';
import logo from '../assets/images/MindElevate.png';
import LeftSideMainMenu from '../components/left_side_menus/LeftSideMainMenuLayout';
import user from '../assets/images/user.png';
import warning_icon from '../assets/images/warning.png';
import Home from '../pages/home/Home';
import { Outlet, useLocation, useNavigate } from 'react-router';
import { useEffect, useState } from 'react';

export default function MainLayout() {
    const location = useLocation();
    const [isDefaultLocation, setIsDefaultLocation] = useState(true);
    const [notification, setNotification] = useState(null);
    const navigate = useNavigate();

    useEffect(()=>{
        location.pathname !== '/' ? setIsDefaultLocation(false) : setIsDefaultLocation(true);
    },[location,setIsDefaultLocation])

    useEffect(()=> {
        const checkNetworkStatus = async () => {
            const url = 'http://localhost:5001/api/v1/index/status';

            try {
                const response = await fetch(url);
                console.log(response);
            } catch (error) {
                if (error.message == 'Failed to fetch'){
                    setNotification({
                        'icon': warning_icon,
                        'message': 'Network Error',
                    });

                    const interval = setInterval(()=> {
                        window.location.reload(true);
                    }, 5000);

                    return () => clearInterval(interval);
                }
            }
        }

        

        checkNetworkStatus();

        
    },[navigate])

    return (
        <div id="main-container">
            <div className="left-side">
                <LeftSideMainMenu />
            </div>
            <div className="right-side">
                <header className="top">
                    <div className="logo">
                        <img src={logo} className='logo-icon' />
                    </div>
                    <div className="profile-container">
                        <div className="proifle-menu">
                            <div className="profile-info">
                                <span className="name">Getaneh</span>
                                <img src={user} />
                            </div>
                        </div>
                        .
                    </div>
                </header>
                <main>
                    {
                        notification ? (
                            <div className="notification-area">
                                <div className="left-notif">
                                    <div className="notification_icon">
                                        <img src={notification.icon} alt="" />
                                    </div>
                                    <span className="notification-text">{notification.message}</span>
                                </div>
                                <div className="actions">
                                    <span className="close">x</span>
                                </div>
                            </div>
                        ) : (
                            ''
                        )
                    }
                    
                {isDefaultLocation ? <Home setNotification={setNotification}/> : <Outlet />}
                </main>
                <footer>
                    copyright&copy;{new Date().getFullYear()}
                </footer>
            </div>
        </div>
    )
}