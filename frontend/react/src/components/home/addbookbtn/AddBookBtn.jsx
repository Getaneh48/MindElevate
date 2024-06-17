import { Link } from 'react-router-dom';
import './addbookbtn.scss';

export default function AddBookBtn() {
    return (
        <section className="add-book-section">
                <Link to="/readbook"><span className="add">+</span></Link>
        </section>
    )
}
