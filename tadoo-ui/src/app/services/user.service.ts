import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { UserCreate, UserAuthentication } from '@app/models/user';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private httpClient: HttpClient) { }

  apiURL = 'http://localhost/users/';

  public createUser(userCreate: UserCreate) {
    return this.httpClient.post(`${this.apiURL}`, userCreate);
  }
}
