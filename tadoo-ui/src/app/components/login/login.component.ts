import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { trigger, style, animate, transition } from '@angular/animations';
import { Router, ActivatedRoute } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';


import { AuthenticationService } from '@app/services/authentication.service';
import { UserService } from '@app/services/user.service';
import { UserCreate, UserAuthentication } from '@app/models/user';




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
  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private authService: AuthenticationService,
    private router: Router,
    private route: ActivatedRoute,
    private snackBar: MatSnackBar) { }

  returnUrl: string;
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
    // redirect to home if already logged in
    if (this.authService.currentUserValue && !this.router.isActive('/home', true)) {
      this.router.navigate(['/home']);
    }
    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/home';
  }

  createUser() {
    const userCreate = new UserCreate();
    userCreate.userEmail = this.registerForm.get('username').value;
    userCreate.userFullName = this.registerForm.get('fullname').value;
    userCreate.userPassword = this.registerForm.get('password').value;

    this.userService.createUser(userCreate).subscribe(
      res => {
        // TODO This feels super funky doing. Try and fix this.
        this.loginForm.patchValue({
          username: userCreate.userEmail,
          password: userCreate.userPassword,
        });
        return this.authenticateUser();
      },
      err => {
        if (err.status === 409) {
          this.snackBar.open(err.error.detail, undefined, {
            duration: 5000,
            panelClass: ['snack-error'],
          });
        }
      });
  }

  authenticateUser() {
    const userAuthenticate = new UserAuthentication();
    userAuthenticate.username = this.loginForm.get('username').value;
    userAuthenticate.password = this.loginForm.get('password').value;

    this.authService.authenticateUser(userAuthenticate).subscribe(
      res => {
        this.router.navigate([this.returnUrl]);
      },
      err => {
        if (err.status === 401) {
          this.snackBar.open(err.error.detail, undefined, {
            duration: 5000,
            panelClass: ['snack-error'],
          });
        }
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
