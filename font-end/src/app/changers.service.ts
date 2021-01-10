import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { BehaviorSubject, Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ChangersService {

  constructor(private http: HttpClient) { }

  signUp(details: any): Observable<any> {
    
    const url = 'http://127.0.0.1:5000/signup';
    return this.http.post(url, {data: details});
  }

  login(details: any): Observable<any> {
    const url = 'http://127.0.0.1:5000/signin';
    return this.http.post(url, {data: details});
  }

  addConsumer(details: any): Observable<any> {
    const url = 'http://127.0.0.1:5000/add-consumer';
    return this.http.post(url, {data: details});
  }

  loadAll(details: any): Observable<any> {
    const url = 'http://127.0.0.1:5000/load-all-consumers';
    return this.http.get(url);
  }

}
