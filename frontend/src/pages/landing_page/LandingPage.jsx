import './landingpage.scss';
import logo_icon from '../../assets/images/MindElevate.png';
import { Link } from 'react-router-dom';
import image_1 from '../../assets/images/screenshots/home-snap-1.png';
import searching_image from '../../assets/images/searching.png';
import recommendation_icon from '../../assets/images/screenshots/recommendation.png'

export default function LandingPage() {
    return (
        <div className="landing-page-container">
            <div className="landing-page-header">
                <header>
                    <div className="landing-page-header-left"></div>
                    <div className="landing-page-header-center">
                        <img src={logo_icon} alt="App logo" />
                    </div>
                    <div className="landing-page-header-right">
                        <Link to="/melv"><span className="login">Login</span></Link>
                        <span className="separator">|</span>
                        <Link to="/melv"><span className="register">Create Account</span></Link>
                    </div>
                </header>
            </div>
            <div className="landing-page-body">
                <section className="about">
                    <div className="title">MindElevate</div>
                    <div className="content">
                    <span>Is a platform designed to address the common challange of findng time and motivation to read in the fast paced modern world</span>
                    <div className="shot">
                        <img src={image_1} alt="" />
                    </div>
                    
                    </div>
                </section>

                <section className="content-2">
                    <div className="title">Track your Reading Progress</div>
                    <div className="content">
                    <span>By simplifying the process of tracking reading habits and creating an engaging enviroment, the app makes reading more accessible and enjoyable</span>
                    <div className="shot">
                        <img src={image_1} alt="" />
                    </div>
                    </div>
                </section>

                <section className="content-3">
                    <div className="title">Find books you love the most easly</div>
                    <div className="content">
                    <span>Our platform seamlessly integrates with third-party book service providers, alleviating the need for you to search extensively. Simply express your thoughts, and we’ll promptly deliver the book you’re seeking.</span>
                    <div className="shot">
                        <img src={searching_image} alt="" />
                    </div>
                    </div>
                </section>

                <section className="content-4">
                    <div className="title">Recommendation based on reading habits</div>
                    <div className="content">
                    <span>Our sophisticated algorithms curate personalized recommendations based on your unique reading habits, ensuring a delightful and diverse selection of books tailored just for you. Happy reading! </span>
                    <div className="shot">
                        <img src={recommendation_icon} alt="" />
                    </div>
                    </div>
                </section>
            </div>
            <div className="landing-page-footer"></div>
        </div>
    )
}