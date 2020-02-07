export class UserCreate {
  userEmail: string;
  userFullName: string;
  userPassword: string;
}

export class User {
  userEmail: string;
}

export class UserAuthenticate {
  username: string;
  password: string;
}
