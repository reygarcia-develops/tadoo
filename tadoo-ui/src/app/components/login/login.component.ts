import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { trigger, style, animate, transition } from '@angular/animations';


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
  loginForm = this.fb.group({
    username: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required]],
  });

  registerForm = this.fb.group({
    username: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required]],
    fullname: ['', [Validators.required]],
  });

  showLogin = true;

  constructor(private fb: FormBuilder) { }

  ngOnInit() {

  }

  toggleViews() {
    this.showLogin = !this.showLogin;

    if (this.showLogin === true) {
      this.registerForm.reset();
    } else {
      this.loginForm.reset();
    }
  }
}
