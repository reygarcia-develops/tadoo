import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  username = new FormControl('', [Validators.required, Validators.email]);
  password = new FormControl('', [Validators.required])

  constructor() { }

  ngOnInit() {

  }


  getErrorMessage() {
    return this.username.hasError('required') ? 'Email is required' :
      this.username.hasError('email') ? 'Invalid email' : '';
  }
}
