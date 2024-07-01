import { Link } from 'react-router-dom';
import './addbookbtn.scss';

export default function AddBookBtn() {
    return (
        <section className="add-book-section">
                <Link to="/melv/readbook"><span className="add">+</span></Link>
        </section>
    )
}
