import './leftsidemenulayout.scss';
import burger_icon from '../../assets/images/menu.png';
import LeftSideMainMenu from './leftsidemenu/LeftSideMainMenu';

export default function LeftSideMainMenuLayout() {
    return (
        <div className="leftside_menu_container">
            <div className="top">
                <img src={burger_icon} />
            </div>
            <div className="middle">
                <LeftSideMainMenu />
            </div>
            <div className="bottom"></div>
        </div>
    )
}