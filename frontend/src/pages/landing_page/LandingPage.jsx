import './landingpage.scss';
import logo_icon from '../../assets/images/MindElevate.png';
import { Link } from 'react-router-dom';
import image_1 from '../../assets/images/screenshots/home-snap-1.png';
import searching_image from '../../assets/images/searching.png';
import recommendation_icon from '../../assets/images/screenshots/recommendation.png';
import books_reading_image from '../../assets/images/books-reading.webp';
import user_icon from '../../assets/images/user-2.png';
import github_icon from '../../assets/images/social_icons/github.png';
import linkedin_icon from '../../assets/images/social_icons/linkedin.png';

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
                    <span className="desc">Is a platform designed to address the common challange of findng time and motivation to read in the fast paced modern world <Link to="/melv" className="goto-app">Goto App</Link></span>
                    
                    <div className="shot">
                        <img src={books_reading_image} alt="" />
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

                <section className="content-5">
                    <div className="title">About</div>
                    <div className="content">
                        <p className="description">
                        Ever feel like you should be reading more, but just can&apos;t seem to find the time or motivation?  That was me exactly. I yearned to delve into captivating stories and insightful ideas beyond textbooks, but life kept getting in the way.  Then it hit me – there had to be a better way to cultivate a consistent reading habit.  Imagine my surprise when I couldn&apos;t find an existing platform that combined engaging content with visually-appealing progress tracking.  So, I decided to build the solution myself: <b>MindElevate</b>.

    This app isn&apos;t just about reading more; it&apos;s about reigniting the joy of getting lost in a good book.  In today&apos;s fast-paced world,  social media and technology can steal our focus from the immersive experience of reading. MindElevate is here to change that. It&apos;s about empowering you to rediscover the magic of reading and build a sustainable reading habit – one captivating chapter at a time.
                        </p>
                        <p className='portfolio-project'>This is a Portfolio Project for <Link to="https://www.holbertonschool.com/" target="_blank">Holberton School.</Link></p>
                    </div>
                </section>
                <section className="team-members">
                    <div className="title">Team Members</div>
                    <div className="bio">
                        <img src={user_icon} alt="team member" />
                        <span className="name">Getaneh Alemayehu</span>
                        <span className='role'>Lead Developer</span>

                        <div className="contacts">
                            <div className="social-icons">
                                <Link to="https://github.com/Getaneh48" target="_blank"><img src={github_icon} alt="github" /></Link>
                                <Link to="https://www.linkedin.com/in/getaneh-alemayehu-7a1406b2" target="_blank"><img src={linkedin_icon} alt="linkedin" /></Link>
                            </div>
                        </div>
                    </div>
                   <div className="project-link">
                        <span>MindElevate - <Link to="https://github.com/Getaneh48/MindElevate" target="_blank">Github Repo</Link></span>
                   </div>
                </section>
            </div>
            <div className="landing-page-footer"></div>
            <footer>
                Copyright&copy;{new Date().getFullYear()}
            </footer>
        </div>
    )
}