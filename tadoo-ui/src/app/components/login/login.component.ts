import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { trigger, style, animate, transition } from '@angular/animations';

import { UserService } from './../../user/user.service';
import { UserCreate, UserAuthenticate } from './../../user/user';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  animations: [
    trigger('slideInAndFade', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(100%)' }),
        animate('500ms ease-in', style({ transform: 'translateY(0%)', opacity: 1 }))
      ]),
      transition(':leave', [
      ]),
    ]),
  ]
})

export class LoginComponent implements OnInit {
  constructor(private fb: FormBuilder, private userService: UserService) { }

  loginForm = this.fb.group({
    username: [null, [Validators.required, Validators.email]],
    password: [null, [Validators.required]],
  });

  registerForm = this.fb.group({
    username: [null, [Validators.required, Validators.email]],
    password: [null, [Validators.required]],
    fullname: [null, [Validators.required]],
  });

  showLogin = true;

  ngOnInit() {

  }

  createUser() {
    const userCreate = new UserCreate();
    userCreate.userEmail = this.registerForm.get('username').value;
    userCreate.userFullName = this.registerForm.get('fullname').value;
    userCreate.userPassword = this.registerForm.get('password').value;

    this.userService.createUser(userCreate).subscribe(
      res => {
        console.log('Response:', res);
      },
      err => {
        console.log('Error:', err);
      });
  }
  authenticateUser() {
    const userAuthenticate = new UserAuthenticate();
    userAuthenticate.username = this.loginForm.get('username').value;
    userAuthenticate.password = this.loginForm.get('password').value;

    this.userService.authenticateUser(userAuthenticate).subscribe(
      res => {
        console.log('Response:', res);
      },
      err => {
        console.log('Error:', err);
      });
  }

  toggleViews() {
    this.showLogin = !this.showLogin;

    if (this.showLogin) {
      this.registerForm.reset();
    } else {
      this.loginForm.reset();
    }
  }
}
