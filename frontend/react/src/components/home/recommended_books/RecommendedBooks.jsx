import './recommendedbooks.scss';
import recommended_books_icon from '../../../assets/images/recommended_books.png'
import RecommendedBook from './recommended_book/RecommendedBook';

export default function RecommendedBooks() {
    const recommended_books = [
        {
            "id": "3030151913",
            "title": "Moral Reasoning at Work",
            "subtitle": "Rethinking Ethics in Organizations",
            "authors": "Øyvind Kvalnes",
            "image": "https://www.dbooks.org/img/books/3030151913s.jpg",
            "url": "https://www.dbooks.org/moral-reasoning-at-work-3030151913/"
        },
        {
            "id": "9813299150",
            "title": "Manual of Digital Earth",
            "subtitle": "",
            "authors": "Huadong Guo, Michael F. Goodchild, Alessandro Annoni",
            "image": "https://www.dbooks.org/img/books/9813299150s.jpg",
            "url": "https://www.dbooks.org/manual-of-digital-earth-9813299150/"
        },
        {
            "id": "1491948965",
            "title": "The Art of SEO",
            "subtitle": "Mastering Search Engine Optimization",
            "authors": "Jessie Stricchiola, Stephan Spencer, Eric Enge",
            "image": "https://www.dbooks.org/img/books/1491948965s.jpg",
            "url": "https://www.dbooks.org/the-art-of-seo-1491948965/"
        },
        {
            "id": "5668680406",
            "title": "Advanced Professional Communication",
            "subtitle": "A Principled Approach to Workplace Writing",
            "authors": "Melissa Ashman, Arley Cruthers",
            "image": "https://www.dbooks.org/img/books/5668680406s.jpg",
            "url": "https://www.dbooks.org/advanced-professional-communication-5668680406/"
        },
        {
            "id": "9463722904",
            "title": "Data Visualization in Society",
            "subtitle": "",
            "authors": "Martin Engebretsen, Helen Kennedy",
            "image": "https://www.dbooks.org/img/books/9463722904s.jpg",
            "url": "https://www.dbooks.org/data-visualization-in-society-9463722904/"
          },
          {
            "id": "1911307401",
            "title": "Visualising Facebook",
            "subtitle": "A Comparative Perspective",
            "authors": "Daniel Miller, Jolynna Sinanan",
            "image": "https://www.dbooks.org/img/books/1911307401s.jpg",
            "url": "https://www.dbooks.org/visualising-facebook-1911307401/"
          },
          {
            "id": "1912656396",
            "title": "Cultural Crowdfunding",
            "subtitle": "Platform Capitalism, Labour and Globalization",
            "authors": "Vincent Rouzé",
            "image": "https://www.dbooks.org/img/books/1912656396s.jpg",
            "url": "https://www.dbooks.org/cultural-crowdfunding-1912656396/"
          },
          {
            "id": "3319685880",
            "title": "Political Social Work",
            "subtitle": "Using Power to Create Social Change",
            "authors": "Shannon R. Lane, Suzanne Pritzker",
            "image": "https://www.dbooks.org/img/books/3319685880s.jpg",
            "url": "https://www.dbooks.org/political-social-work-3319685880/"
          },
          {
            "id": "3319925318",
            "title": "Mediation in Collective Labor Conflicts",
            "subtitle": "",
            "authors": "Martin Euwema, Francisco Medina, Ana Belén García, Erica Romero Pender",
            "image": "https://www.dbooks.org/img/books/3319925318s.jpg",
            "url": "https://www.dbooks.org/mediation-in-collective-labor-conflicts-3319925318/"
          },
          {
            "id": "1137506806",
            "title": "New Frontiers in Social Innovation Research",
            "subtitle": "",
            "authors": "Alex Nicholls, Julie Simon, Madeleine Gabriel",
            "image": "https://www.dbooks.org/img/books/1137506806s.jpg",
            "url": "https://www.dbooks.org/new-frontiers-in-social-innovation-research-1137506806/"
          },

    ]
    return (
        <section className="recommended_books_container">
            <div className="rbooks_header">
                    <img src={recommended_books_icon} alt="Handbook of Medical Herbs"/>
                    <div className="title">Recommended Books</div>
            </div>
            <div className="rbooks_body">
                {
                    recommended_books.map((rbook, index) => {
                        return (
                            <RecommendedBook rbook={rbook} key={index} />
                        )
                    })
                }
                
            </div>
        </section>
    )
}