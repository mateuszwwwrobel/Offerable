import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Offer, Category } from './offer';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class RestApiService {

  apiURL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  } 

  // HttpClient API get() method => Fetch offers list
  getOffers(): Observable<Offer> {
    return this.http.get<Offer>(this.apiURL + '/offers')
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  // HttpClient API get() method => Fetch categories list
  getCategories(): Observable<Category> {
    return this.http.get<Category>(this.apiURL + '/category')
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  // HttpClient API get() method => Fetch Offer
  getOffer(id: string): Observable<Offer> {
    return this.http.get<Offer>(this.apiURL + '/offers/' + id)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }  

  // HttpClient API post() method => Create Offer
  createOffer(Offer: { title: string; description: string; price: number; category: string; }): Observable<Offer> {
    return this.http.post<Offer>(this.apiURL + '/offers/', JSON.stringify(Offer), this.httpOptions)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }  

  // HttpClient API put() method => Update Offer
  updateOffer(id: string, Offer: any): Observable<Offer> {
    console.log(Offer)
    return this.http.put<Offer>(this.apiURL + '/offers/' + id + '/', JSON.stringify(Offer), this.httpOptions)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  // HttpClient API delete() method => Delete Offer
  deleteOffer(id: string){
    return this.http.delete<Offer>(this.apiURL + '/offers/' + id, this.httpOptions)
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  // Error handling 
  handleError(error: { error: { message: string; }; status: any; message: any; }) {
    let errorMessage = '';
    if(error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
 }

}
