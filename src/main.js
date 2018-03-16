
class User{
	constructor(username, email, password) {
		this.username = username;
		this.email = email;
		this.password = password;
	}
	static countUsers() {
		console.log('there are 2 users');
	}
	register() {
		console.log(this.username + ' is now registered!');
	}
}

let os = new User('OSAMA', 'osama@email.com', 'password here');

os.register();
User.countUsers();


// inherit from User class in Member class
class Member extends User {
	constructor(username, email, password, memberPackage) {
		super(username, email, password);
		this.package = memberPackage;
	}

	getPackage() {
		console.log(this.username + ' is uses ' + this.package + ' package')
	}
}

let OSAMA = new Member('OSAMA MOHAMED', 'osama2@email.com', 'password here too', 'Standard');

OSAMA.getPackage();
OSAMA.register();