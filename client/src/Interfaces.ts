export interface Product {
  id?: number;
  name: string;
  description: string;
  price: number;
  raiting?: number;
  stock: number;
  category: string;
  image: File | null;
  quiantity?: number;
  reviews: number;
}
export interface Token {
  exp: number;
}
