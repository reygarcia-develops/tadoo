import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { UserCreate, UserAuthenticate } from './user';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private httpClient: HttpClient) { }

  apiURL = 'http://localhost/users/';

  public createUser(userCreate: UserCreate) {
    return this.httpClient.post(`${this.apiURL}`, userCreate);
  }

  public authenticateUser(userAuthenticate: UserAuthenticate) {
    console.log(userAuthenticate.password);
    const body = new HttpParams()
      .set('username', userAuthenticate.username)
      .set('password', userAuthenticate.password);

    return this.httpClient.post(`${this.apiURL}token`, body.toString(), {
      headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
    });
  }
}
