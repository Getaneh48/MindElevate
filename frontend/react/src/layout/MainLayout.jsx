import './mainlayout.scss';
import logo from '../assets/images/MindElevate.png';
import LeftSideMainMenu from '../components/left_side_menus/LeftSideMainMenuLayout';
import user from '../assets/images/user.png';
import Home from '../pages/home/Home';
import { Outlet, useLocation } from 'react-router';
import { useEffect, useState } from 'react';

export default function MainLayout() {
    const location = useLocation();
    const [isDefaultLocation,setIsDefaultLocation] = useState(true);

    useEffect(()=>{
        location.pathname !== '/' ? setIsDefaultLocation(false) : setIsDefaultLocation(true)
    },[location,setIsDefaultLocation])

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
                {isDefaultLocation ? <Home /> : <Outlet />}
                </main>
                <footer>
                    copyright&copy;{new Date().getFullYear()}
                </footer>
            </div>
        </div>
    )
}