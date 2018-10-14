const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");

let UserSchema = mongoose.Schema({
  name: {
    type: String
  },
  username: {
    type: String,
    createIndexes: true
  },
  email: {
    type: String
  },
  password: {
    type: String
  }
});

let User = (module.exports = mongoose.model("User", UserSchema));

module.exports.createUser = function(newUser, callback) {
  bcrypt.genSalt(10, function(err, salt) {
    bcrypt.hash(newUser.password, salt, function(err, hash) {
      newUser.password = hash;
      newUser.save(callback);
    });
  });
};

module.exports.getUserByUsername = function(username, callback) {
  const query = { username: username };
  User.findOne(query, callback);
};

module.exports.comparePassword = function(candidatePassword, hash, callback) {
  bcrypt.compare(candidatePassword, hash, (err, isMatch) => {
    if (err) throw err;
    callback(null, isMatch);
  });
};

module.exports.getUserById = function(id, callback) {
  User.findById(id, callback);
};
