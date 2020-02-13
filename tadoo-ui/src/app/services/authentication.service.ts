import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { map, pluck, switchMap } from 'rxjs/operators';

import { UserAuthentication, User } from '@app/models/user';
import { environment } from '@environments/environment';



@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  private currentUserSubject: BehaviorSubject<User>;
  private currentTokenSubject: BehaviorSubject<string>;
  public currentUser: Observable<User>;

  constructor(private httpClient: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
    this.currentTokenSubject = new BehaviorSubject(localStorage.getItem('currentToken'));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): User {
    return this.currentUserSubject.value;
  }

  public get currentTokenValue(): string {
    return this.currentTokenSubject.value;
  }


  authenticateUser(userAuth: UserAuthentication) {
    const body = new HttpParams()
      .set('username', userAuth.username)
      .set('password', userAuth.password);

    return this.httpClient.post(`${environment.apiUrl}/users/token`, body.toString(), {
      headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
    }).pipe(
      switchMap((authResponse: { access_token: string, token_type: string }) => {
        const bearer = `Bearer ${authResponse.access_token}`;

        return this.httpClient.get(`${environment.apiUrl}/users`, {
          headers: new HttpHeaders().set('Authorization', bearer)
        }).pipe(map(user => {
          localStorage.setItem('currentUser', JSON.stringify(user));
          localStorage.setItem('currentToken', authResponse.access_token);
          this.currentUserSubject.next(user);
          this.currentTokenSubject.next(authResponse.access_token);

          return user;
        }));
      })
    );

  }

  logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('currentUser');
    localStorage.removeItem('currentJwt');
    this.currentUserSubject.next(null);
    this.currentTokenSubject.next(null);
  }
}
