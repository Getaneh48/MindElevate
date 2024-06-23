import page_turner_pro_badge from '../assets/images/badges/page-turner-pro.png';
import daily_badge from '../assets/images/badges/daily_badge.png';

const badges = [
    {
        'name': 'Page Turner Pro',
        'icon': page_turner_pro_badge,
    },
    {
        'name': 'dialy',
        'icon': daily_badge
    }
]

export default function getBadge(name) {
    for (let ind in badges) {
        if (badges[ind].name == name) {
            return badges[ind]['icon'];
        }
    }

    return null;
}