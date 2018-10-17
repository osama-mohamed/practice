const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");
const expressHandlebars = require("express-handlebars");
const nodemailer = require("nodemailer");
const flash = require("connect-flash");
const session = require("express-session");
const firebase = require("firebase");
const os = require("os");
const https = require("https");
const port = process.env.PORT || 3000;
const app = express();

app.set("views", path.join(__dirname, "views"));
app.engine("handlebars", expressHandlebars());
app.set("view engine", "handlebars");
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
require("dotenv").config();

const config = {
  apiKey: process.env.APIKEY,
  authDomain: process.env.AUTHDOMAIN,
  databaseURL: process.env.DATABASEURL,
  projectId: process.env.PROJECTID,
  storageBucket: process.env.STORAGEBUCKET,
  messagingSenderId: process.env.MESSAGINGSENDERID
};
firebase.initializeApp(config);

app.use(
  session({
    secret: "secretKey",
    resave: true,
    saveUninitialized: true
    // cookie: { secure: true }
  })
);
app.use(flash());
app.use(function(req, res, next) {
  res.locals.success_msg = req.flash("success_msg");
  res.locals.error_msg = req.flash("error_msg");
  next();
});

app.get("/", (req, res) => {
  res.render("contact");
});

app.post("/send", (req, res) => {
  const newMessage = {
    name: req.body.name,
    company: req.body.company,
    email: req.body.email,
    phone: req.body.phone,
    message: req.body.message,
    time: new Date().toJSON(),
    host: os.networkInterfaces(),
    user: {
      USERDOMAIN: process.env.USERDOMAIN,
      USERDOMAIN_ROAMINGPROFILE: process.env.USERDOMAIN_ROAMINGPROFILE,
      USERNAME: process.env.USERNAME,
      system: process.platform,
      ip: [req.socket.remoteAddress, req.connection.remoteAddress],
      globalIP: ""
    }
  };
  
  const id = firebase
    .database()
    .ref("messages")
    .push(newMessage).key;
  firebase
    .database()
    .ref("messages")
    .once("value")
    .then(data => {
      const obj = data.val();
      for (let key in obj) {
        if (key == id) {
          // console.log("obj[key] == : ", obj[key]);
          const updateglobalIP = {};
          https.get({ host: "api.ipify.org" }, response => {
            let ip = "";
            response.on("data", d => {
              ip += d;
              updateglobalIP['user/globalIP'] = ip;
              firebase.database().ref('messages').child(id).update(updateglobalIP);
            });
          });
        }
      }
    });
  const outputPlainText = ` 
    Name: ${req.body.name}, 
    Company: ${req.body.company} 
    Email: ${req.body.email} 
    Phone: ${req.body.phone} 
    Message : ${req.body.message}`;
  const output = `
    <h3>Contact Details</h3>
    <ul>  
    <li>Name: ${req.body.name}</li>
    <li>Company: ${req.body.company}</li>
    <li>Email: ${req.body.email}</li>
    <li>Phone: ${req.body.phone}</li>
    </ul>
    <h3>Message</h3>
    <p>${req.body.message}</p>`;

  let transporter = nodemailer.createTransport({
    // host: process.env.HOST2,
    // auth: {
    //   user: process.env.USER2,
    //   pass: process.env.PASSWORD2
    // },
    host: "smtp.gmail.com",
    port: 465,
    secure: true,
    auth: {
      user: process.env.USER,
      pass: process.env.PASSWORD
    },
    tls: {
      rejectUnauthorized: false
    }
  });

  let mailOptions = {
    // from: `"Node Mailer" ${process.env.USER2}`,
    from: `"Node Mailer" ${process.env.USER}`,
    to: req.body.email,
    subject: req.body.name,
    text: outputPlainText,
    html: output
  };

  if (req.body.email == "") {
    req.flash("error_msg", "No recipients found");
    res.redirect("/");
  } else {
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        req.flash("error_msg", "An error occurred");
        res.redirect("/");
      } else {
        req.flash("success_msg", "Your email has been sent successfully!");
        res.redirect("/");
      }
    });
  }
});

app.listen(port, () => {
  console.log("Server started on port " + port);
});
