export class UserCreate {
  userEmail: string;
  userFullName: string;
  userPassword: string;
}

export class User {
  token?: string;
}

export class UserAuthentication {
  username: string;
  password: string;
}
