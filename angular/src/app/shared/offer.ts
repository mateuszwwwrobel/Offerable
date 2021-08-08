export class Category {
    id!: number;
    name!: string;
}

export class Offer {
    id!: string;
    title!: string;
    description!: string;
    price!: number;
    category!: Category;
}
