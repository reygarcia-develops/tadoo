import { UserCreate, User } from './user';

describe('UserCreate', () => {
  it('should create an instance', () => {
    expect(new UserCreate()).toBeTruthy();
  });
});

describe('User', () => {
  it('should create an instance', () => {
    expect(new User()).toBeTruthy();
  });
});
