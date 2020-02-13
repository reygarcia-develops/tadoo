import { Component, OnInit } from '@angular/core';

import { User } from '@app/models/user';
import { AuthenticationService } from '@app/services/authentication.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  currentUser: User;

  constructor(private authService: AuthenticationService
  ) {
    this.currentUser = this.authService.currentUserValue;
  }

  ngOnInit() {
  }
}