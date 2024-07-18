import './mainlayout.scss';
import logo from '../assets/images/MindElevate.png';
import LeftSideMainMenu from '../components/left_side_menus/LeftSideMainMenuLayout';
import warning_icon from '../assets/images/warning.png';
import Home from '../pages/home/Home';
import { Outlet, useLocation, useNavigate } from 'react-router';
import { useEffect, useState} from 'react';
import config from '../config/config';
import { jwtDecode } from 'jwt-decode';
import AccountContext from '../context/AccountContext';
import Profile from '../components/profile/Profile';

export default function MainLayout() {
    const location = useLocation();
    const [isDefaultLocation, setIsDefaultLocation] = useState(true);
    const [notification, setNotification] = useState(null);
    const navigate = useNavigate();
    const [account, setAccount] = useState(null);
    useEffect(() => {
        //check if the user is logged in 
        if (localStorage.getItem('access_token') == 'null' || localStorage.getItem('access_token') == null){
            navigate('/login');
        } else {
            setAccount(jwtDecode(localStorage.getItem('access_token')))
        }
    },[]);

    useEffect(()=>{
        location.pathname !== '/melv' ? setIsDefaultLocation(false) : setIsDefaultLocation(true);
    },[location,setIsDefaultLocation])

    useEffect(()=> {
        const checkNetworkStatus = async () => {
            const url = `${config.api_url}/status`;

            try {
                const options = {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                };
                const response = await fetch(url, options);
                const respData = await response.json();
                if (response.ok) {
                    console.log(respData);
                } else {
                    // authorization error
                    if (response.status == 401) {
                        //check if token expired
                        if (respData.msg === "Token has expired") {
                            console.log('redirect to login...')
                            navigate('/login');
                        }
                    }
                }
               
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
        
    },[])

    return (
        <AccountContext.Provider value={{'account':account, 'token': localStorage.getItem('access_token')}}>
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
                            <Profile />
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
        </AccountContext.Provider>
    )
}