import './profile.scss';
import AccountContext from "../../context/AccountContext";
import { useContext } from "react";
import user from '../../assets/images/user.png';

export default function Profile() {
    const {account} = useContext(AccountContext);
    
    return (
        <div className="profile-container">
            <div className="proifle-menu">
                <div className="profile-name">
                    <span className="name">{account?.sub.username}</span>
                    <img src={user} />
                </div>
                <div className="profile-detail"></div>
            </div>
        </div>
    )
}